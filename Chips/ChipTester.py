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
        print("Success.")
    except:
        print("Failed.")
    print()