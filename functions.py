def rank(input_set, n):
    r = 0
    for i in range(1, n+1):
        if i in input_set:
            r += pow(2, i-1)
    return r

def unrank(rank_value, n):
    result_set = set()
    for i in range(1, n+1):
        if rank_value % 2 == 1:
            result_set.add(i)
        rank_value = rank_value // 2
    return result_set

def succ(input_set, n):
    rank_value = rank(input_set, n)
    return unrank(rank_value+1, n)

def pred(input_set, n):
    rank_value = rank(input_set, n)
    return unrank(rank_value-1, n)

def print_set(label, input_set):
    print(label, end='')
    for element in input_set:
        print(element, end=' ')
    print()