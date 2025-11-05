import os
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import Chroma
import json

def build_vector_db(input_file, vector_db_path, model_name):
    embeddings = DashScopeEmbeddings(
        model=model_name,
        dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")
    )

    i = 0
    with open(input_file, 'r', encoding='utf-8') as f:
        texts = []
        for line in f:
            line = line.strip()
            if line:
                data = json.loads(line)
                barrages = data.get("barrages", [])
                
                for b in barrages:
                    texts.append(b)
            i += 1
            if i % 10 == 0:
                print(f"Processed {i} lines")

    print("Building vector database...")
    persist_directory = vector_db_path
    vector_db = Chroma.from_texts(
        texts=texts,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    vector_db.persist()
    print(f"Vector database built and saved to {vector_db_path}")
