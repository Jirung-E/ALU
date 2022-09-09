from .Chips import *

def ALU_(in1, in2, selector):
    return MUX(AND(in1, in2), OR(in1, in2), selector)

def testALU_():
    print(f"0 0 0: {ALU_(0, 0, 0)}")
    print(f"0 0 1: {ALU_(0, 0, 1)}")
    print(f"0 1 0: {ALU_(0, 1, 0)}")
    print(f"0 1 1: {ALU_(0, 1, 1)}")
    print(f"1 0 0: {ALU_(1, 0, 0)}")
    print(f"1 0 1: {ALU_(1, 0, 1)}")
    print(f"1 1 0: {ALU_(1, 1, 0)}")
    print(f"1 1 1: {ALU_(1, 1, 1)}")
    assert ALU_(0, 0, 0) == AND(0, 0)
    assert ALU_(0, 0, 1) == OR(0, 0)
    assert ALU_(0, 1, 0) == AND(0, 1)
    assert ALU_(0, 1, 1) == OR(0, 1)
    assert ALU_(1, 0, 0) == AND(1, 0)
    assert ALU_(1, 0, 1) == OR(1, 0)
    assert ALU_(1, 1, 0) == AND(1, 1)
    assert ALU_(1, 1, 1) == OR(1, 1)