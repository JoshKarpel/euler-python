breaks = {200: {200: -1, 100: 2},
          100: {100: -1, 50: 2},
          50: {50: -1, 20: 2, 10: 1},
          20: {20: -1, 10: 2},
          10: {10: -1, 5: 2},
          5: {5: -1, 2: 2, 1: 1},
          2: {2: -1, 1: 2}}


def dict_add(dict_1, dict_2):
    # print('d1', dict_1)
    # print('d2', dict_2)
    return {k: dict_1[k] + dict_2.get(k, 0) for k in dict_1}


def solve(start):
    count = 1

    print(start)

    def break_coins(coins):
        nonlocal count
        print(count)

        breakable_coins = (k for k, v in coins.items() if v > 0 and k != 1)

        for coin in breakable_coins:
            count += 1

            # print(breaks[coin])
            # print(coins[50])
            # print(breaks[coin][50])
            new_coins = dict_add(coins, breaks[coin])
            # print(new_coins)

            break_coins(new_coins)

    break_coins(start)

    print(count)


if __name__ == '__main__':
    start = {200: 0,
             100: 0,
             50: 0,
             20: 2,
             10: 0,
             5: 0,
             2: 0,
             1: 0}

    solve(start)
