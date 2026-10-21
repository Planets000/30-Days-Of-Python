#Day 2: 30 days of python programming, goodluck to me
first_name = 'john'
last_name = 'smith'
full_name = first_name + ' ' + last_name
country = 'USA'
city = 'New York'
age = 28
year = 2026
is_married = True
is_true = True
is_light_on = False

#Multiple lines variables
first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = 'john', 'smith', 'john smith', 'USA', 'New York', '28', 2026, True, True, False

#Testing if it works
print(first_name)
print(last_name)
print(age)
print('Married:', is_married)
print('Is light on:', is_light_on)

#2nd exercise Checking data types

print(type(first_name))
print(type(28))
print(type('planet'))
print(type(is_true))
print(type(full_name))

print(len(first_name))
print('First Name Length:', len(first_name), 'Last Name Length:', len(last_name))

#Numbers & Math

num_one = 5 
num_two = 4
num_addition = num_one + num_two
num_subtraction = num_two - num_one
num_multiplication = num_two * num_one
num_division = num_one / num_two
num_remainder = num_two % num_one
exp = num_one**num_two
floor_division = num_one//num_two

# radius of a circle = 30

radius_of_circle = 30
area_of_circle = (3.14*radius_of_circle**2)
print(area_of_circle)
circum_of_circle = 2*3.14*radius_of_circle
print(circum_of_circle)

#user input test

user1_first_name = input('Your Name:')
user1_last_name = input('last name:')
user1_country = input('country:')
user1_age = input('Age:')
user1_fullname = user1_first_name + ' ' + user1_last_name
print('FirstName:', user1_first_name)
print('LastName:', user1_last_name)
print('FullName:', user1_fullname)
print('Country:', user1_country)
print('Age:', user1_age)

#Day 2 Completed :)