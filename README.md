# Ask Your CSV 📈

This Streamlit web application allows users to ask questions about their CSV files using natural language processing (NLP) powered by OpenAI's language models.

## Overview

This application provides a user-friendly interface for uploading CSV files and querying them using natural language. It utilizes the Streamlit framework for building interactive web applications and integrates with OpenAI's language models for processing user queries.

## Usage

To use the application, follow these steps:

1. **Upload your CSV file**: Click on the "Upload your CSV file" button to select and upload your CSV file.

2. **Ask your question about your CSV file**: Enter your question about the CSV file in the text input field provided.

3. **View the response**: Once you've entered your question, the application will process it using OpenAI's language model and provide you with the response.

## Requirements

Ensure you have the following dependencies installed to run the application:

- Python 3.x
- Streamlit
- LangChain (langchain)
- LangChain Experimental (langchain_experimental)
- LangChain OpenAI (langchain_openai)
- dotenv

Install the dependencies using pip:

```bash
pip install streamlit langchain langchain_experimental langchain_openai python-dotenv
```

## Running the Application

To run the application, execute the following command in your terminal:

```bash
streamlit run app.py
```

This command will start a local server hosting the web application. You can access the application in your web browser by navigating to the provided URL.

## Configuration

The application uses environment variables for configuration. Ensure you have a `.env` file in the project directory with the required variables.

## About

This project is maintained by me. Feel free to contribute by submitting bug reports, feature requests, or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
