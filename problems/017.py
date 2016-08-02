import time


start_time = time.clock()

ones_dictionary = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens_dictionary = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens_dictionary = {0: '', 1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
hundreds_dictionary = {1: 'onehundred', 2: 'twohundred', 3: 'threehundred', 4: 'fourhundred', 5: 'fivehundred', 6: 'sixhundred', 7: 'sevenhundred', 8: 'eighthundred', 9: 'ninehundred'}

end_time = time.clock()

# for i in range(1, 10):
# 	print(ones_dictionary[i])
#
# for i in range(10, 100):
# 	try:
# 		print(teens_dictionary[i])
# 	except KeyError:
# 		print(tens_dictionary[int(str(i)[0])] + ones_dictionary[int(str(i)[1])])

number_words = []

for i in range(1, 1001):
	str_i = str(i)
	if len(str_i) == 1:
		print(ones_dictionary[i])
		number_words += ones_dictionary[i]
	elif len(str_i) == 2:
		try:
			print(teens_dictionary[i])
			number_words += teens_dictionary[i]
		except KeyError:
			print(tens_dictionary[int(str_i[0])] + ones_dictionary[int(str_i[1])])
			number_words += tens_dictionary[int(str_i[0])] + ones_dictionary[int(str_i[1])]
	elif len(str_i) == 3:
		try:
			print(hundreds_dictionary[int(str_i[0])] + 'and' + teens_dictionary[int(str_i[1:])])
			number_words += hundreds_dictionary[int(str_i[0])] + 'and' + teens_dictionary[int(str_i[1:])]
		except KeyError:
			if i % 100 != 0:
				print(hundreds_dictionary[int(str_i[0])] + 'and' + tens_dictionary[int(str_i[1])] + ones_dictionary[int(str_i[2])])
				number_words += hundreds_dictionary[int(str_i[0])] + 'and' + tens_dictionary[int(str_i[1])] + ones_dictionary[int(str_i[2])]
			elif i % 100 == 0:
				print(hundreds_dictionary[int(str_i[0])])
				number_words += hundreds_dictionary[int(str_i[0])]
	elif len(str_i) == 4:
		print('onethousand')
		number_words += 'onethousand'

#print(number_words)
print(len(number_words))

print('Elapsed Time: ' + str(end_time - start_time))