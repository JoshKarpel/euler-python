def solve():
    champernowne = [str(i) for i in range(1, 1000000)]
    champernowne = ''.join(champernowne)

    return int(champernowne[0]) * int(champernowne[9]) * int(champernowne[99]) * int(champernowne[999]) * int(champernowne[9999]) * int(champernowne[99999]) * int(champernowne[999999])


if __name__ == '__main__':
    print(solve())
