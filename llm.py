import os
import getpass

os.environ[
    'OPENAI_API_KEY'] = "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"

from langchain_openai import ChatOpenAI

# from langchain.text_splitter import CharacterTextSplitter
# from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
# from langchain_community.vectorstores import Qdrant
from langchain.chains import RetrievalQAWithSourcesChain

# loader = TextLoader("opt_str_new.txt")
# documents = loader.load()
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# docs = text_splitter.split_documents(documents)
# embeddings = OpenAIEmbeddings()
db = FAISS.load_local("faiss_store", OpenAIEmbeddings())

retriever = db.as_retriever()
model = RetrievalQAWithSourcesChain.from_chain_type(llm=ChatOpenAI(),
                                                    chain_type="stuff",
                                                    retriever=retriever)

response = model({"question": "how are you?"}, return_only_outputs=True)
print(response['answer'])


def resp(question):
  response = model({"question": question}, return_only_outputs=True)
  return response['answer']
