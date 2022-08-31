import unittest

import basics


class TestBasics(unittest.TestCase):

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

        def test_find_duplicate_number_in_integer_list_1_repeated_item(self):
            listOfIntegers = [1,2,3,4,1,6,19]

            result = basics.find_duplicate_number_in_integer_list(listOfIntegers)

            self.assertEqual(result,1)

        def test_find_duplicate_number_in_integer_list_more_than_1_item_repeated(self):
            listOfIntegers = [1,2,3,4,1,6,2,19]

            result = basics.find_duplicate_number_in_integer_list(listOfIntegers)

            self.assertEqual(result,1)

        def test_find_duplicate_number_in_integer_list_more_than_1_item_repeated_return_first_item_repeated(self):
            listOfIntegers = [1,2,3,2,1,6,2,19]

            result = basics.find_duplicate_number_in_integer_list(listOfIntegers)

            self.assertEqual(result,1)

        def test_intesect_2_list(self):
            list1 = [1,2,3,4]
            list2 = [4,5,6]

            result = basics.intersect(list1,list2)

            self.assertEqual(result,[4])

        def test_intesect_2_list_more_than_1_intem_intersected(self):
            list1 = [1,2,3,4,5]
            list2 = [4,5,6]

            result = basics.intersect(list1,list2)

            self.assertEqual(result,[4,5])


        def test_intesect_2_list_with_no_intersect(self):
            list1 = [1,2,3,4]
            list2 = [5,6]

            result = basics.intersect(list1,list2)

            self.assertEqual(result,[])

        # def test_example(self):
        #     self.assertEqual('resultado_obtenido','resultado_esperado')



if __name__ == '__main__':

    unittest.main()
