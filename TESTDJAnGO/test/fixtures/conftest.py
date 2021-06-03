import pytest

@pytest.fixture
def data_2():
    print('fixtures111')
    return 2