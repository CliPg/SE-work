from .wordcloud_generator import generate_wordcloud

INPUT_FILE = "../vocabs/ai_related_vocab_with_human.json"
OUTPUT_FILE = "../imgs/wordcloud.png"

if __name__ == "__main__":
    generate_wordcloud(input_file=INPUT_FILE, output_file=OUTPUT_FILE)