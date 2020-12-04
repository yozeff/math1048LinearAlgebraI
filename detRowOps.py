#Joseph Harrison 2020
#matrix determinant using row operations and cofactor expansions
import rowEchForm
import res
import timeit
import sys

#calculate determinant as product of diagonal entries
def det(mat, ref=False):
    if not ref:
        rowEchForm.row_ech_form(mat)
    det = 1
    for i in range(len(mat)):
        #if a zero is reached immediately return zero
        if det == 0:
            continue
        det *= mat[i][i]
    return det

def main():
    print('compute the determinant of an nxn matrix using row operations\n')

    n = res.int_in('n: ', lambda n: n > 0, 'must be positive')

    mat = res.real_mat_in(n, n)
    print()
    res.print_mat(mat)

    dp = res.int_in('\ndecimal places: ', lambda dp: dp > 0, 'must be positive')

    start = timeit.default_timer()
    d = det(mat)
    end = timeit.default_timer()
    print(f'\ndeterminant by row operations: {round(d, dp)}')
    print(f'finished in {round(end - start, 4)}s (4d.p)')
        
if __name__ == '__main__':
    main()
