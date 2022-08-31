# Check if list contain element x
def list_contains_element(listOfElements:list, x:int):
    return x in listOfElements



# Get missing number in [1..100]
def get_missing_number_1_100(listOfNumbers:list):

    return list(set(range(1,101)) - set(listOfNumbers))[0]

# find first duplicate number in a list
def find_duplicate_number_in_integer_list(listOfIntegers:list):

    return next(x for x in listOfIntegers if listOfIntegers.count(x) >1)

