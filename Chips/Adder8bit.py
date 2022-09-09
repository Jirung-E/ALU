from .FullAdder import FullAdder

def Adder8bit(bin1: str, bin2: str):
    r_bin1 = bin1[::-1]
    r_bin2 = bin2[::-1]
    binary = ""
    carry_bit = 0
    for i in range(0, 8):
        res = FullAdder(int(r_bin1[i]), int(r_bin2[i]), carry_bit)
        carry_bit = res[1]
        binary = binary + str(res[0])
    #result = "".join(reversed(binary))
    result = binary[::-1]
    return result

def testAdder8bit():
    print(f'10101101 00100001 | {Adder8bit("10101101", "00100001")}')
    print(f'10101101 11111111 | {Adder8bit("10101101", "11111111")}')
    print(f'10101101 00000000 | {Adder8bit("10101101", "00000000")}')
    print(f'10101101 01111111 | {Adder8bit("10101101", "01111111")}')
    assert Adder8bit("10101101", "00100001") == "11001110"
    assert Adder8bit("10101101", "11111111") == "10101100"
    assert Adder8bit("10101101", "00000000") == "10101101"
    assert Adder8bit("10101101", "01111111") == "00101100"