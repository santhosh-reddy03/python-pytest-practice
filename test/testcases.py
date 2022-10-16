
# from dev.sample_test import add2num, multiply, power

# import unittest


# def setUpModule():
#     print("started executing all tests")

# def tearDownModule():
#     print("finsihed all test cases execution")


# class Test2add(unittest.TestCase):
    
#     def setUp(self):
#         print("started to execute add test case")

#     def tearDown(self):
#         print("finished add case")


#     def test_add2pos(self):
#         self.assertEqual(add2num(1,2), 3)
    
#     def test_add1pos1neg(self):
#         self.assertEqual(add2num(-8,9), 1)

# class Multiply_test(unittest.TestCase):

#     def test_multiply2pos(self):
#         self.assertEqual(multiply(2,3), 6)
    
#     def test_multiply1pos1neg(self):
#         self.assertEqual(multiply(-1, 3), -3)


# class Power_test(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         print("test power funciton")
    
#     @classmethod
#     def tearDownClass(cls):
#         print("power case finished")

#     def test_pow(self):
#         self.assertEqual(power(2,4), 16)

#     def test_pow_neg(self):
#         self.assertEqual(power(-3, 3), -27)

# if __name__ == "__main__":
#     unittest.main()