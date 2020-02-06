# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
def check_simple(n):
    if n < 1 or n > 1000 or int(n) != n:
        print('Введите натуральное число от 1 до 1000')
    elif n == 1:
        print('Число ' + str(n) + ' - Составное')
    elif n == 2:
        print('Число ' + str(n) + ' - Простое')
    elif n == 3:
        print('Число ' + str(n) + ' - Простое')
    elif n % 2 == 0:
        print('Число ' + str(n) + ' - Составное')
    else:
        delitel = 2
        i = 0
        while delitel < n / 2:
            if (n / delitel).is_integer():
                print('Число ' + str(n) + ' - Составное')
                i = 1
                break

            else:
                delitel += 1
        if i == 0:
            print('Число ' + str(n) + ' - Простое')
        else:
            pass


# 2) выводит список всех делителей числа;
list = []


def del_list(n):
    delitel = 1
    i = 0
    if n < 1 or n > 1000 or int(n) != n:
        print('Введите натуральное число от 1 до 1000')

    else:
        for i in range(n):
            if (n / delitel).is_integer():
                list.append(delitel)
                delitel += 1
            else:
                delitel += 1
        print('Делители числа ', n, ' - ', list)


# 3) выводит самый большой простой делитель числа.

list = []
list2 = []


def del_simple_max(n):
    if n < 1 or n > 1000 or int(n) != n:
        print('Введите натуральное число от 1 до 1000')
    else:
        if n == 1:
            print('Самый большой простой делитель числа ', n, ' - 1')
        else:
            delitel = 1
            i = 0
            for i in range(n):
                if (n / delitel).is_integer():
                    list.append(delitel)
                    delitel += 1
                else:
                    delitel += 1
            m = 0
            for m in list:
                if m == 1:
                    pass
                elif m == 2:
                    list2.append(m)
                elif m == 3:
                    list2.append(m)
                elif m % 2 == 0:
                    pass
                else:
                    delitel = 2
                    i = 0
                    while delitel < m / 2:
                        if (m / delitel).is_integer():
                            i = 1
                            break
                        else:
                            delitel += 1
                    if i == 0:
                        list2.append(m)
                    else:
                        pass
            print('Самый большой простой делитель числа ', m, ' - ', list2[-1])


# 4) функция выводит каноническое разложение числа на простые множители;
list = []
list2 = []


def kanon(n):
    if n < 1 or n > 1000 or int(n) != n:
        print('Введите натуральное число от 1 до 1000')
    else:
        delitel = 1
        i = 0
        for i in range(n):
            if (n / delitel).is_integer():
                list.append(delitel)
                delitel += 1
            else:
                delitel += 1
        m = 0
        for m in list:
            if m == 1:
                pass
            elif m == 2:
                list2.append(m)
            elif m == 3:
                list2.append(m)
            elif m % 2 == 0:
                pass
            else:
                delitel = 2
                i = 0
                while delitel < m / 2:
                    if (m / delitel).is_integer():
                        i = 1
                        break
                    else:
                        delitel += 1
                if i == 0:
                    list2.append(m)
                else:
                    pass

        list3 = sorted(list2)
        list4 = []
        m = n
        for i in list3:
            while m % i == 0:
                list4.append(i)
                m = m / i
            else:
                continue
        print('Каноническое разложение числа ', n, ' на простые множители :', list4)


# 5)функция выводит самый большой делитель (не обязательно простой) числа.
list = []


def max_delitel(n):
    if n < 1 or n > 1000 or int(n) != n:
        print('Введите натуральное число от 1 до 1000')
    else:
        delitel = 1
        i = 0
        for i in range(n):
            if (n / delitel).is_integer():
                list.append(delitel)
                delitel += 1
            else:
                delitel += 1
        print('Самый большой делитель числа', n, ' - ', list[-1])
        print('Самый большой делитель числа', n, ', не равный ему - ', list[-2])
