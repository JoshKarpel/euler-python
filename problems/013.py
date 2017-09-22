def solve():
    with open('problems/013_numbers.txt', mode = 'r') as f:
        numbers = [int(x) for x in f]

    return str(sum(numbers))[:10]
