#Joseph Harrison 2020
import res
import timeit

#row replacement: add s times the j-th row to the i-th row
def row_rep(mat, i, j, s):
	mat[i] = [mat[i][k] + s * mat[j][k] 
			  for k in range(len(mat[i]))]

#row scaling: multiply the i-th row by s
def row_sca(mat, i, s):
	mat[i] = [mat[i][j] * s for j in range(len(mat[i]))]

def row_ech_form(mat):
	for i in range(len(mat) - 1):
		#eliminate the entries under the i-th row in the i-th column
		for j in range(i + 1, len(mat)):
			try:
				row_rep(mat, j, i, -mat[j][i] / mat[i][i])
			except ZeroDivisionError:
				#if the entry is 0, this just means we have a zero-row
				continue
 
def red_row_ech_form(mat, ref=False):
	#if ref (row echelon form) is true, the procedure will assume mat is in a row echelon form
	if not ref:
		row_ech_form(mat)
	for i in range(len(mat)):
		try:
			#make sure the pivot of the i-th row is 1
			row_sca(mat, i, 1 / mat[i][i])
		except ZeroDivisionError:
			#if the entry is 0, this just means we have a zero-row
			continue
		#eliminate all of the entries above the i-th pivot
		for j in range(i):
			row_rep(mat, j, i, -mat[j][i])

def main():
	print('bring an nxm matrix with real enries to a (reduced) row echelon form using row \noperations\n')

	n = res.int_in('n: ', lambda n: n > 0, 'n must be positive')
	m = res.int_in('m: ', lambda m: m > 0, 'm must be positive')

	mat = []
	print('\nentries:')
	for i in range(n):
		mat.append([])
		for j in range(m):
			mat[i].append(res.real_in(f'({i + 1}, {j + 1})-th: '))

	start = timeit.default_timer()
	row_ech_form(mat)
	end = timeit.default_timer()
	total_time = end - start

	print('\nrow echelon form:\n')
	res.print_mat(mat)

	start = timeit.default_timer()
	red_row_ech_form(mat, ref=True)
	end = timeit.default_timer()
	total_time += end - start
	
	print('\nreduced row echelon form:\n')
	res.print_mat(mat)
	print(f'\nfinished in {round(total_time, 4)}s (4d.p)')

if __name__ == '__main__':
	main()