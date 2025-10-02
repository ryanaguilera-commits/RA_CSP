#RA 7th string notes

#examples
first_name = input("what is your first name: \n").strip().capitalize()

last_name = input("what is your last name").strip().capitalize()

sentence = "the quick brown fox jumps over the lazy dog"

print("hello", first_name + " " + last_name)
 
# Sanitization and stupid proofing
#stripping it of any spaces and fixing capitlization
#stupid proofing is higher level building your code so users don't break it sanitization is step 1 of stupid proofing

# Debugging is fixing coder
#programmers spend 80 percent of your time debugging 20 percent building code
#bug is error in your code
#3 types of bugs, Syntax error-syntax is your grammer if you have spaces or tabs where they don't belong misspeling things equal signs commas.
#logic error - when the computer runs the code completly fine but you get the wrong result
num1 = 1
num2 = 2
print(num1+num2)
#Runtime error - when you have no red lines and the code still breaks. cant concatonate string with integer