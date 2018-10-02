def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


def permutations(n, k):
    return factorial(n) // factorial(n - k)


def combinations(n, k):
    return permutations(n, k) // factorial(k)
