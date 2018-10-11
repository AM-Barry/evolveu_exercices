
'''6. Describe what a test is: a python program for testing python code
How a test can “Test” or just “Execute” a function: using pytest 
   7.Describe what pytest does. What it looks for. Describe what files it looks
for and what methods it looks for:pytest  runs a code test, it looks for 
test_ files and method prefixed by test_  
   8. List the steps in creating functions / tests as 
comment in the py file
- create a stub function
- create the test file
- run a test that fail
- fixe the stub function
- run the test that pass

   9.List the 7 math operators python has: +,-,*,/,%,//,**
'''

import unittest
import t_logic

class TestLogic(unittest.TestCase):

	def test_test_dummy_tests(self):
		#self.assertEqual(0,0,0,0,0,0,0, t_logic.dummy_tests(2,2))
		t_logic.dummy_tests()

	def test_mod(self):
		self.assertEqual(2, t_logic.mod(4,2))

	def test_flo(self):
		self.assertEqual(4, t_logic.flo(8, 4))

	def test_expo(self):
		self.assertEqual(5, t_logic.expo(15, 5))

	def test_largest_num(self):
		self.assertEqual(9, t_logic.largest_num(7,8,9))
		self.assertEqual(5, t_logic.largest_num(2,3,5))
		self.assertEqual(15, t_logic.largest_num(12,8,15))
		self.assertEqual(20, t_logic.largest_num(20,8,11))

# Lookup the “range” statement: returns sequence of 
# numbers between the start integer and the stop one