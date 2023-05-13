"""
Tests are a key part of software development. 

The tests provided below are not property-based tests, and their coverage is incomplete.
Thus, passing them does not mean that your code is fully correct.
This test file is a starting point for you to write your own tests.
Pay attention to edge cases (e.g. zero, empty list, empty string, etc).
Your mark will also depend on how you have coded your answers.

Any additional test code you produce will not be marked directly, but it may help give you credit for demonstrating understanding, so it should be included in your fork as part of this test_cw.py file or in a separate file.

To run these tests, type `pytest test_cw.py` within this directory.
"""

import importlib
import py

from pytest import fail  
py_cw = importlib.import_module("py_cw")


## Q1

def test_q1a():
	s = py_cw.cadd((1, 0), (0, 1))
	p = py_cw.cmult((3, 2), (9, 6))
	assert s == (1, 1) and p == (15, 36)


def test_q1b():
	assert py_cw.tocomplex(1, 2) == (1 + 2j) and py_cw.fromcomplex(1 + 1j) == (1, 1)


## Q2

def test_q2a():
	assert py_cw.seqandi([True, False, True, False], [True, True, False, False]) == [True, False, False, False] and py_cw.seqxori([True, False, True, False], [True, True, False, False]) == [False, True, True, False]

def test_q2b():
	assert py_cw.seqandr([True, False, True, False], [True, True, False, False]) == [True, False, False, False] and py_cw.seqxorr([True, False, True, False], [True, True, False, False]) == [False, True, True, False]


def test_q2c():
	assert py_cw.seqandlc([True, False, True, False], [True, True, False, False]) == [True, False, False, False] and py_cw.seqxorlc([True, False, True, False], [True, True, False, False]) == [False, True, True, False]


## Q3 


## Q4 

def test_q4_supermap():
    assert py_cw.supermap( lambda a : 2*a, [5, [5]]) == [10, [10]]


## Q5 

def test_q5_fenc():
	assert py_cw.fenc(4)==[[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]]


def test_q5_fdec():
	assert py_cw.fdec([[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]])==4

## Q6 

def test_q6_love():
   x = py_cw.love()
   assert next(x) == "I love you"
   assert next(x) == "You love that I love you"
   assert next(x) == "I love that you love that I love you"

## Q7

def test_q7_removeall_oo():
    assert py_cw.removeall_oo(0, [0, 0, 1, 1, 0]) == [1, 1]

def test_q7_removeall_ft():
    assert py_cw.removeall_ft(0, [0, 0, 1, 1, 0]) == [1, 1]

def test_q7_removeall_rd():
    assert py_cw.removeall_rd(0, [0, 0, 1, 1, 0]) == [1, 1]

def test_q7_removeall_rd2():
        assert py_cw.removeall_rd(2, [0, 0, 1, 2, 1, 0, 2]) == [0,0,1,1,0]

## Q8

def test_q8_sudan():
    assert py_cw.sudan(0,0,0) == 0 and py_cw.sudan(2,2,1) == 27

## Q9
    #Essay Question
## Q10
    #Essay Question
## Q11
def test_q11_iint():
    assert py_cw.iint(12) == [2,1]
    assert py_cw.iint(14) == [4,1]
    assert py_cw.iint(24) == [4,2]
    assert py_cw.iint(27) == [7,2]

def test_q11_pint():
    assert py_cw.pint([2,1]) == 12
    assert py_cw.pint([4,2]) == 24
    assert py_cw.pint([9,2]) == 29
    assert py_cw.pint([4,5]) == 54

def test_q11_iadd():
    assert py_cw.iadd([5],[5])==[0,1]
    assert py_cw.iadd([5],[14])==[9,1]
    assert py_cw.iadd([9],[9])==[8,1]
    assert py_cw.iadd([6],[6])==[2,1]

def test_q11_imult():
    assert py_cw.imult([],[5])==[]
    assert py_cw.imult([4],[5])==[0,2]
    assert py_cw.imult([3],[6])==[8,1]
    assert py_cw.imult([9],[7])==[3,6]

def test_q11_ipow():
    assert py_cw.ipow([5],[2])==[5,2]
    assert py_cw.ipow([2],[6])==[4,6]
    assert py_cw.ipow([4],[2])==[6,1]
    assert py_cw.ipow([7],[2])==[9,4]
    
# At this level you should be providing your own tests

## Q12
def test_q12_abstractSize():
     assert py_cw.abstractSize([9,8,7,[6,5,4],3,2,1]) == 11
    
def test_q12_compressSize():
     assert py_cw.compressSize([9,8,7,[6,5,4],3,2,1]) == [9,8,7,6,5,4,3,2,1]

## Q13
def test_q13_equals23():
    assert py_cw.equals23(23) == True
