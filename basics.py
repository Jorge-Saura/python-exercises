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

# Find max and min in unsorted list
def get_min_max_from_list_of_integers(listOfIntegers:list):
    return [min(listOfIntegers),max(listOfIntegers)]

# Remove all duplicates form list
def remove_all_duplicates_from_list(listOfItems:list):
    return [listOfItems[x] for x in list(range(len(listOfItems))) if listOfItems[x] not in listOfItems[:x]]

# Reverse string using recursion
def reverse_string_with_recursion(s1:str):
    if(len(s1)>1):
        return reverse_string_with_recursion(s1[1:]) + s1[0]
    else:
        return s1

# Find pairs of integers in a list so that their sum is equal to integer x
def find_pairs(listOfIntegers:list, x:int):
    
    return [ [listOfIntegers[n],x-listOfIntegers[n]] for n in list(range(len(listOfIntegers))) if x-listOfIntegers[n] in listOfIntegers[n+1:]]

# Compute the firs n fiboancci numbers

def compute_fibonacci(n:int):
    if n == 0:
        return []
    elif n  == 1:
        return [0]
    elif n == 2:
        return [0,1] 
    else:
        fibonacciSequence = compute_fibonacci(n-1)
        fibonacciSequence.append(fibonacciSequence[-1]+fibonacciSequence[-2])
        return fibonacciSequence

# Check if a string is a palindrome
def is_palindrome(s:str):
    return  all([True if s[x] == s[-x-1] else False for x in list(range(len(s)))])