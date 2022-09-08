from .XOR import XOR
from .AND import AND

def HalfAdder(a, b):
    return [ XOR(a, b), AND(a, b) ]

def testHalfAdder():
    print(f"0 0: {HalfAdder(0, 0)}")
    print(f"0 1: {HalfAdder(0, 1)}")
    print(f"1 0: {HalfAdder(1, 0)}")
    print(f"1 1: {HalfAdder(1, 1)}")
    assert HalfAdder(0, 0) == [ 0, 0 ]
    assert HalfAdder(0, 1) == [ 1, 0 ]
    assert HalfAdder(1, 0) == [ 1, 0 ]
    assert HalfAdder(1, 1) == [ 0, 1 ]