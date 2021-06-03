import pytest

@pytest.fixture
def class_fixt():
    print('\nclass_fixt started')

'''Чтобы не передавать фикстуру в каждом методе класса, можно указать
перед классом с помощью usefixtures'''


@pytest.mark.usefixtures('class_fixt')
class TestSomething:
    def test_3(self):
        print('test_3 started')

    def test_4(self):
        print('test_4 started')
