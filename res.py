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

#return a string of length size containing x
#x can really be an instance of any class that has the __str__ method
def pad(x, size):
    s = str(x)
    if len(s) > size:
        return s[:size]
    else:
        return s + ' ' * (size - len(s))

#find the length of the entry with the longest string in column j
def longest_entry(mat, j):
    max_len = 0
    for i in range(len(mat)):
        l = len(str(mat[i][j]))
        if str(mat[i][j]) == '-0.0' or str(mat[i][j]) == '0.0':
            l = 1
        if l > max_len:
            max_len = l
    return max_len

#size is the space each entry takes up on the screen
def print_mat(mat):
    #longest entries for each column
    max_lens = [longest_entry(mat, j) for j in range(len(mat[0]))]
    for i in range(len(mat)):
        row_str = ''
        for j in range(len(mat[i])):
            #add a space to compensate for the '-' for negatives
            if mat[i][j] >= 0:
                row_str += ' '
            if str(mat[i][j]) == '-0.0' or str(mat[i][j]) == '0.0':
                row_str += pad('0', max_lens[j]) + ' '
            else:
                row_str += pad(mat[i][j], max_lens[j]) + ' '
            #give the negative entries a space at the end
            if mat[i][j] < 0:
                row_str += ' '
        print(row_str)

#input an n by m matrix
def real_mat_in(n, m):
    mat = []
    print(f'\nenter {n}x{m} matrix: ')
    for i in range(n):
        #create a placeholder row
        mat.append([0] * m)
        flag = True
        while flag:
            row = input(f'row {i + 1}: ')
            row = row.split(' ')
            if len(row) != m:
                print(f"row must contain {m} ' ' delimited entries")
            else:
                #try to cast each entry in the row
                j = 0
                while j < m:
                    try:
                        x = float(row[j])
                        mat[i][j] = x
                    except ValueError:
                        print('row must contain real entries')
                        j = m
                    j += 1
                #j = m if success j = m + 1 if not
                if j == m:
                    flag = False
    return mat

def round_mat(mat, dp):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = round(mat[i][j], dp)
