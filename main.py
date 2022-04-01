def recipe_read(file_name:str) -> dict:
    cook_book = {}
    bool_switch = True
    file = open(file_name, 'rt', encoding='utf-8')
    temp_key = ''
    counter = 0
    for line in file:
        if bool_switch:
            cook_book.setdefault(line.strip(), [])
            temp_key = line.strip()
            bool_switch = False
        elif line == '\n':
            bool_switch = True
        elif counter == 0:
            counter = int(line.strip())
        else:
            temp = line.strip().split(' | ')
            cook_book[temp_key] += [{'ingredient_name': temp[0], 'quantity': int(temp[1]), 'measure': temp[2]}]
            counter -= 1

    file.close()
    return cook_book




print(recipe_read('recipes.txt'))