from functions import *

def test(name, value, expected):
    print(name + f' = {expected}', end=' ')
    print('passed' if expected == value else 'failed')

# rank tests
test('rank([1], 5)', rank(set([1]), 5), 1)