def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        # We will excecute the loop as long as first value is not greater than last value
        midpoint = (first + last)//2
        # Getting midpoint by summing first and last then dividing by two
        # The double forward slash (//) is a floor division which will not only divide but also round off incase the midpoint is a decimal

        if list[midpoint] == target:
            # If midpoint is equal to the target value then we return the midpoint as the target value
            return midpoint
        elif list[midpoint] < target:
            # If target value is greater than midpoint the we don't need values below midpoint
            # The value after midpoint now becomes our first value
            first = midpoint + 1
        else:
            # If target value is less than midpoint the we don't need values above midpoint
            # The value before midpoint now becomes our last value
            last = midpoint - 1

    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not fount in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)