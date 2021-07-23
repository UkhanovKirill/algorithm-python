from os import urandom


def random_number():
    random = int(int.from_bytes(urandom(7), 'big')) >> 5
    list = [n for n in range(0, 101)]
    return list[random % 100]


secret = random_number()
i = 1
while i <= 10:
    print(f'Попытка №{i:2} из 10')
    user_number = int(input('Введите число от 1 до 100: '))
    if user_number == secret:
        print('Загаданное число угадано')
        break
    elif user_number > secret:
        print(f'Ваше число {user_number} больше загаданного')
    else:
        print(f'Ваше число {user_number} меньше загаданного')
    i += 1
if i > 10:
    print(f'Не угадано! Загаданное число {secret}')