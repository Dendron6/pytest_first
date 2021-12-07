import pytest

cnt = 0 # just count of how many times it worked

# decorator that works like before each in JavaScript
@pytest.fixture(autouse=True)
# this function cleans out file before we use it in each test (beforeEach in JavaScript)
def clean_text_file():
    global cnt
    with open('test/prod_file_copy.txt', 'w'):
        pass
    print(cnt)
    cnt+=1