import inspect

import WhoAmI_File
def test_WhoAmI():
    assert WhoAmI_File.WhoAmI() != ''

import BondPrice_File
def test_getBondPrice():
    assert round(BondPrice_File.getBondPrice(.03, 2000000, .04, 10,  1)) == 2170604
    assert round(BondPrice_File.getBondPrice(.03, 2000000, .04, 10,  2)) == 2171686
    assert 'for' not in inspect.getsource(BondPrice_File.getBondPrice)

import BondDuration_File
def test_getBondDuration():
    assert round(BondDuration_File.getBondDuration(.03, 2000000, .04, 10, 1), 2) == 8.51    
    assert round(BondDuration_File.getBondDuration(.03, 2000000, .04, 10, 2), 2) == 8.42
    assert 'for' not in inspect.getsource(BondDuration_File.getBondDuration)

import FizzBuzz_File
def test_FizzBuzz():
    x = FizzBuzz_File.FizzBuzz(40,45)
    assert x[0] == "buzz"
    assert (x[1]) == 41
    assert x[5] == "fizzbuzz"
    assert 'for' not in inspect.getsource(FizzBuzz_File.FizzBuzz)
