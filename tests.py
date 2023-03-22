from functions import *

def test(name, value, expected):
    print(name + f' should return {expected}', end=' ')
    print('passed' if expected == value else f'failed, returned {value}')

# rank
test('rank([1], 5)', rank([1], 5), 1)
test('rank([1,2,3,4], 4)', rank([1,2,3,4], 4), 15)
test('rank([1,2,4], 4)', rank([1,2,4], 4), 12)

# unrank
test('unrank(1, 5)', str(unrank(1, 5)), '[1]')
test('unrank(15, 4)', str(unrank(15, 4)), '[1, 2, 3, 4]')
test('unrank(12, 4)', str(unrank(12, 4)), '[1, 2, 4]')

# succ
test('succ([1], 5)', str(succ([1], 5)), '[2]')
test('succ([1, 2, 3], 5)', str(succ([1, 2, 3], 5)), '[1, 2, 4]')
test('succ([3, 4, 5], 5)', str(succ([3, 4, 5], 5)), '[1, 2, 3, 4]')

# pred
test('pred([2], 5)', str(pred([2], 5)), '[1]')
test('pred([1, 2, 4], 5)', str(pred([1, 2, 4], 5)), '[1, 2, 3]')
test('pred([1, 2, 3, 4], 5)', str(pred([1, 2, 3, 4], 5)), '[3, 4, 5]')