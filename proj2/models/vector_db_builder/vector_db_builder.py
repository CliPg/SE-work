import os
import json
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import Chroma

def build_vector_db(input_file, vector_db_path, model_name, batch_size=1000):
    """
    分批构建向量数据库，避免一次性加载全部弹幕到内存。
    """

    # 初始化嵌入模型
    embeddings = DashScopeEmbeddings(
        model=model_name,
        dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")
    )

    # 若数据库不存在，则新建；存在则加载后追加
    vector_db = Chroma(
        persist_directory=vector_db_path,
        embedding_function=embeddings
    )

    texts = []
    total = 0

    i = 0
    with open(input_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue

            try:
                data = json.loads(line)
                barrages = data.get("barrages", [])
                texts.extend(barrages)
            except json.JSONDecodeError:
                print(f"JSON格式错误：第 {line_num} 行")
                continue

            # 达到批次大小就写入数据库
            if len(texts) >= batch_size:
                print(f"正在写入 {len(texts)} 条弹幕...")
                vector_db.add_texts(texts)
                vector_db.persist()
                total += len(texts)
                texts.clear()  # 清空缓存
            i += 1
            print(f"已处理 {i} 行数据")
        # 处理最后一批不足 batch_size 的部分
        if texts:
            print(f"正在写入最后 {len(texts)} 条弹幕...")
            vector_db.add_texts(texts)
            vector_db.persist()
            total += len(texts)

    print(f"向量数据库构建完成，共添加 {total} 条弹幕。")
    print(f"数据已保存至：{vector_db_path}")