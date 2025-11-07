from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import Chroma
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.llm import client

def build_retriever():

    model_name = "text-embedding-v4"
    vector_db_path = "../vector_db/barrage_vector_db"

    embeddings = DashScopeEmbeddings(
        model=model_name,
        dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")
    )

    vector_db = Chroma(
        persist_directory=vector_db_path,
        embedding_function=embeddings
    )

    retriever = vector_db.as_retriever(search_kwargs={"k": 5})
    return retriever

def quest(question):
    retriever = build_retriever()
    docs = retriever.invoke(question)
    
    messages = []
    system_prompt = f"你是一个专业的人工智能技术助理，擅长从弹幕内容中提取有价值的信息。根据用户的问题，结合以下弹幕内容，提供简洁且准确的回答。以下是从向量数据库检索的弹幕内容：\n"
    for doc in docs:
        print(f"retrieve: {doc.page_content}")
        system_prompt += f"- {doc.page_content}\n"
    messages.append({"role": "system", "content": system_prompt})

    user_prompt = f"请根据上述弹幕内容，回答用户的问题。如果弹幕内容中没有相关信息，请礼貌地说明无法回答。以下是用户的问题{question}"
    messages.append({"role": "user", "content": user_prompt})

    response = client.chat.completions.create(
        model="qwen3-max",
        messages=messages,
    )

    result = response.choices[0].message.content.strip()

    print(result)


if __name__ == "__main__":
    question1 = "大语言模型技术的应用成本的主流看法是什么？"
    question2 = "大语言模型技术的潜在应用领域的主流看法是什么"
    question3 = "大语言模型技术的带来的不利影响有哪些"
    
    questions = [question1, question2, question3]
    
    for question in questions:
        print(f"问题: {question}")
        quest(question)
        print("-" * 50)