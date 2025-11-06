from adapters import (
    run_scratch_barrage as scratch_barrage,
)

def test_scratch_barrage():
    output_file = 'test_dataset/test_barrage.json'
    keyword = 'LLM'
    num = 2

    out_put = scratch_barrage(output_file, keyword, num)
    assert out_put == num