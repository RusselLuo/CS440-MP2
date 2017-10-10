
filename = "assets/input88.txt"

init_state = {}

with open(filename) as f:
    for line_no, line in enumerate(f):
        line = line[0:-1]
        for col_no, c in enumerate(line):
            if c != "_":
                if c in init_state:
                    init_state[c].append((line_no, col_no))
                else:
                    init_state[c] = [(line_no, col_no)]

if __name__ == "__main__":
    print(init_state)