import  pytest

@pytest.fixture
def data_2():
    print('tests')
    return 2

@pytest.fixture
def wide_use():
    print('\nWide use')