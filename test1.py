import unittest
import p1

class Test2(unittest.TestCase):
	def test_func(self):
		num=5.0
		res=p1.c
		self.assertEqual(res, num)

if __name__ == '__main__':
    unittest.main()
