import pytest

@pytest.fixture
def fixt(request):
    print('\nBegin in fixt')
    print(f'Call from {request.function.__name__}')
    #выполнили setup
    yield
    #возвращаемся обратно в фикстуру
    print('\nRolling back in fixt')

