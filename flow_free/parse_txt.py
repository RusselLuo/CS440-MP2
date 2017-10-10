filename = "assets/tiny_input.txt"
state = {}

seen_color = set()
start_points = {}
end_points = {}

with open(filename) as f:
    for line_no, line in enumerate(f):
        line = line[0:-1]
        for col_no, c in enumerate(line):
            if c != "_":
                state[(line_no, col_no)] = c # color of square
                if c not in seen_color:
                    start_points[(line_no, col_no)] = c
                    seen_color.add(c)
                else:
                    end_points[(line_no, col_no)] = c

if __name__ == "__main__":
    print(state)
    print(start_points)
    print(end_points)