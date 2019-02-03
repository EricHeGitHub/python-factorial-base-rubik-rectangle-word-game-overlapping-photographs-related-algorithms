from collections import deque
from sys import exit

def row_exchange(cube):
    cube_copy = cube
    cube_copy = list(cube_copy)
    temp = cube_copy[0:4]
    cube_copy[0:4] = cube_copy[4:8]
    cube_copy[4:8] =temp
    return ''.join(str(i) for i in cube_copy)

def right_circular_shift(cube):
    cube_copy = cube
    row_1 = deque(cube_copy[0:4])
    row_2 = deque(cube_copy[4:8])
    row_1.rotate()
    row_2.rotate()
    cube_copy = row_1 + row_2
    return ''.join(i for i in cube_copy)

def left_circular_shift(cube):
    cube_copy = cube
    row_1 = deque(cube_copy[0:4])
    row_2 = deque(cube_copy[4:8])
    row_1.rotate(-1)
    row_2.rotate(-1)
    cube_copy = row_1 + row_2
    return ''.join(i for i in cube_copy)

def middle_clock_wise(cube):
    cube_copy = cube
    cube_copy = list(cube_copy)
    row = deque(cube_copy[1:3]+cube_copy[6:4:-1])
    row.rotate()
    row = list(row)
    cube_copy[1:3] = row[0:2]
    cube_copy[6:4:-1] = row[2:4]
    return ''.join(i for i in cube_copy)

def middle_counter_clock_wise(cube):
    cube_copy = cube
    cube_copy = list(cube_copy)
    row = deque(cube_copy[1:3]+cube_copy[6:4:-1])
    row.rotate(-1)
    row = list(row)
    cube_copy[1:3] = row[0:2]
    cube_copy[6:4:-1] = row[2:4]
    return ''.join(i for i in cube_copy)

cube = input('Input final configuration: ')

test_input = [1] * 8
for i in cube:
    if i in '12345678' and i.isdigit():
        test_input[int(i)-1] *= -1
    elif i == ' ' or i == '\t':
        pass
    else:
        print('Incorrect configuration, giving up ...')
        exit()
if test_input.count(1):
    print('Incorrect configuration, giving up ...')
    exit()
states_old_start = set()
states_old_start.add('12348765')
states_new_start = set()

cube_clean = []
for i in cube:
    if i.isdigit():
        cube_clean.append(i)
cube_clean = ''.join(i for i in cube_clean)
cube_temp = cube_clean[4:]
cube_temp = list(cube_temp)
cube_temp.reverse()
cube_temp = ''.join(i for i in cube_temp)
cube_clean = cube_clean[0:4] + cube_temp
states_old_end = set()
states_old_end.add(cube_clean)
states_new_end = set()
flag = -1
steps = 0
while states_old_start & states_old_end == set():
    if flag == -1:
        for i in states_old_start:
            states_new_start.add(row_exchange(i))
            states_new_start.add(right_circular_shift(i))
            states_new_start.add(middle_clock_wise(i))
        states_old_start = states_new_start
        states_new_start = set()
    else:
        for i in states_old_end:
            states_new_end.add(row_exchange(i))
            states_new_end.add(left_circular_shift(i))
            states_new_end.add(middle_counter_clock_wise(i))
        states_old_end = states_new_end
        states_new_end = set()
    steps += 1
    flag *= -1
        
print('{} steps are needed to reach the final configuration.'.format(steps))
        






        
        
    
