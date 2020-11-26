#Joseph Harrison 2020
#matrix determinant using row operations and cofactor expansions
import rowEchForm
import res
import timeit

def det(mat, ref=False):
	if not ref:
		rowEchForm.row_ech_form(mat)
	det = 1
	for i in range(len(mat)):
		if det == 0:
			continue
		det *= mat[i][i]
	return det

def main():
	print('compute the determinant of an nxn matrix using row operations\n')

	n = res.int_in('n: ', lambda n: n > 0, 'n must be positive')

	mat = []
	print('\nentries:')
	for i in range(n):
		mat.append([])
		for j in range(n):
			mat[i].append(res.real_in(f'({i + 1}, {j + 1})-th: '))
	print()
	res.print_mat(mat)

	start = timeit.default_timer()
	d = det(mat)
	end = timeit.default_timer()
	print(f'\ndeterminant by row operations: {round(d, 3)} (3d.p)')
	print(f'finished in {round(end - start, 4)}s (4d.p)')
		
if __name__ == '__main__':
	main()