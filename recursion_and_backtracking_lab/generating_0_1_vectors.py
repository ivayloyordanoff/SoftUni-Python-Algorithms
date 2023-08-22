def gen01(idx, vector):
    if idx >= len(vector):
        print(''.join([str(x) for x in vector]))
        return
    for number in range(0, 2):
        vector[idx] = number
        gen01(idx + 1, vector)


number = int(input())
vector = [0] * number

gen01(0, vector)
