from fishy_idea.deserializer import init_state
from fishy_idea.path_generator import driver

height, width = 8, 8

'''1. preproc'''
state = {}
for k, v in init_state.items():
    print(v)
    state[k] = list(driver(v[0], v[1], height, width))

for k in state:
    print(len(state[k]))

'''2. backtracking'''
