import xml.etree.ElementTree as ET

def print_help():
	print()
	print("---- HELP ----")
	print("Enter 't' to see the morse table.")
	print("Enter 'q' to quit.")
	print("type your text to convert to morse, " + \
		"or morse to convert to text.\n")

def get_ascii_dict():
	tree = ET.parse('morse.xml')
	morsexml = tree.getroot()
	morse_table = list(morsexml)

	ascii_dict = dict()

	for letter in morse_table:
		tag = letter.tag
		code = letter.text
		if tag.startswith('n'):
			tag = tag[1:]

		ascii_dict[tag] = code

	return ascii_dict


def get_morse_dict(ascii_dict):
	morse_dict = dict()

	for ascii_letter, morse_code in ascii_dict.items():
		morse_dict[morse_code] = ascii_letter

	return morse_dict

def print_morse_table(morse_dict):
	for morse_code, ascii_letter in morse_dict.items():
		print(ascii_letter, morse_code)

def get_list_from_input(inpt):
	return " / ".join(inpt.split('/')).split()

def morse2text(morse_dict, morse_input):
	res = ''
	for code in morse_input:
		if code == "/":
			res += ' '
		else:
			res += morse_dict[code]
	return res

def text2morse(ascii_dict, text_input):
	res = ''
	for char in text_input:
		if char == ' ':
			res += '/ '
		else:
			res += ascii_dict[char.upper()]
			res += " "

	return res.strip()

def is_text(string):
	return ''.join(string.split()).isalnum()

def is_morse(string):
	for char in string:
		if not char in ".- /":
			return False
	return True

def main(ascii_dict, morse_dict):
	print("Welcome to the Morse-Translator.")
	print("type 'help' for help.\n")
	while True:
		inpt = input("Input: ")

		if inpt == "q":
			break

		elif inpt == "help":
			print_help()

		elif inpt == "t":
			print_morse_table(morse_dict)
		
		elif is_text(inpt):
			print(text2morse(ascii_dict, inpt))
		
		elif is_morse(inpt):
			morse_input = get_list_from_input(inpt)
			print(morse2text(morse_dict, morse_input))

		else:
			print('error, please enter morse, text, t or q.')

if __name__ == '__main__':
	ascii_dict = get_ascii_dict()
	morse_dict = get_morse_dict(ascii_dict)
	main(ascii_dict, morse_dict)