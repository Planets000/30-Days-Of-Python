#Exercise 1
empty_tuple = tuple() #or ()

brothers = ('muhammad', 'jake', 'ahmad', 'bob') #Imaginary names
sisters = ('sarah', 'veronica', 'kara') #imaginary names
siblings = brothers + sisters

print(f"You Have: {len(siblings)} siblings")

family_members = list(siblings)
family_members.append('smith') #imaginary
family_members.append('layla') #imaginary
print('Family Members: ', family_members)

#Exercise 2
siblings_lst = family_members[0:7]
print('Siblings: ', siblings_lst)

parents_lst = family_members[7:9]
print('Parents: ', parents_lst)

fruits = ('apple', 'banana', 'orange')
vegetables = ('lettuce', 'carrot', 'broccoli')
animal_products = ('milk', 'egg', 'honey')
food_stuff_tpl = fruits + vegetables + animal_products
print('food stuff: ', food_stuff_tpl)

food_stuff_lst = list(food_stuff_tpl)

slicing_itm = len(food_stuff_lst)
print('Number of food items: ', slicing_itm)
middle_items = food_stuff_lst[2:7]
print('Middle Items: ', middle_items)

last_three = food_stuff_lst[-3:]
first_three = food_stuff_lst[0:3]
print('First Three Items: ', first_three)
print('Last Three Items: ', last_three)

del food_stuff_tpl

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('is Estonia a nordic country?', 'Estonia' in nordic_countries)
print('is Iceland a nordic Country?', 'Iceland' in nordic_countries)
#donee :)