import json
import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def jsonl_to_excel(jsonl_file: str, excel_file: str):
    """
    将一行一个JSON对象的文件（JSONL）转换为Excel文件

    Args:
        jsonl_file (str): 输入 JSONL 文件路径
        excel_file (str): 输出 Excel 文件路径
    """
    data = []

    # 逐行读取 JSONL 文件
    with open(jsonl_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError:
                print(f"第 {line_num} 行不是合法 JSON，已跳过")

    # 转换为 DataFrame
    df = pd.DataFrame(data)

    # 写入 Excel 文件
    df.to_excel(excel_file, index=False)

    print(f"已成功将 {jsonl_file} 转换为 {excel_file}")
    print(f"共 {len(df)} 行数据")

if __name__ == "__main__":
    jsonl_to_excel("../vocabs/ai_related_vocab_with_human.json", "../vocabs/ai_related_vocab_with_human.xlsx")