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

        def test_is_anagram(self):
            s1 = "delira"
            s2 = "lidera"

            result = basics.is_anagram(s1,s2)

            self.assertEqual(result, True)

        def test_is_anagrams_return_false_if_not_anagrams(self):
            s1 = "deliran"
            s2 = "lideras"

            result = basics.is_anagram(s1,s2)

            self.assertEqual(result, False)

        def test_min_max_from_list_of_integers(self):
            listOfIntegers = [1,2,3]

            result = basics.get_min_max_from_list_of_integers(listOfIntegers)

            self.assertEqual(result, [1,3])

        def test_min_max_from_list_of_integers_unsorted_list(self):
            listOfIntegers = [7,3,4,8,5,2,1]

            result = basics.get_min_max_from_list_of_integers(listOfIntegers)

            self.assertEqual(result, [1,8])

        def test_remove_all_duplicates_from_list(self):
            listOfIntegers = [1,2,3,1]

            result = basics.remove_all_duplicates_from_list(listOfIntegers)

            self.assertEqual(result, [1,2,3])

        def test_remove_all_duplicates_from_list_only_1_different(self):
            listOfIntegers = [1,1,1]

            result = basics.remove_all_duplicates_from_list(listOfIntegers)

            self.assertEqual(result, [1])


        def test_remove_all_duplicates_from_list_all_items_in_position(self):
            listOfIntegers = [1,2,5,2,4,5,5,4,4,4,4,4,1]

            result = basics.remove_all_duplicates_from_list(listOfIntegers)

            self.assertEqual(result, [1,2,5,4])

        def test_remove_all_duplicates_from_list_with_different_types(self):
            listOfIntegers = [1,2,"python",2,3,6,4,"hi","python",3]

            result = basics.remove_all_duplicates_from_list(listOfIntegers)

            self.assertEqual(result, [1,2,"python",3,6,4,"hi"])

        def test_reverse_string_with_recursion(self):
            s1 = 'python'

            result = basics.reverse_string_with_recursion(s1)

            self.assertEqual(result, 'nohtyp')

        def test_find_pairs_of_integers(self):
            listOfIntegers = [1,2,3]

            result = basics.find_pairs(listOfIntegers,  3)

            self.assertEqual(result, [[1,2]])

        def test_find_pairs_of_integers_multiple_solutions(self):
            listOfIntegers = [1,2,2,3]

            result = basics.find_pairs(listOfIntegers,  4)

            self.assertEqual(result, [[1,3],[2,2]])

        def test_compute_fibonacci_0(self):
            result = basics.compute_fibonacci(0)

            self.assertEqual(result, [])

        def test_compute_fibonacci_1(self):
            result = basics.compute_fibonacci(1)

            self.assertEqual(result, [0])

        def test_compute_fibonacci_2(self):
            result = basics.compute_fibonacci(2)

            self.assertEqual(result, [0,1])

        def test_compute_fibonacci_3(self):
            

            result = basics.compute_fibonacci(3)

            self.assertEqual(result, [0,1,1])

        def test_compute_fibonacci_7(self):
            

            result = basics.compute_fibonacci(7)

            self.assertEqual(result, [0,1,1,2,3,5,8])




        # def test_example(self):
        #     self.assertEqual('resultado_obtenido','resultado_esperado')



if __name__ == '__main__':

    unittest.main()
