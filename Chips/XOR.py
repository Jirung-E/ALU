from .NAND import NAND

def XOR(a, b):
    x = NAND(a, b)
    return NAND(NAND(a, x), NAND(x, b))

def testXOR():
    print(f"0 0 : {XOR(0, 0)}")
    print(f"0 1 : {XOR(0, 1)}")
    print(f"1 0 : {XOR(1, 0)}")
    print(f"1 1 : {XOR(1, 1)}")
    assert XOR(0, 0) == 0
    assert XOR(0, 1) == 1
    assert XOR(1, 0) == 1
    assert XOR(1, 1) == 0