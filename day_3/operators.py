age_int = 32
height_float = 5.9
complex_num = 1-2j

#Area of triangle script&formula
print('Calculate Area of the Triangle')

T_base = input('Triangle base: ')
T_height = input('Triangle height: ')
Base = float(T_base)
height = float(T_height)
triangle_area_formula = 0.5*Base*height
print('the area of the triangle is: ', triangle_area_formula)

#perimeter of triangle script&formula
print('calculate perimeter of a triangle')

side1 = input('Triangle Side a value: ')
side2 = input('Triangle Side b value: ')
side3 = input('Triangle Side c value: ')
side_a = float(side1)
side_b = float(side2)
side_c = float(side3)
triangle_perimeter_formula = side_a + side_b + side_c 
print('The perimeter of the triangle is: ', triangle_perimeter_formula)

#Area & Perimeter of a rectangle script&Formula
print('Calculate Area & Perimeter of a rectangle')
inp_length = input('length of rectangle: ') #inp stands for input
inp_width = input('width of rectangle: ') #inp stands for input
length = float(inp_length)
width = float(inp_width)
rectangle_area_formula = length*width
rectangle_perimeter_formula = 2*(length + width)
print('Area Of Rectangle: ', rectangle_area_formula)
print('Perimeter Of Rectangle: ', rectangle_perimeter_formula)

#Radius of a circle
print('Calculate Area & circumference of a circle')
inp_radius = input('Radius of circle: ')
radius = float(inp_radius)
circle_area_formula = 3.14*radius*radius
circle_circumference_formula = 2*3.14*radius
print('Area Of Circle: ', circle_area_formula)
print('Circumference of circle: ', circle_circumference_formula)

#calculate Slope
print('Calculate Slope')
inp_x2 = input('X2: ')
inp_x1 = input("X1: ")
inp_y2 = input('Y2: ')
inp_y1 = input('Y1: ')
X2 = float(inp_x2)
X1 = float (inp_x1)
Y2 = float(inp_y2)
Y1 = float(inp_y1)
slope_formula = (Y2-Y1) / (X2-X1)
print('Slope is: ', slope_formula)

#false string statements
print(len('python')!= len('dragon'))
print(len('python') > len('dragon'))
print(len('python') < len('dragon'))
#check with is,in,is not
print('on is in python','on' in 'python',' on is in dragon', 'on' in 'dragon')
#better version
print('Is "on" in "python"?:', 'on' in 'python')
print('Is "on" in "dragon"?:', 'on' in 'dragon')

print('is "jargon" in "I hope this course is not full of jargon?"', 'jargon' in 'I hope this course is not full of jargon.')
len_word = len('python')
float_word = float(len_word)
str_word = str(float_word)
print(len_word, float_word, str_word)

print(type(10) == type(10))
print(int(float('9.8')))

#Calculate weekly Pay of the person
print('calculate weekly pay')
hour = float(input('Hours Working: '))
rate = float(input('Rate income Per hour: '))
weekly_pay_formula = hour*rate
print('Your weekly Income Is: ', weekly_pay_formula)

#calculate how long you have to live assuming you live to 100
years = float(input('How old are you(in years): '))
days = years*365
months = years*12
remaining_days = 36500-days
remaining_months = 1200-months
remaining_years = 100-years
print('You Have: ', remaining_years, 'years remaining')
print('You Have: ', remaining_months, 'months remaining')
print('You Have: ', remaining_days, 'days remaining')

print(1,1**0,1**1,1**2,1**3)
print(2,2**0,2**1,2**2,2**3)
#day 3 Completed Fun day :) loved it! wish me luck
print('Congrats to me! :D')