# Check if list contain element x
def list_contains_element(listOfElements:list, x:int):
    return x in listOfElements

# Get missing number in [1..100]
def get_missing_number_1_100(listOfNumbers:list):

    return list(set(range(1,101)) - set(listOfNumbers))[0]

# Find first duplicate number in a list
def find_duplicate_number_in_integer_list(listOfIntegers:list):

    return next(x for x in listOfIntegers if listOfIntegers.count(x) >1)

# Intersect two lists
def intersect(list1:list, list2:list):

    return [x for x in set(list1) if x in list2]

# Check if two strings are anagrams
def is_anagram(s1:str, s2:str):
    return next((False for x in set(s1+s2) if s1.count(x) != s2.count(s2)), True)
