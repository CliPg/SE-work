import cProfile
import pstats
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.vocab_generator.vocab_generator import generate_vocab

def main():
    # 这里放你要测试的主函数，比如爬虫或数据处理逻辑
    INPUT_FILE = "../datasets/barrage.json"
    OUTPUT_FILE = "../vocabs/barrage_vocab.json"
    generate_vocab(input_file=INPUT_FILE, output_file=OUTPUT_FILE)


# python -m cProfile -o profile.stats vocab_profiling.py
# snakeviz profile.stats
if __name__ == "__main__":
    main()