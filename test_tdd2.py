
import unittest
import tdd2
import datetime

class TestTdd2(unittest.TestCase):

	def test_add_five(self):
		# a = tdd2.add_five(3)
		# print('from test : ', a)
		self.assertEqual(8,tdd2.add_five(3))

	def test_my_max(self):
		self.assertEqual(5,tdd2.my_max([1,2,3,4,5]))

	def test_my_min(self):
		self.assertEqual(1,tdd2.my_min([1,2,3,4,5]))

	def test_has_string(self):
		self.assertEqual(["Mary had"],
						tdd2.has_string(
							["Mary had",
							 "a little lamb",
							 "little lamb",
							 "Whose fleece",
							],"Mary had"))

	def test_to_date(self):
		dt = tdd2.to_date("2010-08-02")
		self.assertIsInstance(dt, datetime.date)
		self.assertEqual(2010,dt.year)
		self.assertEqual(8,dt.month)
		self.assertEqual(2,dt.day)


	def test_date_diff(self):
		self.assertEqual(1, tdd2.date_diff("2018-09-02", "2018-09-01"))

	def test_contains(self):
		self.assertTrue(tdd2.contains(['a','b','d'],"a"))

	def test_add_contents(self):
		self.assertEqual(6, tdd2.add_contents([1,2,3]))


	def test_lookup(self):
		self.assertEqual('one mine', tdd2.lookup({1:'one', 2:'two', 3:'three'} , 1))


	def test_lookup(self):
		self.assertEqual('one mine', tdd2.lookup({1:'one', 2:'two', 3:'three'} , 1))
		self.assertEqual('one mine', tdd2.lookup({1:'one', 2:'two', 3:'three'} , 2))