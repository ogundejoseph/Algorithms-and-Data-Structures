def recursive_binary_search(list, target):
    # If list is empty we return false
    if len(list) == 0:
        return False
    else:
        # We calculate the midpoint by by dividing the length of the list by two. If the midpoint is decimal then we round down.
        midpoint = (len(list))//2

        # If midpoint is equal to the target value then we return true
        if list[midpoint] == target:
            return True
        else:
            # If the target value is greater than the midpoint then we will create a new sub-list starting from the value after the midpoint to the end of the list
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                # If the target value is less than the midpoint then we will create a new sub-list starting from the beginning of the list to the midpoint
                return recursive_binary_search(list[:midpoint], target)
            
def verify(result):
    print("Target found:", result)

numbers = [1,2,3,4,5,6,7,8]

result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)