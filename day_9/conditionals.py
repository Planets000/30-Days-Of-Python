#Exercise 1 :)
print('Are You Old enough To Learn to drive?')
usr_age = float(input('Enter Your Age: '))
if usr_age < 18:
    print(f'you got {18 - usr_age} more years to learn to drive')
else: 
    print('Your Old Enough To learn to Drive!')

print('whos older me or you?')
my_age = 33
if usr_age == 33:
    print('were the same age')
elif usr_age > 33:
    if usr_age - 33 == 1:
        print(f'you are {usr_age - 33} year older then me')
    else:
        print(f'you are {usr_age - 33} years older than me')
elif 33 - usr_age == 1:
    print(f'you are {33 - usr_age} years younger than me')
else:
    print(f'you are {33 - usr_age} years younger than me')

print('What Number Is Bigger?')
num_a = float(input('Enter First Number: '))
num_b = float(input('Enter Second Number: '))

if num_a > num_b:
    print(f'{num_a} is Greater than {num_b}')
elif num_a < num_b:
    print(f'{num_b} is Greater than {num_a}')

# self test
print('which car is faster?')
car_a = float(input('First Cars Speed In Km/h: '))
car_b = float(input('Second Cars Speed In Km/h: '))
if car_a > car_b:
    print(f'The First car is faster By {car_a - car_b} Kph')
elif car_a < car_b:
    print(f'The Second Car is faster By {car_b - car_a} Kph')
else:
    print('Both Cars Are The Same Speed')

#Exercise 2
print('Find Out your Grade')
Grades = '''sh
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
'''
grade = float(input('What is your grade: '))
if grade >= 90 and grade <= 100:
    print('You Got An A!')
elif grade >= 80:
    print('You Got a B!')
elif grade >= 70:
    print('You Got a C')
elif grade >= 60:
    print('You Got a D')
else:
    print('You Got an F')

print('What Month Is It?')
usr_month = input('What Month is it: ')
if usr_month in ['September', 'October', 'November']:
    print('The Season Is Autumn')
elif usr_month in ['December', 'January', 'February']:
    print('The Season Is Winter')
elif usr_month in ['March', 'April', 'May']:
    print('The Season is spring')
else:
    print('The Season Is Summer')

print('Check To See if Fruit exists In My List')
fruits = ['banana', 'orange', 'mango', 'lemon']

usr_fruit = input('Does the fruit exist in the list?')
if usr_fruit in fruits:
    print(f'{usr_fruit} Is in The list')
else:
    fruits.append(usr_fruit)
    print(f'{usr_fruit} Was Just Added To The List')

#Exercise 3
    #Exercise 3
person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_married': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
    'street': 'Space street',
    'zipcode': '02210'
}
}

    
    # Un-indent Exercise 3 so it lines up with the left margin
if 'skills' in person and person['skills']:
    skills_list = person['skills']
    middle_index = len(skills_list) // 2
    print(f"Middle skill: {skills_list[middle_index]}")


    if 'skills' in person: has_python = 'Python' in person['skills']
    print(f"Has Python skill: {has_python}")

    if 'skills' in person: skills = person['skills']
    # Checking for fullstack first since it shares overlapping skills
    if 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')
    elif 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print('He is a front end developer')
    else:
        print('unknown title')

    if person.get('is_married') and person.get('country') == 'Finland': first = person['first_name']
    last = person['last_name']
    country = person['country']
    print(f"{first} {last} is married and lives in {country}.")