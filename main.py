def recipe_read_from_file(file_name:str) -> dict:
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


def get_shop_list_by_dishes(dishes:list, person_count:int) -> dict:
    cook_book = recipe_read_from_file('recipes.txt')
    ingredients = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in list(ingredients.keys()):
                ingredients[ingredient['ingredient_name']]['quantity'] += person_count * ingredient['quantity']
            else:
                ingredients.setdefault(ingredient['ingredient_name'], {'measure': ingredient['measure'],'quantity':person_count * ingredient['quantity']})
    return ingredients


#Testing if the results
print(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))
print(get_shop_list_by_dishes(['Омлет'], 4))
print(get_shop_list_by_dishes(['Фахитос'], 3))