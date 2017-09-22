import functools


def memoize(func):
    """Memoize a function by storing a dictionary of {inputs: outputs}."""
    memo = {}

    @functools.wraps(func)
    def memoizer(*args):
        try:
            return memo[args]
        except KeyError:
            memo[args] = func(*args)
            return memo[args]

    return memoizer
