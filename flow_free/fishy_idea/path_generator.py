'''
idea: can we generate all paths and select the set of paths to take?
'''

height, width = 8, 8

def get_four_neighbors(location):
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

def only_one_visited_in_four_neighbors(location, visited):
    '''
    prevent zigzag pattern
    can take care of the case where a neighbor is None
    '''
    up, down, left, right = get_four_neighbors(location)
    count = 0
    if up in visited:
        count += 1
    if down in visited:
        count += 1
    if left in visited:
        count += 1
    if right in visited:
        count += 1
    return count == 1

def path_gen(start, end, solution_set, visited):
    if start == end:
        yield solution_set
    else:
        # print("AT: ", start)
        curr_visited = visited | {start}
        up, down, left, right = get_four_neighbors(start)
        # print("EXPANDING ON: ", up, down, left, right)
        if up != None and up not in curr_visited and only_one_visited_in_four_neighbors(up, curr_visited):
            # print("UP WORKS")
            yield from path_gen(up, end, frozenset(solution_set | {up}), curr_visited)
        if down != None and down not in curr_visited and only_one_visited_in_four_neighbors(down, curr_visited):
            # print("DOWN WORKS")
            yield from path_gen(down, end, frozenset(solution_set | {down}), curr_visited)
        if left != None and left not in curr_visited and only_one_visited_in_four_neighbors(left, curr_visited):
            # print("LEFT WORKS")
            yield from path_gen(left, end, frozenset(solution_set | {left}), curr_visited)
        if right != None and right not in curr_visited and only_one_visited_in_four_neighbors(right, curr_visited):
            # print("RIGHT WORKS")
            yield from path_gen(right, end, frozenset(solution_set | {right}), curr_visited)

def driver(start, end, input_height, input_width):
    global height
    height = input_height
    global width
    width = input_width
    yield from path_gen(start, end, frozenset(), set())


def test(test_height, test_width, start, end):
    paths = list(driver(start, end, test_height, test_width))
    print(paths)
    print(len(paths))
    return len(paths)

if __name__ == "__main__":
    l1 = test(3, 3, (0, 0), (2, 2))
    l2 = test(3, 3, (0, 1), (2, 1))