import random


def random_choice():
    if random.random() < 0.5:
        return True
    else:
        return False


def int_to_alphabet(x):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[x]


def generate_password():

    pass_length = random.randint(8, 12)
    password = []

    for i in range(0, pass_length):
        if random_choice():
            password.append(random.randint(0, 9))
        else:
            ch = int_to_alphabet(random.randint(0, 25))
            if random_choice():
                ch = ch.capitalize()
            password.append(ch)

    return ''.join(str(e) for e in password)


print(generate_password())