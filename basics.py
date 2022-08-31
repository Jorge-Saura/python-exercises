# Check if list contain element x
def list_contains_element(listOfElements:list, x:int):
    return x in listOfElements



# Get missing number in [1..100]
def get_missing_number_1_100(listOfNumbers:list):

    return list(set(range(1,101)) - set(listOfNumbers))[0]