import numpy as np

'''
    For all testers in this file,
    tester returns False if it sees repeat
    True otherwise
'''

from deserializer import grid

def row_no_rep(grid, row_no):
    '''
    determine if grid has repeat letter on row "row_no"
    '''
    row = grid[row_no, :]
    seen = set()
    for letter in row:
        if letter != "_":
            if letter in seen:
                return False # has repeat letter
            else:
                seen.add(letter)
    return True

def column_no_rep(grid, column_no):
    '''
    determine if grid has repeat letter on column "column_no"
    '''
    column = grid[:, column_no]
    seen = set()
    for letter in column:
        if letter != "_":
            if letter in seen:
                return False  # has repeat letter
            else:
                seen.add(letter)
    return True

def submatrix_no_rep(grid, nth_sub):
    '''
    determine if grid has repeat letter in submatrix "nth_sub"
    NOTE: nth_sub is ROW-prime
    :param nth_sub: nth sub-matrix
    '''
    row_idx = int(nth_sub / 3) * 3
    column_idx = int(nth_sub % 3) * 3
    sub_m = grid[row_idx:(row_idx+3), column_idx:(column_idx+3)]
    seen = set()
    for l in sub_m:
        for c in l:
            if c != "_":
                if c in seen:
                    return False
                else:
                    seen.add(c)
    return True

if __name__ == "__main__":
    print(grid)
    for i in range(9):
        assert row_no_rep(grid, i)
        assert column_no_rep(grid, i)
        assert submatrix_no_rep(grid, i)
