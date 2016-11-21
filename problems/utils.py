import functools
import datetime as dt


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


class Timer:
    """A context manager that times the code in the with block. Print the Timer after exiting the block to see the results."""

    __slots__ = ('time_start', 'time_end', 'time_elapsed')

    def __init__(self):
        self.time_start = None
        self.time_end = None
        self.time_elapsed = None

    def __enter__(self):
        self.time_start = dt.datetime.now()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.time_end = dt.datetime.now()
        self.time_elapsed = self.time_end - self.time_start

    def __str__(self):
        if self.time_end is None:
            return 'Timer started at {}, still running'.format(self.time_start)
        else:
            return 'Timer started at {}, ended at {}, elapsed time {}'.format(self.time_start, self.time_end, self.time_elapsed)
