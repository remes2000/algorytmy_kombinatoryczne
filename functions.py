import math

def binom(n, k):
    return math.comb(n,k)

def rank(input_set, n):
    result = 0
    k = len(input_set)
    for i in range(0, k):
        result += binom(n, i)
    result += k_subset_lex_rank(input_set, n)
    return result

def k_subset_lex_rank(input_set, n):
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
    return k_subset_lex_unrank(rank_value, n, k)

def k_subset_lex_unrank(rank_value, n, k):
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

def succ(input_set, n):
    t = [0] + input_set
    max_value = n
    for i in reversed(range(1, len(input_set)+1)):
        if t[i]+1 > t[i-1] and t[i]+1 <= max_value:
            t[i] += 1
            for j in range(i+1, len(input_set)+1):
                t[j] = t[j-1] + 1
            return t[1:] 
        max_value = t[i]-1
    if len(t) > n: # no successor
        return []
    return [*range(1, len(input_set)+2)]
    
def pred(input_set, n):
    t = [0] + input_set
    for i in reversed(range(1, len(input_set)+1)):
        if t[i]-1 > t[i-1] and t[i]-1 > 0:
            t[i] = t[i] - 1
            return t[1:i+1] + [*range(n - (len(input_set) - i - 1), n+1)]
    if len(input_set) - 1 < 0: # no predecessor
        return []
    return [*range(n - (len(input_set) - 2), n+1)]

def print_set(input_set, label=''):
    print(label, end='')
    for element in input_set:
        print(element, end=' ')
    print()