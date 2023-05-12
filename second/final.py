# Funkcja rank i unrank dla permutacji w porządku minimalnych zmian
# Michał Nieruchalski 462084

def rank(n, perm):
    if n == 1:
        return 0
    perm_without_n = list(filter(lambda v: v != n, perm))
    k = perm.index(n) + 1
    prev_perm_rank = rank(n - 1, perm_without_n)
    if prev_perm_rank % 2 == 0:
        # od prawej
        return n * prev_perm_rank + n - k
    # od lewej
    return n * prev_perm_rank + k - 1

def unrank(rank_number, n):
    if n == 1:
        return [1]
    
    blocks_above = rank_number // n
    prev_perm = unrank(blocks_above, n-1)

    n_index = rank_number - n * blocks_above
    
    if blocks_above % 2 == 0:
        # od prawej:
        prev_perm.insert(n - 1 - n_index, n)
    else:
        # od lewej:
        prev_perm.insert(n_index, n)

    return prev_perm


# --- === TESTS === ---
print(rank(4, [3, 4, 2, 1])) # 13
print(rank(2, [1, 2])) # 0
print(rank(2, [2, 1])) # 1
print(rank(3, [3, 1, 2])) # 2

print(unrank(13, 4)) # [3, 4, 2, 1]
print(unrank(0, 2)) # [1, 2]
print(unrank(1, 2)) # [2, 1]
print(unrank(2, 3)) # [3, 1, 2] 