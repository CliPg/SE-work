MODEL_NAME = "qwen3-max"
from openai import OpenAI
import os
import json
from sentence_transformers import SentenceTransformer, util

def distill_vocab_with_llm(input_file, output_file, model_name, batch_size=30):

    client = OpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    words = []
    freqs = {}

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            word_data = json.loads(line)
            words.append(word_data["word"])
            freqs[word_data["word"]] = word_data["frequency"]

    ai_related = []
    total_prompt_tokens = 0
    total_completion_tokens = 0

    # 按批次处理
    for i in range(0, len(words), batch_size):
        batch = words[i:i + batch_size]
        prompt = (
            "请判断以下词语是否与“人工智能技术应用”相关。"
            "输出 JSON 格式：{'词语': true/false}。\n\n"
            + "\n".join(batch)
        )

        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
        )

        usage = response.usage
        total_prompt_tokens += usage.prompt_tokens
        total_completion_tokens += usage.completion_tokens
        print(f"Batch {i//batch_size+1} tokens: {usage.total_tokens}")

        result = response.choices[0].message.content.strip()

        try:
            result_json = json.loads(result)
        except json.JSONDecodeError:
            print("模型输出解析失败，跳过该批次")
            continue

        for word, related in result_json.items():
            if related is True:
                ai_related.append((word, freqs[word]))

    ai_related.sort(key=lambda x: x[1], reverse=True)

    with open(output_file, "w", encoding="utf-8") as f:
        for word, freq in ai_related:
            json_line = json.dumps({"word": word, "frequency": freq}, ensure_ascii=False)
            f.write(json_line + "\n")

    print(f"\n总 token 使用情况：输入 {total_prompt_tokens}，输出 {total_completion_tokens}，总计 {total_prompt_tokens + total_completion_tokens}")
    

def distill_vocab_with_sentence_transformer(input_file: str, output_file: str):
    model = SentenceTransformer("shibing624/text2vec-base-chinese")
    topic = "人工智能 技术 应用"
    topic_vec = model.encode(topic, convert_to_tensor=True)
    ai_related = []
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            word_data = json.loads(line)
            word = word_data["word"]
            word_vec = model.encode(word, convert_to_tensor=True)
            sim = util.cos_sim(topic_vec, word_vec).item()
            if sim >= 0.5:
                ai_related.append((word, word_data["frequency"], sim))

    ai_related.sort(key=lambda x: x[1], reverse=True)
    with open(output_file, "w", encoding="utf-8") as f:
        for word, freq, sim in ai_related:
            json_line = json.dumps({"word": word, "frequency": freq, "similarity": sim}, ensure_ascii=False)
            f.write(json_line + "\n")