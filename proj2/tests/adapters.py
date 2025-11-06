import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.scratcher.scratch_barrage import scratch_barrage
from models.vocab_generator.vocab_generator import generate_vocab


# pytest -k test_scratch_barrage
def run_scratch_barrage(output_file: str, keyword: str, num: int):
    return scratch_barrage(output_file, keyword, num)

# pytest -k test_generate_vocab
def run_generate_vocab(input_file: str, output_file: str):
    return generate_vocab(input_file, output_file)