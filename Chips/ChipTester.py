from .NAND import *

def test(chip):
    print("Test " + chip + "...")
    try:
        testNAND()
        print("Success.")
    except:
        print("Failed.")