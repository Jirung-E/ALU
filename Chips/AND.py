from .NAND import NAND

def AND(a, b):
    x = NAND(a, b)
    return NAND(x, x)

def testAND():
    print(f"0 0 : {AND(0, 0)}")
    print(f"0 1 : {AND(0, 1)}")
    print(f"1 0 : {AND(1, 0)}")
    print(f"1 1 : {AND(1, 1)}")
    assert AND(0, 0) == 0
    assert AND(0, 1) == 0
    assert AND(1, 0) == 0
    assert AND(1, 1) == 1