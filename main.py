import os
import streamlit as st
import time
from langchain import PromptTemplate
from langchain.docstore.document import Document
from langchain.document_loaders import WebBaseLoader
from langchain.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set API key for Gemini
os.environ['GOOGLE_API_KEY'] = 'AIzaSyA9NCNH7dEORDMgbj9LmLBJPxXOhNzsFXY'

st.title("RockyBot: News Research Tool 📈")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i + 1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
persist_directory = "./chroma_db"

main_placeholder = st.empty()

# Initialize the Gemini embeddings
gemini_embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

if process_url_clicked:
    # Load data from URLs
    data = []
    for url in urls:
        if url:
            loader = WebBaseLoader(url)
            main_placeholder.text(f"Data Loading from {url}...Started...✅✅✅")
            data.extend(loader.load())

    # Extract text content and process
    combined_text = ""
    for doc in data:
        text_content = doc.page_content

        # Safely split the text content
        if "code, audio, image and video." in text_content and "Cloud TPU v5p" in text_content:
            text_content_1 = text_content.split("code, audio, image and video.", 1)[1]
            final_text = text_content_1.split("Cloud TPU v5p", 1)[0]
            combined_text += final_text
        else:
            combined_text += text_content  # Or handle it differently if needed

    # Convert the text to LangChain's Document format
    docs = [Document(page_content=combined_text, metadata={"source": "local"})]

    # Create embeddings and save to Chroma vector store
    vectorstore = Chroma.from_documents(documents=docs, embedding=gemini_embeddings,
                                        persist_directory=persist_directory)
    vectorstore.persist()

    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)

query = main_placeholder.text_input("Question: ")
if query:
    # Load the Chroma vector store from the persisted directory
    vectorstore = Chroma(persist_directory=persist_directory, embedding_function=gemini_embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 1})
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7, top_p=0.85)
    llm_prompt_template = """You are an assistant for question-answering tasks.
    Use the following context to answer the question.
    If you don't know the answer, just say that you don't know.
    Use five sentences maximum and keep the answer concise.\n
    Question: {question} \nContext: {context} \nAnswer:"""
    llm_prompt = PromptTemplate.from_template(llm_prompt_template)


    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)


    rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | llm_prompt
            | llm
            | StrOutputParser()
    )

    result = rag_chain.invoke(query)
    st.header("Answer")
    if isinstance(result, str):
        st.write(result)
    else:
        st.write(result.get("answer", "No answer found"))

    # Display sources, if available
    if isinstance(result, dict):
        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")
            sources_list = sources.split("\n")  # Split the sources by newline
            for source in sources_list:
                st.write(source)
