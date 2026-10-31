# day 11
def add_two_numbers(num1,num2):
    sum_num = num1 + num2
    return sum_num
print('add two numbers: ', add_two_numbers(2,4))

def area_of_circle(r):
    area = 3.14 * r * r
    return area
print('area of circle: ', area_of_circle(10))

def add_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total
result = add_all_nums(3,6,1)

print('all nums: ', result)
print('The Type is: ', type(result))

celsius = float(input('°C: '))
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit
print(convert_celsius_to_fahrenheit(celsius), '°F')

month = input('What Month Is It: ')
def check_season(month):
    season = ''
    if month in ['January', 'February', 'December']:
        season = 'Winter'
    elif month in ['March','April','May']:
        season = 'Spring'
    elif month in ['June','July','August']:
        season = 'Summer'
    else:
        season = 'Autumn'
    return season
print(check_season(month))


def calculate_slope():
    y2 = float(input('Whats Y2: '))
    y1 = float(input('Whats Y1: '))
    x2 = float(input('Whats X2: '))
    x1 = float(input('Whats X1: '))
    Y = y2 - y1
    X = x2 - x1
    if X == 0:
        print('Wrong Input Divison by Zero')
        return "Undefined"
    if Y == 0:
        print('Wrong Input Divison by Zero')
        return "Undefined"
    slope = Y / X
    return slope
print(calculate_slope())

print('Quadratic Equation')

def solve_quadratic_eqn():
    A = int(input('ax²: '))
    B = int(input('bx: '))
    C = int(input('c: '))

    D = B**2 - 4*A*C
    answr = 0
    answr1 = 0
    if D > 0:
        answr = (-B+D**0.5)/(2*A)
        answr1 = (-B-D**0.5)/(2*A)
        print('It has 2 Answers')
        print(f'X = {answr}')
        print(f'X = {answr1}')
    elif D == 0:
        answr = -B/(2*A)
        print(answr)
    else:
        print("No real roots (the answers are complex/imaginary numbers).")

solve_quadratic_eqn()


print('Print any list')
planets =  ['Earth', 'Mars']
fruits = ['Apple', 'Banana']
# i wanted to use 0 parameters lol
def print_list():
    lst_usr = input('List: ')
    lst = globals()[lst_usr] # i know in actual code globals isnt good to use often but wanted to try it anyway
    print(lst)
print_list()
