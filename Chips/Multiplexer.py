from .AND import AND
from .NOT import NOT
from .OR import OR

def MUX(a, b, s):
    return OR(AND(a, NOT(s)), AND(b, s))

def testMUX():
    print(f"0 0 0: {MUX(0, 0, 0)}")
    print(f"0 0 1: {MUX(0, 0, 1)}")
    print(f"0 1 0: {MUX(0, 1, 0)}")
    print(f"0 1 1: {MUX(0, 1, 1)}")
    print(f"1 0 0: {MUX(1, 0, 0)}")
    print(f"1 0 1: {MUX(1, 0, 1)}")
    print(f"1 1 0: {MUX(1, 1, 0)}")
    print(f"1 1 1: {MUX(1, 1, 1)}")
    assert MUX(0, 0, 0) == 0
    assert MUX(0, 0, 1) == 0
    assert MUX(0, 1, 0) == 0
    assert MUX(0, 1, 1) == 1
    assert MUX(1, 0, 0) == 1
    assert MUX(1, 0, 1) == 0
    assert MUX(1, 1, 0) == 1
    assert MUX(1, 1, 1) == 1