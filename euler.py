import click
import functools
import time
import importlib
import os
import sys
import collections
import re
import timeit as timeit_

ANSWERS = collections.defaultdict(lambda: object())
THIS_DIR = os.path.dirname(__file__)

answers_file = os.path.join(THIS_DIR, 'answers.txt')
with open(answers_file) as f:
    for line in f:
        problem, answer = line.strip().split(':')

        if answer == '':
            ANSWERS[problem] = object()
        else:
            ANSWERS[problem] = int(answer)

Answer = collections.namedtuple('answer_with_diags', ['answer', 'correct', 'elapsed_time'])


def solve_with_diagnostics(func):
    @functools.wraps(func)
    def solver():
        t_start = time.clock()
        answer = func()
        elapsed_time = time.clock() - t_start

        problem = func.__module__[-3:]
        try:
            correct = answer == ANSWERS[problem]
        except KeyError:
            correct = None

        return Answer(answer, correct, elapsed_time)

    return solver


CORRECT_TO_STR = {
    True: '✓',
    False: '✘',
    None: '?',
}
CORRECT_TO_COLOR = {
    True: 'green',
    False: 'red',
    None: 'yellow',
}


@click.group()
def cli():
    pass


ANSWER_WIDTH = 20


@cli.command()
@click.argument('problem')
def solve(problem):
    """Solve PROBLEM."""
    try:
        problem = problem.rjust(3, '0')
        mod = importlib.import_module(f'problems.{problem}')
    except (ImportError, ModuleNotFoundError):
        click.secho('SOLVER NOT FOUND',
                    fg = 'yellow')
        return 0

    solver = solve_with_diagnostics(mod.solve)
    answer = solver()

    click.secho(f'Answer: {answer.answer} {CORRECT_TO_STR[answer.correct]} │ Elapsed Time: {round(answer.elapsed_time, 6)} seconds',
                fg = CORRECT_TO_COLOR[answer.correct])

    return answer


def get_maximally_solved_problem_number():
    problem_regex = re.compile('[0-9]{3}.py')
    solvers = (int(f[:3]) for f in os.listdir(os.path.join(THIS_DIR, 'problems')) if problem_regex.search(f))
    return max(solvers)


@cli.command()
@click.option('--start', '-s', default = 1)
@click.option('--end', '-e', default = get_maximally_solved_problem_number())
# @click.option('--file', '-f', type = click.Path(dir_okay = False), default = '-')
def check(start, end):
    start = max(start, 1)

    header = f'  P  │ {"Answer".center(ANSWER_WIDTH)} │ C │ Elapsed Time'
    bar = ''.join('─' if char != '│' else '┼' for char in header)

    click.echo(header)
    click.echo(bar)

    for problem in range(start, end + 1):
        problem = str(problem).rjust(3, '0')
        try:
            mod = importlib.import_module(f'problems.{problem}')
            solver = solve_with_diagnostics(mod.solve)
            answer = solver()

            click.secho(f' {problem} │ {str(answer.answer).center(ANSWER_WIDTH)} │ {CORRECT_TO_STR[answer.correct]} │ {round(answer.elapsed_time, 6)} seconds',
                        fg = CORRECT_TO_COLOR[answer.correct])
        except (ImportError, ModuleNotFoundError):
            click.secho(f' {problem} │ {"SOLVER NOT FOUND".center(ANSWER_WIDTH)} │ ? │',
                        fg = 'yellow')
        except Exception as e:
            click.secho(f' {problem} │ {"EXCEPTION".center(ANSWER_WIDTH)} │ ? │',
                        fg = 'yellow')


@cli.command()
@click.argument('problem')
def timeit(problem):
    """Time the solver for PROBLEM."""
    problem = problem.rjust(3, '0')

    timer = timeit_.Timer('mod.solve()', setup = f'import importlib; mod = importlib.import_module(f"problems.{problem}")')
    loops, total_time = timer.autorange()
    click.echo(f'Time per Solve: {round(total_time / loops, 6)} seconds')


if __name__ == '__main__':
    cli()
