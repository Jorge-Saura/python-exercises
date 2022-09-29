
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




# Get all the permutations of a string
def get_permutations(string:str):
    permutations_list = []
    if len(string) == 1:
        return [string]
    else:
        for char in string:
            for a in get_permutations(string.replace(char, "", 1)):
                permutations_list.append(char + a)
    return permutations_list
     

# Multi fibonacci. Create a function that execute the fiboacci sequence for a sum of n elements
# If n = 3 and your input list is [1,1,2] your next element will be 4, and the next 7
# If n = 4 and your imput list is [1,1,1,3] your next element will be 6, and the next 11
# n must be greater or equal than the number of elements in the initial list 
def multi_fibonacci(iterarations:int, initialList: list, n:int):
    result = initialList
    for i in range(iterarations-n):
        result.append(sum(result[i:i+n]))
    return result


# Get factors of a given numbers
def get_factors(n:int) -> set:

    factors = set({1,n})
    max_factor = int((n**.5)+1)
    for i in range(2, max_factor):
        if n % i == 0:
            factors |= {i, n // i}
    print(factors)
    return factors
