import jieba
import re
import json
from collections import Counter

def generate_vocab(input_file: str, output_file: str):
    """
    从 JSON 行文件中提取弹幕内容并生成词表

    Args:
        input_file (str): 输入 JSON 行文件路径（每行一个视频的弹幕数据）
        output_file (str): 输出词表文件路径
    """
    jieba.enable_parallel(4)
    all_words = []

    # 1. 按行读取 JSON 文件
    with open(input_file, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
                barrages = data.get("barrages", [])
                if not isinstance(barrages, list):
                    continue

                # 2. 对每个弹幕分词并收集结果
                for text in barrages:
                    words = jieba.lcut(text)
                    # 过滤无意义词，只保留中文、英文、数字，长度>1
                    words = [w for w in words if re.match(r'^[\u4e00-\u9fa5a-zA-Z0-9]+$', w) and len(w) > 1]
                    all_words.extend(words)

            except json.JSONDecodeError:
                print(f"第 {line_num} 行不是合法 JSON，已跳过")

    # 3. 统计词频
    word_freq = Counter(all_words)

    # 4. 按词频排序并保存到文件
    with open(output_file, "w", encoding="utf-8") as f:
        for word, freq in word_freq.most_common():
            json_line = json.dumps({"word": word, "frequency": freq}, ensure_ascii=False)
            f.write(json_line + "\n")

    print(f"词表已生成：{output_file}")
    print(f"共统计到 {len(word_freq)} 个不同的词语")
