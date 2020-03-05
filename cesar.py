initial_key = "abcdefghijklmnopqrstuvwxyz "


def change(shift, letter):
    index = initial_key.index(letter) + shift
    if index > 26:
        index = index - 27
    return initial_key[index]


if __name__ == '__main__':
    print('Ingresa tu texto')
    text = input()
    print('Ingresa tu llave')
    key = input()
    shift = initial_key.index(key)

    new_string = ""

    for letter in text:
        new_string = new_string + change(shift, letter)

    print(new_string)