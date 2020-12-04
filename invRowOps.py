#Joseph Harrison 2020
#matrix inverse using row operations
import res
import rowEchForm
import detRowOps
import timeit

def inv(user_mat):
    #don't edit the user's matrix
    mat = []
    #create the augmented matrix (mat|In)
    for i in range(len(user_mat)):
        mat.append([])
        mat[i] += user_mat[i] + [1 if i == j else 0 for j in range(len(user_mat))]
    #we can compute the determinant to check it's non-zero and bring the augented matrix 
    #to row echelon form
    if detRowOps.det(mat) == 0:
        return None
    else:
        #now we can bring the augmented matrix to a reduced row echelon form and read 
        #off the inverse
        rowEchForm.red_row_ech_form(mat)
        for i in range(len(mat)):
            mat[i] = mat[i][len(mat):]
        return mat

def main():
    print('find the inverse of an nxn matrix using row operations\n')

    n = res.int_in('n: ', lambda n: n > 0, 'must be positive')

    #take entries and create augmented matrix
    mat = res.real_mat_in(n, n)

    dp = res.int_in('\ndecimal places: ', lambda dp: dp > 0, 'must be positive')

    print('\nmatrix:\n')
    res.print_mat(mat)

    start = timeit.default_timer()
    inv_mat = inv(mat)
    end = timeit.default_timer()

    if inv_mat == None:
        print("\ndeterminant is 0 so inverse doesn't exist")
    else:
        print('\ninverse matrix:\n')
        res.round_mat(inv_mat, dp)
        res.print_mat(inv_mat)
    print(f'finished in {round(end - start, 4)}s (4d.p)')

if __name__ == '__main__':
    main()
