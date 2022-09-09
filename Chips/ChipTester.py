from .Chips import *
from .ALU import *

def test(chip):
    print("Test " + chip + "...")
    try:
        if chip == "NAND":
            testNAND()
        elif chip == "NOT":
            testNOT()
        elif chip == "OR":
            testOR()
        elif chip == "AND":
            testAND()
        elif chip == "XOR":
            testXOR()
        elif chip == "MUX":
            testMUX()
        elif chip == "DEMUX":
            testDEMUX()
        elif chip == "HalfAdder":
            testHalfAdder()
        elif chip == "FullAdder":
            testFullAdder()
        elif chip == "Adder8bit":
            testAdder8bit()
        elif chip == "ALU_":
            testALU_()
        elif chip == "ALU":
            testALU()
        else:
            print("No such chip: " + chip)
            return
        print("Success.")
    except:
        print("Failed.")
    print()