from .FullAdder import FullAdder

def Adder8bit(bin1: str, bin2: str):
    binary: str
    for i in range(0, 8):
        binary = binary + str(FullAdder(int(bin1[i]), int(bin2[i])))
    return binary

def testAdder8bit():
    print(Adder8bit("10101101", "00100001"))
    assert Adder8bit("10101101", "00100001") == "11001110"