def NAND(a, b):
    if a == 1 and b == 1:
        return 0
    else:
        return 1

def testNAND():
    print(f"0 0 : {NAND(0, 0)}")
    print(f"0 1 : {NAND(0, 1)}")
    print(f"1 0 : {NAND(1, 0)}")
    print(f"1 1 : {NAND(1, 1)}")
    assert NAND(0, 0) == 1
    assert NAND(0, 1) == 1
    assert NAND(1, 0) == 1
    assert NAND(1, 1) == 0