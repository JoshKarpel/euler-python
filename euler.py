import argparse
import functools
import time
import importlib


def solve_and_print(func):
    @functools.wraps(func)
    def printer():
        answer = func()
        print(f'Answer: {answer}')

    return printer


def timed(func):
    @functools.wraps(func)
    def timed_func():
        t_start = time.clock()
        func()
        print(f'Elaped Wall Time: {round(time.clock() - t_start, 6)} seconds')

    return timed_func


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Run Project Euler solutions.')
    parser.add_argument('problem_number',
                        type = str,
                        help = 'the name of the job')
    parser.add_argument('--timed', '-t',
                        action = 'store_true')

    args = parser.parse_args()

    problem_name = args.problem_number.rjust(3, '0')
    mod = importlib.import_module(f'problems.{problem_name}')

    solver = solve_and_print(mod.solve)
    if args.timed:
        solver = timed(solver)

    solver()
