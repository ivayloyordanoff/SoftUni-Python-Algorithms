def nested_loops(idx, array):
    if idx >= n:
        print(' '.join(str(x) for x in array))
        return
    for num in range(1, n + 1):
        array[idx] = num
        nested_loops(idx + 1, array)


n = int(input())
array = [None] * n

nested_loops(0, array)
