def monthly_amounts(other_things):
   return round(other_things/ income*100,2)

income = int(input("What is your monthly income?\n"))
rent = monthly_amounts(1500)
utilities = monthly_amounts(600)
groceries = monthly_amounts(100)
transportation = monthly_amounts(85)


print(f"\nYour rent takes up {rent}% of your income")
print(f"\nYour utilities take up {utilities}% of your income") 
print(f"\nYour groceries take up {groceries}% of your income")
print(f"\nYour transportation takes up {transportation}% of your income")
