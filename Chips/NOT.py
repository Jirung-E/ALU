from .NAND import NAND

def NOT(a):
    return NAND(a, 1)

def testNOT():
    print(f"0 : {NOT(0)}")
    print(f"1 : {NOT(1)}")
    assert NOT(0) == 1
    assert NOT(1) == 0