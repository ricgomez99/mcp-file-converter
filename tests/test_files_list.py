import pytest
from helpers import Files_List

@pytest.fixture
def files_list():
    """Creates an instance of the linked list"""
    return Files_List()

def test_inset_items(files_list):
    assert files_list.insert('file1.pdf') == True
    assert files_list.insert('file2.pdf') == True

def test_insert_repeated_item(files_list):
    files_list.insert('file.pdf')
    with pytest.raises(ValueError):
        files_list.insert('file.pdf')

def test_list_length(files_list):
    files_list.insert('file1.pdf')
    files_list.insert('file2.pdf')
    assert files_list.list_length() == 2

def test_print_items(files_list): 
    test_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']
    for file in test_files:
        files_list.insert(file)
    assert files_list.print_items() == ['file3.pdf', 'file2.pdf', 'file1.pdf']
