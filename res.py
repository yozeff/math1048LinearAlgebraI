#Joseph Harrison 2020
def real_in(prompt, cond=lambda x: True, err=''):
	while True:
		try:
			x = float(input(prompt))
			if cond(x):
				return x
			else:
				print(err)
		except ValueError:
			print('must be a real number')

def int_in(prompt, cond=lambda x: True, err=''):
	while True:
		try:
			x = int(input(prompt))
			if cond(x):
				return x
			else:
				print(err)
		except ValueError:
			print('must be an integer')

def print_mat(mat, dp=3):
	for i in range(len(mat)):
		row_str = ''
		for j in range(len(mat[i])):
			entry = round(mat[i][j], dp)
			if entry >= 0 and str(entry)[:2] != '-0':
				row_str += ' '
			row_str += str(entry) + ' ' * (dp - len(str(entry - int(entry))) + 1)
			row_str += ' '
		print(row_str)
