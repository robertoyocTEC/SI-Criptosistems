import random

initial_key = "abcdefghijklmnopqrstuvwxyz "


def change(shift, letter):
    index = initial_key.index(letter) + shift
    if index > 26:
        index = index - 27
    return initial_key[index]


if __name__ == '__main__':
    print('Ingresa tu texto')
    text = input()
    key = ""

    for a in range(0,4):
        key = key + random.choice(initial_key)

    new_string = ""

    for index in range(0, len(text)):
        key_v = key[index%4]
        shift = initial_key.index(key_v)
        new_string = new_string + change(shift, text[index])

    print("Llave: ")
    print(key)

    print("Texto Cifrado: ")
    print(new_string)