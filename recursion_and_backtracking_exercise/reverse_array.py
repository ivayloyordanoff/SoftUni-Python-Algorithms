def reverse_array(left_index, array):
    if left_index == len(array) // 2:
        return
    right_index = len(array) - 1 - left_index
    array[left_index], array[right_index] = array[right_index], array[left_index]
    reverse_array(left_index + 1, array)


array = input().split()

reverse_array(0, array)

print(' '.join(array))
