'''
idea: can we generate all paths and select the set of paths to take?
'''

def path_gen(start, end, solution_set, height, width):
    if start == end:
        yield solution_set
    else:
        x, y = start
        up = None
        down = None
        right = None
        left = None
        if x > 0:
            up = x - 1, y
        if x < height - 1:
            down = x + 1, y
        if y < width - 1:
            right = x, y + 1
        if y > 0:
            left = x, y - 1
        