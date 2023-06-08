def linear_search(list, target):
    # Return the index position of the target if found, else returns None
    # We loop through the list each time comparing i with with the target value
    for i in range(0, len(list)):
        # If i is equal to the target value then we return i as the target value
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not fount in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)