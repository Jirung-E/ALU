from .XOR import XOR
from .OR import OR
from .AND import AND

def FullAdder(a, b, c):
    x = XOR(a, b)
    return [ XOR(x, c), OR(AND(a, b), AND(x, c)) ]

def testFullAdder():
    print(f"0 0 0: {FullAdder(0, 0, 0)}")
    print(f"0 0 1: {FullAdder(0, 0, 1)}")
    print(f"0 1 0: {FullAdder(0, 1, 0)}")
    print(f"0 1 1: {FullAdder(0, 1, 1)}")
    print(f"1 0 0: {FullAdder(1, 0, 0)}")
    print(f"1 0 1: {FullAdder(1, 0, 1)}")
    print(f"1 1 0: {FullAdder(1, 1, 0)}")
    print(f"1 1 1: {FullAdder(1, 1, 1)}")
    assert FullAdder(0, 0, 0) == [ 0, 0 ]
    assert FullAdder(0, 0, 1) == [ 1, 0 ]
    assert FullAdder(0, 1, 0) == [ 1, 0 ]
    assert FullAdder(0, 1, 1) == [ 0, 1 ]
    assert FullAdder(1, 0, 0) == [ 1, 0 ]
    assert FullAdder(1, 0, 1) == [ 0, 1 ]
    assert FullAdder(1, 1, 0) == [ 0, 1 ]
    assert FullAdder(1, 1, 1) == [ 1, 1 ]