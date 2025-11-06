from adapters import (
    run_generate_vocab as generate_vocab
)

def test_generate_vocab():
    input_file = 'test_dataset/test_barrage.json'
    output_file = 'test_dataset/test_vocab.json'

    generate_vocab(input_file, output_file)

    with open(output_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    assert len(lines) > 0