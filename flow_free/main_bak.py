'''
algorithm overview
variable: color taken by a square
domain: colors
constraint:
    1. cannot zigzag
    2. path cannot overlap
'''

def is_goal_state(solution_set):
    pass

def get_next_location_to_assign(solution_set):
    '''
    :return: a 2-D tuple (row, column)
    '''
    pass

def get_ordered_domain_value(solution_set):
    '''
    :return: a list of colors ("Y", "B", etc)
    '''
    return []

def can_assign_color_at(color, location, solution_set):
    '''
    :return: true if can assign color at location
    '''
    if location in solution_set:
        return False # has already been assigned
    row, column = location
    up = row - 1, column
    down = row + 1, column
    right = row, column + 1
    left = row, column - 1
    # has exactly one neighbor already assigned the same color
    count = 0
    if up in solution_set:
        count += int(solution_set[up][0] == color)
    pass

def csp(solution_set):
    if is_goal_state(solution_set):
        return solution_set
    next_to_assign = get_next_location_to_assign(solution_set)
    for color in get_ordered_domain_value(solution_set):
        if can_assign_color_at(color, next_to_assign, solution_set):
            solution_set[next_to_assign] = (
                color,
                False # not a source
            )
            rec_result = csp(solution_set)
            if rec_result != None:
                return rec_result
            solution_set.pop(next_to_assign) # reset
    return None # mark failure