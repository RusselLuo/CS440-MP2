def get_four_neighbors(location, height, width):
    x, y = location
    up = None
    down = None
    right = None
    left = None
    if x > 0:
        up = x - 1, y
    if x < height - 1:
        down = x + 1, y
    if y > 0:
        left = x, y - 1
    if y < width - 1:
        right = x, y + 1
    return up, down, left, right

def get_num_neighbors_of_color(location, color, solution_set, height, width):
    up, down, left, right = get_four_neighbors(location, height, width)
    count = 0
    if up in solution_set and solution_set[up] == color:
        count += 1
    if down in solution_set and solution_set[down] == color:
        count += 1
    if left in solution_set and solution_set[left] == color:
        count += 1
    if right in solution_set and solution_set[right] == color:
        count += 1
    return count