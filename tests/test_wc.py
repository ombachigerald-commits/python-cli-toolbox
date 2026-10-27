import pytest
from src.wc import count_file

def test_count_file(tmp_path):
    f = tmp_path / "test.txt"
    f.write_text("Hello world\nThis is a test.")
    res = count_file(f)
    assert res["lines"] == 2
    assert res["words"] == 6
