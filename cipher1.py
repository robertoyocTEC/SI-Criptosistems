


initial_key = "abcdefghijklmnopqrstuvwxyz "

def write(shift, data):
    with open(f'results2/cipher{shift}.txt', 'w') as file:
        new_string = ""
        for letter in data:
            index = initial_key.index(letter) + shift
            if index > 26:
                index = index - 27
            decoded = initial_key[index]
            new_string = new_string + decoded
        file.write(new_string)


        




with open('cipher1.txt', 'r') as file:
    data = file.read()
    for number in range(1, 27):
        write(number, data)
    


