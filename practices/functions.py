#RA 7th Functions notes

def welcome():
    name = input("what is your name")
    print(f"Hello, {name}")


print("this is not in my function")


def add(number, number2):
    number += number2
    print(number)


num1 = 12
num2 = 4

add(80, 8)
add(8, 30)


import random
def roll(mod):
    return random.randint(2, 20) + mod

strength = roll(0)
dexterity = roll(3)
inteligence = roll(2)
charisma = roll(5)
print('here are your stats')
print(f"strength: {roll(0)}\ndex: {roll(3)}\nInt: {roll(2)}\nChar: {roll(5)}" )