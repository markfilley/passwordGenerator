state = (1 << 127) | 1
for i in range(10000):
    print(state &1, end='')
    newbit = (state ^ (state >> 1) ^ (state >> 2) ^ (state >> 7)) & 1
    state = (state >> 1) | (newbit << 127)
