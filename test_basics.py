import unittest

import basics


class TestBasicsOpe(unittest.TestCase):

        def test_list_contains_element(self):
            listOfElements = [1,2,3,4,5,6,8,9]
            x = 3
            result = basics.list_contains_element(listOfElements,x)
            self.assertEqual(result,True)

        def test_list_not_contains_element(self):
            listOfElements = [1,2,3,4,5,6,8,9]
            x = 10
            result = basics.list_contains_element(listOfElements,x)
            self.assertEqual(result,False)


        def test_get_missing_number_10(self):
            listOfNumbers = list(range(1,101))
            listOfNumbers.remove(10)
            result = basics.get_missing_number_1_100(listOfNumbers)
            self.assertEqual(result,10)

        def test_get_missing_number_100_is_the_corner_case(self):
            listOfNumbers = list(range(1,101))
            listOfNumbers.remove(100)
            result = basics.get_missing_number_1_100(listOfNumbers)
            self.assertEqual(result,100)

        # def test_example(self):
        #     self.assertEqual('resultado_obtenido','resultado_esperado')



if __name__ == '__main__':

    unittest.main()