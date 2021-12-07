from my_funcs.file_workers import read_from_file
from my_funcs.utils import division
import pytest


def create_test_data(test_data):
    # we append the file and then write data into it
    with open('test/prod_file_copy.txt', 'a') as f_o:
        f_o.writelines(test_data)

# conftest.py is file similar to package.json with roadmap of behavior

# at the end of configuration ::test_read_from_file - to use only one test by name
def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three\n', 'four\n', 'five\n', 'six\n', 'seven\n', 'eight\n', 'nine\n', 'ten\n']
    create_test_data(test_data)
    assert test_data == read_from_file('test/prod_file_copy.txt')


def test_read_from_file2():
    test_data = ['one\n', 'two\n', 'three\n' ]
    create_test_data(test_data)
    assert test_data == read_from_file('test/prod_file_copy.txt')

#allows to skip
@pytest.mark.skip(reason="test")
def test_read_from_file3():
    test_data = ['one\n', 'two\n', 'three\n']
    create_test_data(test_data)
    assert test_data == read_from_file('test/prod_file_copy.txt')

# we import this test from utils and we delibarately fail it and mark it as such so it does not show as fail
@pytest.mark.xfail
def test_divide_fail():
    assert division(4, 2) == 3





