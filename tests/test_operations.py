from src.maths_operations import add, subtract, multiply, divide

def test_add():
    assert add(5, 3) == 8   
    assert add(-1, 1) == 0
    assert add(2,3) == 5
    assert add(-5, 0) == -5
    assert add(-5, -5) == -10

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2
    assert subtract(2,3) == -1
    assert subtract(-5, 0) == -5
    assert subtract(-5, -5) == 0

def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(-1, 1) == -1
    assert multiply(2,3) == 6
    assert multiply(-5, 0) == 0
    assert multiply(-5, -5) == 25

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-4, 2) == -2
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    assert divide(-10, -2) == 5
    