#dictionary Exercise    day 8 of 30days
dog = {}
dog['color'] = 'black'
dog['breed'] = 'pitbull'
dog['legs'] = 'medium'
dog['age'] = 'old'

print('dog information: ',dog)

student = {'first_name':'planet',
            'last_name':'aura', 
            'gender':'male',
            'age':'122', 
            'martial status':'noneType',
            'skills':['learning python'], 
            'continent':'asia',
            'city':'secret'
            }

print('length of student dictionary: ', len(student))
print('student skills: ', student['skills'])
student['skills'].append('Hardware')
print('dictionary keys: ', student.keys())
print('dictionary to list: ', list(student))
print('dictionary to list of tuples: ', student.items())
remove = student.pop('age')
print('removing age item: ', student)
del student

#day 8 complete www 8/30