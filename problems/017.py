ONES = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
TEENS = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
TENS = {0: '', 1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
HUNDREDS = {1: 'onehundred', 2: 'twohundred', 3: 'threehundred', 4: 'fourhundred', 5: 'fivehundred', 6: 'sixhundred', 7: 'sevenhundred', 8: 'eighthundred', 9: 'ninehundred'}


def solve():
    words = []

    for number_as_str in (str(i) for i in range(1, 1001)):
        print(number_as_str, len(number_as_str))
        # if len_i == 1:
        #     print(ONES[i])
        #     words += ONES[i]
        # elif len_i == 2:
        #     try:
        #         print(TEENS[i])
        #         words += TEENS[i]
        #     except KeyError:
        #         print(TENS[int(str_i[0])] + ONES[int(str_i[1])])
        #         words += TENS[int(str_i[0])] + ONES[int(str_i[1])]
        # elif len_i == 3:
        #     try:
        #         print(HUNDREDS[int(str_i[0])] + 'and' + TEENS[int(str_i[1:])])
        #         words += HUNDREDS[int(str_i[0])] + 'and' + TEENS[int(str_i[1:])]
        #     except KeyError:
        #         if i % 100 != 0:
        #             print(HUNDREDS[int(str_i[0])] + 'and' + TENS[int(str_i[1])] + ONES[int(str_i[2])])
        #             words += HUNDREDS[int(str_i[0])] + 'and' + TENS[int(str_i[1])] + ONES[int(str_i[2])]
        #         elif i % 100 == 0:
        #             print(HUNDREDS[int(str_i[0])])
        #             words += HUNDREDS[int(str_i[0])]
        # elif len_i == 4:
        #     print('onethousand')
        #     words += 'onethousand'

    return len(''.join(words))
