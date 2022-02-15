import random


def generate_password(length: int, chars: str) -> str:
    password = ''
    for _ in range(length):
        password = password + random.choice(list(chars))
    return password


def brute_force(length: int, chars: str, correct_password: str) -> None:
    wrong_passwords = []
    while True:
        password = ''
    
        for _ in range(length):
            password += random.choice(list(chars))
     
        if password not in wrong_passwords:
            if password != correct_password:
                wrong_passwords.append(password)
            else:
                print(password)
                break


if __name__ == '__main__':
    chars = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789'
    length = input('Enter password length: ')
    user_password = generate_password(int(length), chars)

    print(user_password + "\n")
    brute_force(int(length), chars, user_password)
