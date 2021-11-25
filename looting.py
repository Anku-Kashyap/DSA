def check(a, n):
    incl = 0
    excl = 0

    for i in a:
        new_excl = max(incl,excl)
        incl = excl + i
        excl = new_excl

    return max(incl,excl)


a = [1, 2, 3]
n = len(a)
print(check(a, n))
