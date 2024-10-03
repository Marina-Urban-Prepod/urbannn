# import web12
#
# def test_add():
#     if web11.add(1,3) == 4:
#         print('функция add работает исправно')
#     else:
#         print('функция add ломается')
#
#
# test_add()


# import random
# import unittest
# import web11
#
# class CalcTest(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(web11.add(1,2), 3)
#
#     def test_sub(self):
#         self.assertEqual(web11.sub(10, 7), 4)
#
#
# if __name__ == '__main__':
#     unittest.main()

import unittest
import web12

class CalcTest(unittest.TestCase):
    def setUp(self):
        print('setup')

    @classmethod
    def setUpClass(cls):
        print('MegaSetup')
    def test_add(self):
        self.assertEqual(web12.add(1,2), 3)

    def test_sub(self):
        self.assertEqual(web12.sub(10, 7), 3)

class NewCalcTest(unittest.TestCase):
    @unittest.skip('не нравится')
    def test_mul(self):
        self.assertEqual(web12.mul(1,2), 2)

    @unittest.skipIf(random.randint(0,1), 'не повезло')
    def test_div(self):
        self.assertEqual(web12.div(10, 5), 2)


if __name__ == '__main__':
    unittest.main()
