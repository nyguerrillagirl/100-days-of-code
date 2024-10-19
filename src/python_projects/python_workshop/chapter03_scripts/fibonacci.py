def fibonacci_iterative(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    if n == 2:
        return 1

    # We start the algorithm here
    pre_1 = 1
    pre_2 = 1
    current_index = 2
    while current_index < n:
        current_index += 1
        temp = pre_2
        pre_2 = pre_1 + pre_2
        pre_1 = temp

    print(pre_2)





