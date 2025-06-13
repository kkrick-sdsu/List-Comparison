import csv
import os
import types
import pathlib

# Load the list-comparison module while skipping the trailing invocation of
# `list_comparison()` so that no interactive prompts execute during import.
MODULE_PATH = pathlib.Path(__file__).resolve().parents[1] / 'list-comparison.py'
source_lines = MODULE_PATH.read_text().splitlines()
module_source = "\n".join(source_lines[:-1])
list_comparison = types.ModuleType("list_comparison")
exec(module_source, list_comparison.__dict__)


def test_unique_elements():
    result = list_comparison.unique_elements([1, 2, 3], [3, 4, 5])
    assert result["list_one"] == [1, 2]
    assert result["list_two"] == [4, 5]


def test_intersection_elements():
    assert list_comparison.intersection_elements([1, 2, 3], [3, 4]) == [3]


def test_union_elements():
    assert list_comparison.union_elements([1, 2], [2, 3]) == [1, 2, 3]


def test_output_elements(tmp_path):
    out_file = tmp_path / "out.csv"
    list_comparison.output_elements(["a", "b"], "header", out_file)
    with open(out_file, newline="") as f:
        rows = list(csv.reader(f))
    assert rows == [["h", "e", "a", "d", "e", "r"], ["a"], ["b"]]


def test_read_file_nonexistent():
    assert list_comparison.read_file("nonexistent_file.csv") == ""
