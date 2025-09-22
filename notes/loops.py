foods = ["Pizza", "Ice cream", "Chocolate" ]


#For loop
for food in foods:
    print(f"{food} is my favorite food")
    print("hi")
for x in range(1,20):
    print(x)


#while loop
#i = 0
#while True:
#    print(i)
#    i+=1


#infinite loops


#correct while loops
i = 1
while i < 20:
    print(i)
    i+=1


x = 1

while x < 21:
    if x % 2 ==0:
        print(f"{x} is an even number")
    else:
        print("{x} is an odd number")
    x += 1

import random

d = 1
end = random.randint(1,20)

while d != end:
    print("duck")
    d+=1

print("goose")



while True:
    if d == end:
        print("goose")
    
    else:
        print("duck")
        d += 1