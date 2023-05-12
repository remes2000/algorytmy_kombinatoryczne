from functions import *

def test(name, value, expected):
    has_passed = expected == value
    print('✓' if has_passed else '𐄂', end=' ')
    print(name + f' should return {expected}', end=' ')
    print('passed' if has_passed else f'failed, returned {value}')

# rank
print('--- rank ---')
test('rank([], 1)', rank([], 1), 0)
test('rank([4], 5)', rank([4], 5), 4)
test('rank([2, 3, 5], 5)', rank([2, 3, 5], 5), 23)
test('rank([1, 2, 3, 4], 5)', rank([1, 2, 3, 4], 5), 26)

# unrank
print('\n--- unrank ---')
test('unrank(0, 1)', str(unrank(0, 1)), '[]')
test('unrank(5, 5)', str(unrank(5, 5)), '[5]')
test('unrank(23, 5)', str(unrank(23, 5)), '[2, 3, 5]')
test('unrank(26, 5)', str(unrank(26, 5)), '[1, 2, 3, 4]')

# succ
print('\n--- succ ---')
test('succ([], 1)', str(succ([], 1)), '[1]')
test('succ([4], 5)', str(succ([4], 5)), '[5]')
test('succ([5], 5)', str(succ([5], 5)), '[1, 2]')
test('succ([2, 3, 4], 5)', str(succ([2, 3, 4], 5)), '[2, 3, 5]')
test('succ([1, 4, 5], 5)', str(succ([1, 4, 5], 5)), '[2, 3, 4]')
test('succ([1, 2, 3, 4, 5], 5) (!) no succesor', str(succ([1, 2, 3, 4, 5], 5)), '[]')

# pred
print('\n--- pred ---')
test('pred([1], 1)', str(pred([1], 1)), '[]')
test('pred([4], 5)', str(pred([4], 5)), '[3]')
test('pred([1, 2], 5)', str(pred([1, 2], 5)), '[5]')
test('pred([1, 2, 3], 5)', str(pred([1, 2, 3], 5)), '[4, 5]')
test('pred([3, 4, 5], 5)', str(pred([3, 4, 5], 5)), '[2, 4, 5]')
test('pred([1, 3, 4, 5], 8)', str(pred([1, 3, 4, 5], 8)), '[1, 2, 7, 8]')
test('pred([], 1) (!) no predecessor', str(pred([], 1)), '[]')