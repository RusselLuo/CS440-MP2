'''
algorithm overview
variable: color taken by a square
domain: colors
constraint:
    1. cannot zigzag
    2. path cannot overlap

NOTE: to get rid of the annoying edge case where you have two
neighboring squares of the same color when you get to end points,
we pretend that end points doesn't exist.

We could achieve this purpose by starting with the starting points
as the initial solution_set;
Any attempt to directly write to end points location will FAIL
'''
from parse_txt import start_points, end_points, state
from utils import get_four_neighbors, get_num_neighbors_of_color
height, width = 5, 5

print(start_points)
print(end_points)

temp_color_list = end_points.values()
# temp_color_list = ['R', 'B', 'O', 'Y', 'G']
temp_color_set = set(temp_color_list)
print(temp_color_list)

end_area = {}
for k, v in end_points.items():
    end_area[v] = get_four_neighbors(k, height, width)

def is_goal_state(solution_set):
    '''
    idea: every "end" square has a neighboring square of its color
    '''
    is_goal = True
    for end_point, end_color in end_points.items():
        count = get_num_neighbors_of_color(end_point, end_color, solution_set, height, width)
        if count != 1:
            is_goal = False
            break
    return is_goal

def get_next_location_to_assign(solution_set):
    '''
    idea: maintain a set of visited squares
    keep expanding
    :return: a 2-D tuple (row, column)
    '''
    for column in range(width):
        for row in range(height):
            if (row, column) not in solution_set:
                yield (row, column)

def get_ordered_domain_value(next_to_assign, solution_set):
    '''
    :return: a list of colors ("Y", "B", etc)
    '''
    return temp_color_list

def can_assign_color_at(color, location, solution_set):
    '''
    location must be valid
    :return: true if can assign color at location
    '''
    x, y = location
    assert x >= 0 and x < height and y >= 0 and y < width

    if location in solution_set or location in end_points:
        return False # has already been assigned / hitting an end point
    # has exactly one neighbor already assigned the same color
    count = get_num_neighbors_of_color(location, color, solution_set, height, width)
    return count == 1

# def csp(solution_set):
#     print(solution_set)
#     if is_goal_state(solution_set):
#         return solution_set
#     for next_to_assign in get_next_location_to_assign(solution_set):
#         for color in get_ordered_domain_value(next_to_assign, solution_set):
#             if can_assign_color_at(color, next_to_assign, solution_set):
#                 solution_set[next_to_assign] = color
#                 rec_result = csp(solution_set)
#                 if rec_result != None:
#                     return rec_result
#                 solution_set.pop(next_to_assign) # reset
#     return None # mark failure

def csp_trial(solution_set, color_set):
    # print(solution_set)
    if len(color_set) == 0:
        return solution_set
    for next_to_assign in get_next_location_to_assign(solution_set):
        for color in color_set:
            # print("TRYING TO PUT " + color + " IN " + str(next_to_assign))
            if can_assign_color_at(color, next_to_assign, solution_set):
                solution_set[next_to_assign] = color
                if next_to_assign in end_area[color]:
                    color_set -= {color}
                rec_result = csp_trial(solution_set, color_set)
                if rec_result != None:
                    return rec_result
                color_set.add(color)
                solution_set.pop(next_to_assign) # reset
    return None # mark failure

if __name__ == "__main__":
    # print(csp(start_points))
    print(csp_trial(start_points, temp_color_set))