import math

def binom(n, k):
    return math.comb(n,k)

def rank(input_set, n):
    result = 0
    k = len(input_set)
    for i in range(0, k):
        result += binom(n, i)
    result += kSubsetLexRank(input_set, n)
    return result

def kSubsetLexRank(input_set, n):
    result = 0
    k = len(input_set)
    t = [0] + input_set
    for i in range(1, k+1):
        if t[i-1] < t[i] - 1:
            for j in range(t[i-1] + 1, t[i]):
                result += binom(n-j, k-i)
    return result

def unrank(rank_value, n):
    k = 0
    binom_value = binom(n,k)
    while binom_value <= rank_value:
        rank_value -= binom_value
        k += 1
        binom_value = binom(n,k)
    return kSubsetLexUnrank(rank_value, n, k)

def kSubsetLexUnrank(rank_value, n, k):
    x = 1
    result = []
    for i in range(1, k+1):
        binom_value = binom(n-x, k-i)
        while binom_value <= rank_value:
            rank_value -= binom_value
            x += 1
            binom_value = binom(n-x, k-i)
        result.append(x)
        x += 1
    return result

# todo re-write this
def succ(input_set, n):
    return unrank(rank(input_set, n)+1, n)

# todo re-write thisss
def pred(input_set, n):
    return unrank(rank(input_set, n)-1, n)

def print_set(input_set, label=''):
    print(label, end='')
    for element in input_set:
        print(element, end=' ')
    print()