t9_dict = {'a': '2', 'b': '22', 'c': '222', 'd': '3', 'e': '33', 'f': '333',
			'g': '4', 'h': '44', 'i': '444', 'j': '5', 'k': '55', 'l': '555',
			'm': '6', 'n': '66', 'o': '666', 'p': '7', 'q': '77', 'r': '777',
			's': '7777', 't': '8', 'u': '88', 'v': '888', 'w': '9', 'x': '99',
			'y': '999', 'z': '9999'}
 

def t9_spelling(message):
	t9_message, prev = '', ' '
	for char in message:
		if char == ' ':
			t9_message += '0'
			prev = '0'
		elif prev in t9_dict[char]:
			t9_message += (' ' + t9_dict[char])
			prev = t9_dict[char][0]
		else:
			t9_message += (t9_dict[char])
			prev = t9_dict[char][0]
	return t9_message

cases = int(input())

file = open("output.txt", "w")

for case in range(0, cases):
	file.write(t9_spelling(input()))
	
file.close()