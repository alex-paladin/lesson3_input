while True:

    print('Введите число NUM1 (>=0):')

    num1 = input()
    try:
        if float(num1)<0:
            print('Вы ввели число<0. Повторите ввод')
            continue
        if float(num1)>=0:
            print('NUM1 =', num1)
            break
    except ValueError:
        print('Вы ввели не число. Повторите ввод')
        continue

while True:

    print('Введите число NUM2 (>=0):')

    num2 = input()
    try:
        if float(num2)<0:
            print('Вы ввели число<0. Повторите ввод')
            continue
        if float(num2)>=0:
            print('NUM2 =', num2)
            break
    except ValueError:
        print('Вы ввели не число. Повторите ввод')
        continue

print('**********************')
print('NUM1 =',float(num1), 'NUM2 =',float(num2))
print('**********************')
print('NUM1 + NUM2 =',float(num1)+float(num2))
print('NUM1 - NUM2 =',float(num1)-float(num2))


