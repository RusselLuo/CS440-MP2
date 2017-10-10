from deserializer import init_state
from path_generator import driver

'''1. preproc'''
state = {}
for k, v in init_state.items():
    print(v)
    state[k] = frozenset(list(driver(v[0], v[1], 7, 7)))

for k in state:
    print(len(state[k]))

