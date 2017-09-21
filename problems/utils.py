import functools


class Memoize:
    """
    Decorator. Caches a function's return value each time it is called.

    If called later with the same arguments, the cached value is returned (not reevaluated).
    """

    def __init__(self, func):
        self.func = func
        self.memo = {}

    def __call__(self, *args):
        """Memoized call to the wrapped function."""
        if args in self.memo:
            out = self.memo[args]
        else:
            value = self.func(*args)
            self.memo[args] = value
            out = value

        return out

    def __get__(self, obj, objtype):
        # support instance methods
        return functools.partial(self.__call__, obj)
