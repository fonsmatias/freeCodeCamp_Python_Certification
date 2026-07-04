# algorithm to perform binary search on a sorted list

def binary_search(search_list, value):
    path_to_target = [] # list to store the path taken to find the target value
    low = 0
    high = len(search_list) - 1
    
    while low <= high:
        mid = (low + high) // 2 # calculate the middle index
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle)
        
        if value == value_at_middle: # if the value is found at the middle index, return the path and index
            return path_to_target, f'Value found at index {mid}'
        elif value > value_at_middle: # if the value is greater than the middle value, search in the right half of the list
            low = mid + 1
        else: # if the value is less than the middle value, search in the left half of the list
            high = mid - 1
    
    return [], "Value not found"

# test cases
print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5, 9], 4))
print(binary_search([1, 3, 5, 9, 14, 22], 10))