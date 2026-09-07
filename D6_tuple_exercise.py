# # Level 1

# # 1
# empty_tuple = tuple()

# # 2
# brothers = ('John', 'Smith')
# print('Brothers:', brothers) # ('John', 'Smith')
# sisters = ('Anna', 'Elsa')
# print('Sisters:', sisters) # ('Anna', 'Elsa')

# # 3
# siblings = brothers + sisters
# print('Siblings:', siblings) # ('John', 'Smith', 'Anna', 'Elsa')

# # 4 
# print('Number of siblings:', len(siblings)) # 4

# # 5
# parents = ('Peter', 'Mary')
# print('Parents:', parents) # ('Peter', 'Mary')

# family_members = siblings + parents
# print('Family Members:', family_members) # ('John', 'Smith', 'Anna', 'Elsa', 'Peter', 'Mary')

# # Level 2

# # 1

# family_members = lst_family_members = list(family_members)
# print('Family Members (as list):', lst_family_members)

# brothers = lst_family_members[0:2]
# print('Brothers:', brothers) # ['John', 'Smith']

# sisters = lst_family_members[2:4]
# print('Sisters:', sisters) # ['Anna', 'Elsa']

# parents = lst_family_members[4:6]
# print('Parents:', parents) # ['Peter', 'Mary']

# # 2

# fruits = ('banana', 'orange', 'mango', 'lemon', 'lime', 'apple')
# print('Fruits:', fruits) # ('banana', 'orange', 'mango', 'lemon', 'lime', 'apple')

# vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
# print('Vegetables:', vegetables) # ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')

# animal_products = ('milk', 'meat', 'butter', 'yogurt')
# print('Animal Products:', animal_products) # ('milk', 'meat', 'butter', 'yogurt')

# tpl_food_stuff = fruits + vegetables + animal_products
# print('Food Stuff:', tpl_food_stuff)

# # 3

# lst_food_stuff = list(tpl_food_stuff)
# print('Food Stuff (as list):', lst_food_stuff)

# # 4
# middle_items = lst_food_stuff[3:8]
# print('Middle Items:', middle_items) # ['lemon', 'lime', 'apple', 'Tomato', 'Potato']

# # 5
# first_three_items = lst_food_stuff[:3]
# print('First Three Items:', first_three_items) # ['banana', 'orange', 'mango']

# last_three_items = lst_food_stuff[-3:]
# print('Last Three Items:', last_three_items) # ['meat', 'butter', 'yogurt']  

# # 6
# del tpl_food_stuff

# # 7
# does_exist = 'banana' in tpl_food_stuff

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Nordic Countries:', nordic_countries) # ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

is_exist = 'Estonia' in nordic_countries
print('Is Estonia a nordic country?', is_exist) # False

is_exist = 'Iceland' in nordic_countries
print('Is Iceland a nordic country?', is_exist) # True