c = True

while c:
    try:
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))

        print('Итог: ', a / b)
        print('Остаток: ', a % b)

        d = input('Enter "y" to continue or no "n": ')
        if d == 'n':
            c = False
        else:
            continue

    except ValueError:
        print('Enter only number')
    except ZeroDivisionError:
        print('Don\'t divistion zero')
