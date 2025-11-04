from .vocab_generator import generate_vocab

# INPUT_FILE = "../datasets/test_barrage.json"
# OUTPUT_FILE = "../vocabs/test_barrage_vocab.txt"

INPUT_FILE = "../datasets/barrage.json"
OUTPUT_FILE = "../vocabs/barrage_vocab.json"

if __name__ == "__main__":
    generate_vocab(input_file=INPUT_FILE, output_file=OUTPUT_FILE)