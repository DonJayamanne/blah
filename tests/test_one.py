# # # test_something.py
# # from pytest import mark


# # @mark.parametrize(
# #     "a, b",
# #     [
# #         ["""no new line""", "b"],
# #         [
# #             """new line
# #         """,
# #             "b",
# #         ],
# #         ["also fails\n", "b"],
# #     ],
# # )
# # def test_something(a, b):
# #     assert True


# # def xyz(one: str) -> float:
# #     return "1234"


# import unittest



# class TestSample(unittest.TestCase):
#     def test_this(self):
#         a = 4
#         b = 6
#         result = a + b
#         expected = 10
#         self.assertEqual(result, expected)
import unittest
import sys

x = '$\mu$'

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        print('Setting up class\n')

    def setUp(self):
        super(Test, self).setUp()
        print('Setting up method\n')

    def test(self):
        return
