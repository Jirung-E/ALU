from .AND import AND
from .NOT import NOT

def DEMUX(a, s):
    return [ AND(a, NOT(s)), AND(a, s) ]

def testDEMUX():
    print(f"0 0: {DEMUX(0, 0)}")
    print(f"0 1: {DEMUX(0, 1)}")
    print(f"1 0: {DEMUX(1, 0)}")
    print(f"1 1: {DEMUX(1, 1)}")
    assert DEMUX(0, 0) == [ 0, 0 ]
    assert DEMUX(0, 1) == [ 0, 0 ]
    assert DEMUX(1, 0) == [ 1, 0 ]
    assert DEMUX(1, 1) == [ 0, 1 ]