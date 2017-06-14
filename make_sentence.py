sentence_arr = []

while 0==0:
	print('Enter a word (. ! or ? to end): ')
	x = raw_input()
	if x == '.' or x == '!' or x == '?':
		sentence_arr.append(x)
		break

	sentence_arr.append(x)

sentence = ''
for word in sentence_arr:
	sentence = sentence + word
	if word != sentence_arr[-1] and word != sentence_arr[-2]:
		sentence = sentence + ' '

print(sentence)