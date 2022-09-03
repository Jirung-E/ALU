from .Chips import *

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
        else:
            print("No such chip: " + chip)
            return
        print("Success.")
    except:
        print("Failed.")
    print()