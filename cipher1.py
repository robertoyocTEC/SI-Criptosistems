


initial_key = "abcdefghijklmnopqrstuvwxyz "

def write(shift, data):
    with open(f'results/cipher{shift}.txt', 'w') as file:
        new_string = ""
        for letter in data:
            index = 0
            if ord(letter) == 32:
                index = 96 + shift
            else:
                index = ord(letter) + shift
                if index == 123:
                    index = 32
                elif index > 123:
                    index = index -27
            new_string = new_string + chr(index)
        file.write(new_string)



        




with open('cipher1.txt', 'r') as file:
    data = file.read()
    for number in range(1, 27):
        write(number, data)
    


