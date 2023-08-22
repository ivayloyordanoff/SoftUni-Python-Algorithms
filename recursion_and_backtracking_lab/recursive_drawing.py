def print_figure(number):
    if number == 0:
        return
    print('*' * number)
    print_figure(number - 1)
    print('#' * number)


number = int(input())

print_figure(number)
