from functions import *

n = int(input('n='))
input_set = set(map(lambda e: int(e), input('set=').split(' ')))

rank_value = rank(input_set, n)
unranked_set = unrank(rank_value, n)
succ_set = succ(input_set, n)
pred_set = pred(input_set, n)

print('rank =', rank_value)
print_set('unrank = ', unranked_set)
print_set('succ = ', succ_set)
print_set('pred = ', pred_set)
