from collections import Counter


initial_key = "abcdefghijklmnopqrstuvwxyz "


def change(shift, letter):
    index = initial_key.index(letter) + shift
    if index > 26:
        index = index - 27
    return initial_key[index]





with open('cipher2.txt', 'r') as file:
    data = file.read()
    letters = Counter(data)
    print("cantidad de letras = ", len(letters))
    groups = []
    groups.append("")
    groups.append("")
    groups.append("")
    groups.append("")
    index = 0
    while index < len(data):
        try:
            groups[0] = groups[0] + data[index]
        except:
            pass
        try:
            groups[1] = groups[1] + data[index+1]
        except:
            pass
        try:
            groups[2] = groups[2] + data[index+2]
        except:
            pass
        try:
            groups[3] = groups[3] + data[index+3]
        except:
            pass
        index = index + 4
        
    
    with open(f'cipherA.txt', 'w') as file:
        file.write('')
    
    index = 0
    shifts = [20, 0,25,17]
    new_groups = []
    new_groups.append("")
    new_groups.append("")
    new_groups.append("")
    new_groups.append("")
    for group in groups:
        letters = Counter(group)

        new_string = ""
        for letter in group:
            new_string = new_string + change(shifts[index], letter)
    
        new_groups[index] = new_string
        index = index + 1

        



    
    # Space
    index = 0
    string_new = ""
    for letter in range(0, len(new_groups[0])):
        try: 
            string_new = string_new + new_groups[0][index]
        except:
            pass
        try: 
            string_new = string_new + new_groups[1][index]
        except:
            pass
        try: 
            string_new = string_new + new_groups[2][index]
        except:
            pass
        try: 
            string_new = string_new + new_groups[3][index]
        except:
            pass
        index = index + 1
    with open(f'results3/cipher2.txt', 'w') as file:
        file.write(string_new)



    
    


