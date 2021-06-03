import pytest

'''
Параметр scope определяет как часто будет вызываться setup и teardown
фикстуры
function - один раз для каждой тестовой функции, которая использует эту фикстуру
class - один раз для каждого тестового класса вне зависимости от количества методв в классе
module - один раз для модуля вне зависимости от того, сколько тестовых функций, методов
или других фикстур использует эту фикстуру
session - один раз на запуск тестов(сессию)
'''



@pytest.fixture(scope='function')
def func_scope():
    pass


@pytest.fixture(scope='module')
def mod_scope():
    pass


@pytest.fixture(scope='session')
def sess_scope():
    pass


@pytest.fixture(scope='class')
def class_scope():
    pass


def test_1(sess_scope,mod_scope,func_scope):
    pass

def test_2(sess_scope,mod_scope,func_scope):
    pass

@pytest.mark.usefixtures('class_scope')
class TestSomething:
    def test_3(self):
        pass

    def test_4(self):
        pass

