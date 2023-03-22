from functions import *

n = int(input('n='))
input_set = sorted(list(map(lambda e: int(e), input('set=').split(' '))))
print(f'Provided set: {input_set}')
rank_value = rank(input_set, n)
print(f'Rank value: {rank_value}')