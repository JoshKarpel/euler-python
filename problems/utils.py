import functools


def hash_args_kwargs(*args, **kwargs):
    """Return the hash of a tuple containing the args and kwargs."""
    return hash(args + tuple(kwargs.items()))


def memoize(func):
    """Memoize a function by storing a dictionary of {inputs: outputs}."""
    memo = {}

    @functools.wraps(func)
    def memoizer(*args, **kwargs):
        key = hash_args_kwargs(*args, **kwargs)
        try:
            return memo[key]
        except KeyError:
            memo[key] = func(*args, **kwargs)
            return memo[key]

    return memoizer
