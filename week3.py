#Movie Ticket Pricer
print("--- Movie Ticket Pricer ---")
age=int(input("Enter your age: "))
if age<=12:
    print(f"You fall into 'Child' category.")
    print(f"Your ticket price is: $8")
elif age>=65:
    print(f"You fall into 'Senior' category.")
    print(f"Your ticket price is: $10")    
else:
    print(f"You fall into 'Adult' category.")
    print(f"Your ticket price is: $15")

#The Running Total Calculator
print("--- Running Total Calculator ---")
print("Enter numbers to add them up. Type 'done' to see the total.")
total=0
while True:
    number=str(input("Enter a number or 'done':"))
    if number=="done":
        break    
    total+=float(number)
    print(f"Current total: {total}")
print()
print("--- Final Calculation ---")
print(f"The final sum of all numbers is: {total}")

#Simple Triangle Pattern
print("--- Triangle Pattern Printer ---")
height=int(input("Enter the desired height of the triangle: "))
for i in range(height):
    for j in range(i+1):
        print("*", end="")
    print()

#The "FizzBuzz" Challlenge
print("--- FizzBuzz Challenge (1-100) ---")
for num in range(1,41):
    if num%3==0 and num%5==0:
        print("Fizz-Buzz")    
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)

quantity=int(input("Enter the quantity: "))
a=0
b=1
for num in range(quantity):
    print(a)
    a=b
    b=a+b

#Coffee Shop Order System
print()
print("=== Coffee Shop Order System ===")
print("Enter drink sizes: small, medium, or large")
print("Type 'done' when finished ordering ")
print()
running_total=0
small=3.5
medium=4.5
large=5.5
while True:
    drink=str(input("Enter drink size: "))
    if drink=="done":
        break
    elif drink=="small":
        print(f"Price: ${small}")
        running_total+=small
        print(f"Current total: ${running_total}")
        print()
    elif drink=="medium":
        print(f"Price: ${medium}")        
        running_total+=medium
        print(f"Current total: ${running_total}")   
        print()
    elif drink=="large":
        print(f"Price: ${large}")
        running_total+=large
        print(f"Current total: ${running_total}")
        print()
    else:
        print("Invalid drink type! Try: small, medium, large ")
        print
print()
print("=== Order Summary ===")
print(f"Subtotal: ${running_total}")
loyalty_discount=3
if running_total>=20:
    running_total-=loyalty_discount
print(f"Loyalty Discount: -${loyalty_discount}")
print(f"Final Total: ${running_total}")
print("Thank you for your order!")


#Gym Class Registration System
beginner=12
intermediate=15
advanced=18
current_total=0
multi_class_discount=10
print("=== Gym Class Registration System ===")
print("Enter class level: beginner, intermediate, or advanced")
print("Type 'done' when finished registering")
print()
while True:
    gym_class=str(input("Enter class level: "))
    if gym_class=="done":
        break
    elif gym_class=="beginner":
        print(f"Price: ${beginner}")
        current_total+=beginner
        print(f"Current total: ${current_total}")
        print()
    elif gym_class=="intermediate":
        print(f"Price: ${intermediate}")
        current_total+=intermediate
        print(f"Current total: ${current_total}")
        print()
    elif gym_class=="advanced":
        print(f"Price: ${advanced}")
        current_total+=advanced
        print(f"Current total: ${current_total}")
        print()
    else:
        print("invalid Gym Class type! Try: beginner, intermediate, advanced")
        print()

print("=== Registration Summary ===")
print(f"Subtotal: ${current_total}")
print(f"Multi-Class Discount: -${multi_class_discount}")
if current_total>=60:
    current_total-=multi_class_discount
print(f"Final Total: ${current_total}")
print("Thank you for registering!")

#Guessing Game
correct_answer="Turkey"
chances=3
while chances>0:
    answer=str(input("Which country became independent in 1923?: "))
    if answer==correct_answer:
        print("You got it! You won!")
        break
    else:
        print("Incorrect, Try again!")
        chances-=1
        print(f"You have {chances} chances left")
        print()
if chances==0:
    print("You are run out of chances")
    print("you lost!")
