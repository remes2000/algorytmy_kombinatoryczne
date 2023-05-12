from functions import *

n = int(input('n='))
input_set = sorted(list(map(lambda e: int(e), input('set=').split(' '))))
print(f'Provided set: {input_set}')
rank_value = rank(input_set, n)
unranked_set = unrank(rank_value, n)
print(f'Rank value: {rank_value}')
print(f'Unranked set: {unranked_set}')
print(f'Succ: {succ(input_set, n)}')
print(f'Pred: {pred(input_set, n)}')
