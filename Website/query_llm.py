from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from transformers import AutoTokenizer, pipeline
from langchain import PromptTemplate
import torch
import json
import time
import pathlib
import os

# Define document class
class Document:
    def __init__(self, page_content, metadata=None):
        self.page_content = page_content
        self.metadata = metadata if metadata is not None else {}

# Load documents from the directory with the specified encoding
class UTF8TextLoader(TextLoader):
    def lazy_load(self):
        with open(self.file_path, encoding='utf-8') as f:
            text = f.read()
        return [Document(text)]

loader = DirectoryLoader('data/', glob="*.txt", loader_cls=UTF8TextLoader)
documents = loader.load()

# Split documents into manageable chunks
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = splitter.split_documents(documents)

# Initialize the embeddings model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device': 'cpu'})

# Create a vector store from the documents
vectorstore = FAISS.from_documents(texts, embeddings)
vectorstore.save_local("faiss")

# Load the FAISS index and create a retriever
db = FAISS.load_local("faiss", embeddings, allow_dangerous_deserialization=True)
retriever = db.as_retriever(search_kwargs={'k': 1})

# Define the template for the prompt
template = """ Context: {context} Question: {question} """
prompt = PromptTemplate(
    template=template,
    input_variables=['context', 'question']
)
    
# Initialize the Hugging Face pipeline for question answering
llm = Ollama(model="llama3")

# Set up the RetrievalQA chain
QA_LLM = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={'prompt': prompt}
)

def query(model, question):
    model_path = model.combine_documents_chain.llm_chain.llm.model
    model_name = pathlib.Path(model_path).name
    time_start = time.time()
    output = model({'query': question})
    response = output["result"]
    time_elapsed = time.time() - time_start

    # Extract and return the source document and response
    source_document = output['source_documents'][0].page_content
    result = f"Response time: {time_elapsed:.02f} sec\n"
    result += f"Question: {question}\n"
    result += f"Answer: {response}\n\n"
    result += f"Source Document:\n {source_document}\n"

    # Convert newlines to HTML <br> tags
    result = result.replace("\n", "<br>")

    return result

def query_llm(question):
    return llm.invoke(question)