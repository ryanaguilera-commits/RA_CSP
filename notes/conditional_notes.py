#RA 7th Conitional notes
##homework_done = input("is your homwork done\n").strip().capitalize()

##if homework_done == "yes":
    #print("yes you can go")
##else:
    #print("go do your homework")

grade = 1001

if grade>= 89:
    if grade > 100:
        print("You cheated that isn't possible")
    else:
        print(f"you have {grade}% thats an A")
elif grade>79:
    print(f"you have an {grade} that is a B")
else:
    print(f"you have an {grade} that's an F")


name = input("what is yout name\n")

if name == "Ms Larose":
    print("you are the teacher")
elif name == "Tia" or name == "Ashley":
    print("you are the TA")
else:
    print(f"hello, {name} you are a student")