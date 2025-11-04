from .vocab_distiller import distill_vocab_with_llm, distill_vocab_with_sentence_transformer

INPUT_FILE = "../vocabs/barrage_vocab.json"
OUTPUT_FILE = "../vocabs/ai_related_vocab_with_llm.json"
MODEL_NAME = "qwen3-max"

if __name__ == "__main__":
    # distill_vocab_with_sentence_transformer(input_file=INPUT_FILE, output_file=OUTPUT_FILE)
    distill_vocab_with_llm(input_file=INPUT_FILE, output_file=OUTPUT_FILE, model_name=MODEL_NAME)
    