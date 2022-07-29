def check(v1,v2,v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + " ... lazy"
    if (v1 == 1 or v2 == 1) and v3 =='*':
        msg = msg +  ' ... very lazy'
    if (v1 == 0 or v2 == 0) and ( v3 == '*' or v3 =='+' or v3 =='-'):
        msg = msg + " ... very, very lazy"
    if msg != "":
        msg = "You are" + msg
        print(msg)


def is_one_digit(v1):
    if -10 < v1 < 10 and float.is_integer(v1):
        return True
    else:
        return False


msg_list = ["Are you sure? It is only one digit! (y / n)","Don't be silly! It's just one number! Add to the memory? (y / n)","Last chance! Do you really want to embarrass yourself? (y / n)"]
msg_index = 0
memory = 0
result = 0
activator = True
activator1 = True


while True:
    while activator1:
        while activator:
            print(f'Enter an equation')
            x, oper, y = input().split()

            if x == 'M':
                x = memory
            if y == "M":
                y = memory

            try:
                x = float(x)
                y = float(y)
            except:
                print(f'Do you even know what numbers are? Stay focused!')
                continue

            if oper == '+' or oper == '-' or oper == '*' or oper == '/':
                activator = False
                break
            else:
                print(f"Yes ... an interesting math operation. You've slept through all classes, haven't you?")
                continue
        if oper == '+':
            check(x, y, oper)
            result = x + y
            print(result)
            activator1 = False
            break
        elif oper == '-':
            check(x, y, oper)
            result = x - y
            print(result)
            activator1 = False
            break
        elif oper == '*':
            check(x, y, oper)
            result = x * y
            print(result)
            activator1 = False
            break
        elif oper == '/' and y != 0:
            check(x, y, oper)
            result = x / y
            print(result)
            activator1 = False
            break
        else:
            check(x, y, oper)
            print(f'Yeah... division by zero. Smart move...')
            activator = True
            continue
    print(f'Do you want to store the result? (y / n):')
    answer = input()
    if answer == 'y':
        if is_one_digit(result):
            while msg_index < 3:
                if is_one_digit(result):
                    print(msg_list[msg_index])
                    answer = input()
                    if answer == 'y' and msg_index < 2:
                        msg_index += 1
                        continue
                    if answer == 'y' and msg_index == 2:
                        memory = result
                        break
                    if answer == 'n':
                        msg_index = 0
                        break
                else:
                    memory = result
                    break
        else:
            memory = result
        print(f'Do you want to continue calculations? (y / n):')
        answer = input()
        if answer == 'y':
            activator1 = True
            activator = True
            continue
        elif answer == 'n':
            break
    elif answer == 'n':
        print(f'Do you want to continue calculations? (y / n):')
        answer = input()
        if answer == 'n':
            break
        elif answer == 'y':
            activator1 = True
            activator = True
            continue