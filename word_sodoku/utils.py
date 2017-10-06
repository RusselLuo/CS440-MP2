import numpy as np
from deserializer import grid, word_bank

def test_row(grid, row_no):
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

def test_column(grid, column_no):
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

def test_submatrix(grid, nth_sub):
    '''
    determine if grid has repeat letter in submatrix "nth_sub"
    NOTE: nth_sub is ROW-prime
    :param nth_sub: nth sub-matrix
    '''
    row_idx = int(nth_sub / 3) * 3
    column_idx = int(nth_sub % 3) * 3
    sub_m = grid[row_idx:(row_idx+3), column_idx:(column_idx+3)]
    print(sub_m)

if __name__ == "__main__":
    print(grid)
    test_submatrix(grid, 0)
    test_submatrix(grid, 4)
    test_submatrix(grid, 5)
    test_submatrix(grid, 8)