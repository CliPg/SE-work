from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
import os

vector_db_path = "../vector_db/barrage_vector_db"
embeddings = DashScopeEmbeddings(
    model="text-embedding-v4",
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")
)
vector_db = Chroma(persist_directory=vector_db_path, embedding_function=embeddings)

docs = vector_db.get()
print(docs)