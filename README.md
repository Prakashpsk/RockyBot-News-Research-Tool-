# RockyBot: News Research Tool 📈

Welcome to **RockyBot**, a sophisticated news research tool designed to process and analyze news articles, providing you with concise and informative summaries.

![Roky](https://github.com/Prakashpsk/RockyBot-News-Research-Tool-/blob/main/Screenshot%202024-07-06%20213422.png)

## Table of Contents

1. [Introduction](#introduction)
2. [Agenda](#agenda)
3. [Skills and Technologies Used](#skills-and-technologies-used)
4. [Features](#features)
5. [Setup and Installation](#setup-and-installation)
6. [Usage](#usage)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

## Introduction

RockyBot leverages advanced language processing models to provide accurate and concise answers to questions based on the content of news articles. It aims to assist researchers, journalists, and anyone interested in extracting key information from lengthy articles quickly and efficiently.

## Agenda

- Load and process news articles from given URLs.
- Generate embeddings using Google's Gemini model.
- Store embeddings in a Chroma vector store.
- Retrieve and answer questions based on processed news content.
- Display sources of information for transparency.

## Skills and Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For creating the web interface.
- **LangChain**: For document processing and embedding.
- **Google Gemini API**: For generating embeddings and language model interaction.
- **Chroma**: For storing and retrieving vectorized documents.
- **dotenv**: For managing environment variables.

## Features

- **User-Friendly Interface**: Easy-to-use Streamlit web application.
- **URL Processing**: Load and process multiple news article URLs.
- **Advanced Embeddings**: Use Google Gemini for accurate embeddings.
- **Question Answering**: Retrieve concise answers from the processed content.
- **Source Transparency**: Display sources of the information provided.

## Setup and Installation

Follow these steps to set up and run RockyBot on your local machine:

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)
- Anaconda (optional but recommended for managing virtual environments)

### Installation

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/rockybot.git
cd rockybot
