import pytest
@pytest.fixture()
def tester():
    Username ="admin"
    password="admin"
    return [Username,password]
def testing_1(tester):
    Username=""
    assert tester[0]==Username
def testing_2(tester):
    Username="admin"
    assert tester[0]==Username
def testing_3(tester):
    password='admin'
    assert tester[1]==password
def testing_4(tester):
    password='asdfgh'
    assert tester[1]==password
