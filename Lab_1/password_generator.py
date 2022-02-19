import random
import itertools


def generate_password(length: int, chars: str) -> str:
    password = ''
    for _ in range(length):
        password += random.choice(list(chars))
    return password


def brute_force(length: int, chars: str, correct_password: str) -> None:
    password = itertools.product(chars, repeat = length)
    for i in password:
        str = ''.join(i)
        if str == correct_password:
            print(str)
            break


if __name__ == '__main__':
    chars = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789'
    length = int(input('Enter password length: '))

    hitrate = dict.fromkeys(chars, 0)

    for i in range(10000):
        user_password = generate_password(length, chars)
        for elem in user_password:
            hitrate[elem] += 1

    for char in hitrate:
        if hitrate[char] > 0:
            print(char, hitrate[char])

    passwd = generate_password(length, chars)
    print(passwd)


    brute_force(int(length), chars, passwd)
