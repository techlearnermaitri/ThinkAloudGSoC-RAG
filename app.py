import streamlit as st
import os
import pymupdf as pdf
import pandas as pd
import base64


#langchian imports
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchian_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchai.prompts import PromptTemplate

from datetime  import datetime

<<<<<<< HEAD
#text chunking to get text from pdf
def get_pdf_text(pdf_doc):
    text="" #this is oen  empty string
    for pdf in pdf_docs:
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text

#to get chunks of text
=======
#text chunking imports
>>>>>>> ff8b6d2 (imported neccesary files and create a myenv)
