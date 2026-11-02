import random


def random_usr():
    random_user_id = ''
    for i in range(6):
        random_user_id += random.choice('0123456789abcdefghijklmnopqrstuvwxyz')
    return random_user_id
print(random_usr())

def user_id_gen_by_user():
    numb_char = int(input('How many characters Long Would You Like It to Be: '))
    numb_ids = int(input('How many ids do you want to generate: '))
    for j in range(numb_ids):
        usr_gen = ''
        for l in range(numb_char):
            usr_gen += random.choice('0123456789abcdefghijklmnopqrstuvwxyz')
        print(usr_gen)
user_id_gen_by_user()

def rgb_color_gen():
    a = random.randint(1,255)
    b = random.randint(1,255)
    c = random.randint(1,255)
    print(f'rgb({a},{b},{c})')
rgb_color_gen()

# Exercise 2 soon 

print('Opsec')