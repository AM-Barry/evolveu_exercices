
import unittest
import function

class TestFunction(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(12,function.add_numbers(6,6))


    def test_payment(self):
    	self.assertEqual(320, function.payment(8,40))

    def test_div_numbers(self):
    	self.assertEqual(5, function.div_numbers(10,2))

    def test_count_occur(self):
    	self.assertEqual({1:2, 2:3, 3:4}, function.count_occur([1,1,2,2,2,3,3,3,3]))

    def test_lookup_prov(self):
    	self.assertEqual('ON',function.lookup_prov({'MB':'Manitoba', 'AB': 'Alberta', 'ON': 'Ontario'}, 'ON'))