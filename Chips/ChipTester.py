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
        print("Success.")
    except:
        print("Failed.")
    print()