filename = "assets/input77.txt"
state = {}
with open(filename) as f:
    for line_no, line in enumerate(f):
        line = line[0:-1]
        for col_no, c in enumerate(line):
            if c != "_":
                state[(line_no, col_no)] = (
                    c, # color of square
                    True # is_source
                )

if __name__ == "__main__":
    print(state)