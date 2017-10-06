import numpy as np
'''
1. read grid files
'''
grid_filename = "assets/grid1.txt"
grid = []
with open(grid_filename) as f:
    for line in f:
        grid.append(list(line[0: -1]))
grid = np.array(grid)

'''
2. read word banks
'''
word_bank = set()
bank_filename = "assets/bank1.txt"
with open(bank_filename) as f:
    for line in f:
        word_bank.add(line[0:-1])

if __name__ == "__main__":
    print(grid)