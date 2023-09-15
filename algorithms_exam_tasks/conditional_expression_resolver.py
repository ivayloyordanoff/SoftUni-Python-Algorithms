def parse_expression(expression, idx):
    if expression[idx].isdigit():
        return expression[idx]

    if expression[idx] == 't':
        return parse_expression(expression, idx + 2)

    cursor = idx + 2
    counter = 0

    while True:
        symbol = expression[cursor]

        if symbol == '?':
            counter += 1
        elif symbol == ':':
            if counter == 0:
                return parse_expression(expression, cursor + 1)
            counter -= 1

        cursor += 1


expression = input().split()

print(parse_expression(expression, 0))
