from .NAND import NAND

def OR(a, b):
    return NAND(NAND(a, a), NAND(b, b))

def testOR():
    print(f"0 0 : {OR(0, 0)}")
    print(f"0 1 : {OR(0, 1)}")
    print(f"1 0 : {OR(1, 0)}")
    print(f"1 1 : {OR(1, 1)}")
    assert OR(0, 0) == 0
    assert OR(0, 1) == 1
    assert OR(1, 0) == 1
    assert OR(1, 1) == 1