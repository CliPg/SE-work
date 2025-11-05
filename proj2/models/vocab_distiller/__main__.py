from .vocab_distiller import distill_vocab_with_llm, distill_vocab_with_sentence_transformer
import sys
INPUT_FILE = "../vocabs/barrage_vocab.json"
OUTPUT_FILE = "../vocabs/ai_related_vocab_with_llm.json"
MODEL_NAME = "qwen3-max"

if __name__ == "__main__":

    mode = sys.argv[1].lower()

    if mode == "llm":
        # 使用llm蒸馏
        distill_vocab_with_llm(input_file=INPUT_FILE, output_file=OUTPUT_FILE, model_name=MODEL_NAME)
    elif mode == "sentence":
        # 使用sentence_transformer蒸馏
        distill_vocab_with_sentence_transformer(input_file=INPUT_FILE, output_file=OUTPUT_FILE)
    