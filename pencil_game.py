import random
random.seed()


print(f'How many pencils would you like to use:')
total_pencils = input()
activator = True
winner = ''
while activator:
    try:
        total_pencils = int(total_pencils)
    except:
        print(f'The number of pencils should be numeric')
        total_pencils = input()
        continue
    else:
        while True:
            if total_pencils < 0:
                print(f'The number of pencils should be numeric')
                total_pencils = input()
                break
            elif total_pencils == 0:
                print(f'The number of pencils should be positive')
                total_pencils = input()
                break
            else:
                activator = False
                break

print(f'Who will be the first (John, Jack):')
first = input()
while True:
    if first != 'John' and first != 'Jack':
        print(f'Choose between John and Jack')
        first = input()
        continue
    else:
        break



print('|' * total_pencils)

while total_pencils > 0:
    print(f"{first}'s turn:")
    if first == 'John':
        first = 'Jack'
        winner = 'Jack'
        turn = input()
        while True:
            while True:
                try:
                    turn = int(turn)
                except:
                    print(f"Possible values: '1', '2' or '3'")
                    turn = input()
                    continue
                else:
                    turn = int(turn)
                if turn < 1 or turn > 3:
                    print(f"Possible values: '1', '2' or '3'")
                    turn = input()
                    continue
                else:
                    break
            if total_pencils - turn < 0:
                print(f'Too many pencils were taken')
                turn = input()
                continue
            else:
                break
    else:
        first = 'John'
        winner = 'John'
        if total_pencils in range(2,9999, 4):
            turn = 1
            print(turn)
        elif total_pencils in range(3,9999,4):
            turn = 2
            print(turn)
        elif total_pencils in range(4,9999,4):
            turn = 3
            print(turn)
        else:
            if total_pencils == 1:
                turn = 1
                print(turn)
            else:
                turn = random.randint(1,3)
                print(turn)
    total_pencils -= turn
    print('|' * total_pencils)
print(f'{winner} won!')