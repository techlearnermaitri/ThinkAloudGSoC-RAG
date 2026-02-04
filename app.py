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
def get_text_chunks(text,model_name):
    if model_name=="Google AI":
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=1000)
    chunks=text_splitter.split_text(text)
    return chunks

#embedding chunks and them in vector store 
def get_vector_store(text_chunks,model_name,api_key=None):
    if model_name == "Google AI":
        embeddings=GoogleGenerativeAIEmbeddings(model="model/embedding-001",google_api_keys=api_key)
    vector_store=FAISS.from_texts(text_chunks,embedding=embeddings)
    vector_store.save_local("faiss_index")
    return vector_store