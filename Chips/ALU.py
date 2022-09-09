from .Chips import *

def ALU_(in1, in2, selector):
    return MUX(AND(in1, in2), XOR(in1, in2), selector)

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
    assert ALU_(0, 0, 1) == XOR(0, 0)
    assert ALU_(0, 1, 0) == AND(0, 1)
    assert ALU_(0, 1, 1) == XOR(0, 1)
    assert ALU_(1, 0, 0) == AND(1, 0)
    assert ALU_(1, 0, 1) == XOR(1, 0)
    assert ALU_(1, 1, 0) == AND(1, 1)
    assert ALU_(1, 1, 1) == XOR(1, 1)

# def OR8bit(a: str, b: str):
#     return a

# def OR8bit4in(a: str, b: str, c: str, d: str):
#     return OR8bit(OR8bit(a, b), OR8bit(c, d))

def MUX8bit(a: str, b: str, selector):
    if selector == 0:                   # 임시로 if-else 사용
        return a
    else:
        return b

def MUX8bit4in(a: str, b: str, c: str, d: str, selector: str):
    return MUX8bit(MUX8bit(a, b, int(selector[1])), MUX8bit(c, d, int(selector[1])), int(selector[0]))

def INC8bit(in_: str):
    return Adder8bit(in_, "00000001")

def ALU(in1: str, in2: str, selector: str):
    return MUX8bit4in(Adder8bit(in1, in2), INC8bit(in1), "00000000", "11111111", selector)

def testALU():
    print(f"01101011 00010101 00: {ALU('01101011', '00010101', '00')}")
    print(f"01101011 00010101 01: {ALU('01101011', '00010101', '01')}")
    print(f"01101011 00010101 10: {ALU('01101011', '00010101', '10')}")
    print(f"01101011 00010101 11: {ALU('01101011', '00010101', '11')}")
    assert ALU('01101011', '00010101', '00') == Adder8bit('01101011', '00010101')
    assert ALU('01101011', '00010101', '01') == INC8bit('01101011')
    assert ALU('01101011', '00010101', '10') == "00000000"
    assert ALU('01101011', '00010101', '11') == "11111111"