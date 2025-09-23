#RA 7th Fizz Buzz

x = 1


while x < 51:
    if x % 15 ==0:
        print(f"fizzbuzz ")
    elif x % 5 ==0:
        print("buzz")
    elif x % 3 ==0:
        print(f"fizz")
    else:
        print(f"{x}")
    x += 1



