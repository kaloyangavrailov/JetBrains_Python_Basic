grid_creation = '         '
X_s = grid_creation.count('X')
O_s = grid_creation.count('O')

tezt_l_1 = []
tezt_l_2 = []
tezt_l_3 = []

for x in range(0, len(grid_creation)):
    if x < 3:
        tezt_l_1.append(grid_creation[x])
    elif 2 < x < 6:
        tezt_l_2.append(grid_creation[x])
    elif x > 5:
        tezt_l_3.append(grid_creation[x])


t_t = []
result = ''

t_t.append(tezt_l_1)
t_t.append(tezt_l_2)
t_t.append(tezt_l_3)


def print_game_grid():
    print(f'---------')
    print(f'| {t_t[0][0]} {t_t[0][1]} {t_t[0][2]} |')
    print(f'| {t_t[1][0]} {t_t[1][1]} {t_t[1][2]} |')
    print(f'| {t_t[2][0]} {t_t[2][1]} {t_t[2][2]} |')
    print(f'---------')


def game_state_test():
    global result
    if t_t[0][0] == t_t[0][1] == t_t[0][2]:
        if t_t[0][0] == 'X' and t_t[0][1] == 'X' and t_t[0][2] == 'X':
            result = f'X wins'
        elif t_t[0][0] == 'O' and t_t[0][1] == 'O' and t_t[0][2] == 'O':
            result = 'O wins'
    elif t_t[0][0] == t_t[1][0] == t_t[2][0]:
        if t_t[0][0] == 'X' and t_t[1][0] == 'X' and t_t[2][0] == 'X':
            result = f'X wins'
        elif t_t[0][0] == 'O' and t_t[1][0] == 'O' and t_t[2][0] == 'O':
            result = 'O wins'
    elif t_t[0][1] == t_t[1][1] == t_t[2][1]:
        if t_t[0][1] == 'X' and t_t[1][1] == 'X' and t_t[2][1] == 'X':
            result = f'X wins'
        elif t_t[0][1] == 'O' and t_t[1][1] == 'O' and t_t[2][1] == 'O':
            result = 'O wins'
    elif t_t[0][2] == t_t[1][2] == t_t[2][2]:
        if t_t[0][2] == 'X' and t_t[1][2] == 'X' and t_t[2][2] == 'X':
            result = f'X wins'
        elif t_t[0][2] == 'O' and t_t[1][2] == 'O' and t_t[2][2] == 'O':
            result = 'O wins'
    elif t_t[1][0] == t_t[1][1] == t_t[1][2]:
        if t_t[1][0] == 'X' and t_t[1][1] == 'X' and t_t[1][2] == 'X':
            result = f'X wins'
        elif t_t[1][0] == 'O' and t_t[1][1] == 'O' and t_t[1][2] == 'O':
            result = 'O wins'
    elif t_t[2][0] == t_t[2][1] == t_t[2][2]:
        if t_t[2][0] == 'X' and t_t[2][1] == 'X' and t_t[2][2] == 'X':
            result = f'X wins'
        elif t_t[2][0] == 'O' and t_t[2][1] == 'O' and t_t[2][2] == 'O':
            result = 'O wins'
    elif t_t[0][0] == t_t[1][1] == t_t[2][2]:
        if t_t[0][0] == 'X' and t_t[1][1] == 'X' and t_t[2][2] == 'X':
            result = f'X wins'
        elif t_t[0][0] == 'O' and t_t[1][1] == 'O' and t_t[2][2] == 'O':
            result = 'O wins'
    elif t_t[0][2] == t_t[1][1] == t_t[2][0]:
        if t_t[0][2] == 'X' and t_t[1][1] == 'X' and t_t[2][0] == 'X':
            result = f'X wins'
        elif t_t[0][2] == 'O' and t_t[1][1] == 'O' and t_t[2][0] == 'O':
            result = 'O wins'
    elif ' ' not in tezt_l_1 and ' ' not in tezt_l_2 and ' ' not in tezt_l_3:
        result = 'Draw'
    elif ' ' in tezt_l_1 or ' ' in tezt_l_2 or ' ' in tezt_l_3:
        result = 'Game not finished'


print_game_grid()

previous_choice = 'X'

while True:
    choice = input()
    try:
        coor_1, coor_2 = choice.split()
    except:
        print(f'You should enter numbers!')
        continue
    try:
        coor_1 = int(coor_1)
        coor_2 = int(coor_2)
    except:
        print(f'You should enter numbers!')
        continue
    coor_1 -= 1
    coor_2 -= 1
    if -1 < coor_1 < 3 and -1 < coor_2 < 3:
        if t_t[coor_1][coor_2] == 'X' or t_t[coor_1][coor_2] == 'O':
            print(f'This cell is occupied! Choose another one!')
        else:
            if previous_choice == 'X':
                t_t[coor_1][coor_2] = 'X'
                previous_choice = 'O'
            else:
                previous_choice = 'X'
                t_t[coor_1][coor_2] = 'O'


            print_game_grid()
            game_state_test()
            if result == 'Game not finished':
                continue
            elif result == 'Draw':
                print(result)
                break
            elif result == f'X wins':
                print(result)
                break
            elif result == 'O wins':
                print(result)
                break
    else:
        print(f'Coordinates should be from 1 to 3!')