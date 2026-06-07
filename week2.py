from math import pi
#Exercise1
#Temperature Converter
temp_in_celsius=float(input("Enter a temperature in Celcius:"))
temp_in_fahrenheit=(temp_in_celsius*9/5)+32
temp_in_kelvin=temp_in_celsius+273.15
print()
print("="*40)
print(f"Temperature in Celsius: {round(temp_in_celsius,2)}")
print(f"Temperature in Fahrenheit: {round(temp_in_fahrenheit,2)}")
print(f"Temperature in Kelvin: {round(temp_in_kelvin,2)}")
print("="*40)
print()

#Circle Properties Calculator
radius=float(input("Enter the radius of a circle:"))
area_of_circle=round(pi*radius**2,2)
circumference_of_circle=round(2*pi*radius,2)
print()
print("="*40)
print(f"Area of a circle is: {area_of_circle}")
print(f"Circumference of a circle is: {circumference_of_circle}")
print("="*40)
print()
#Grade Eligibility Checker
in_deans_list=False
name=str(input("Enter your name:"))
gpa=float(input("Enter your GPA:"))
total_credit_hours=int(input("Enter your total credit hours:"))
print(f"Student name: {name}")
print(f"Student GPA: {gpa}")
print(f"Student total credit hours:{total_credit_hours}")
if gpa>=3.5 and total_credit_hours>=12:
    in_deans_list=True
elif gpa<3.5 and total_credit_hours>=12:
    print(f"{name} needs {round(3.5-gpa,2)} gpa points to be eligible")
elif gpa>=3.5 and total_credit_hours<12:
    print(f"{name} needs {round(12-total_credit_hours,2)} credit hours to be eligible")
else:
    print(f"{name} needs {round(12-total_credit_hours,2)} credit hours and {round(3.5-gpa,2)} gpa points to be eligible")
print(f"{name} in dean's list: {in_deans_list}")

#Smart Shopping Cart Calculator
is_member=False
item_name=str(input("Enter the item name:"))
price=float(input(f"Enter the price of {item_name}:$"))
quantity=int(input(f"Enter the quantity of {item_name}:"))
is_member=(input("You are member of our Supermarket: (Yes/No): "))
subtotal=round(quantity*price,2)
discount=(is_member=="Yes")*0.1*subtotal
tax=(subtotal-discount)*0.05
shipping=subtotal*0.02
total=(subtotal-discount)+tax+shipping
print(f"item name: {item_name}")
print(f"item price: ${price}")
print(f"item quantity: {quantity}")
print(f"You have discount of: ${discount}")
print(f"Your tax: ${tax}")
print(f"Your shipping cost: ${shipping}")
print(f'Your total: ${total}')

#Electronics Store
item1=str(input("Enter your 1st item:"))
item2=str(input("Enter your 2nd item:"))
item3=str(input("Enter your 3rd item:"))
price1=float(input(f"Enter the price of {item1}:$ "))
price2=float(input(f"Enter the price of {item2}:$ "))
price3=float(input(f"Enter the price of {item3}:$ "))
quantity1=int(input(f"Enter the quantity of {item1}: "))
quantity2=int(input(f"Enter the quantity of {item2}: "))
quantity3=int(input(f"Enter the quantity of {item3}: "))
customer_name=str(input("Enter your name: "))
is_member=str(input("Are you a member? (Yes/No): "))
total_previous_purchases=float(input("Enter your previous purchases total: "))
item1_total=price1*quantity1
item2_total=price2*quantity2
item3_total=price3*quantity3
total_items=quantity1+quantity2+quantity3
subtotal=round(((quantity1*price1)+(quantity2*price2)+(quantity3*price3)),2)
#Discounts
member_discount=round((is_member=="Yes")*0.1*subtotal,2)
bulk_discount=round(0.05*(total_items>5)*subtotal,2)
loyalty_discount=round(0.03*(total_previous_purchases>=1_000)*subtotal,2)
all_discounts_stack=round(member_discount+bulk_discount+loyalty_discount,2)
subtotal_with_discounts=round(subtotal-(member_discount+loyalty_discount+bulk_discount),2)
tax=round(0.12*subtotal_with_discounts,2)
shipping=round((subtotal<=1500)*25,2)
final_total=round((subtotal-all_discounts_stack)+tax+shipping,2)
#Output Display
print(f"Customer name: {customer_name}")
print(f"Membership status: {is_member=="Yes"}")
print(f"Item: {item1}, price: {price1}, quantity: {quantity1}, item total: ${item1_total}")
print(f"Item: {item2}, price: {price2}, quantity: {quantity2}, item total: ${item2_total}")
print(f"Item: {item3}, price: {price3}, quantity: {quantity3}, item total: ${item3_total}")
print(f"Subtotal: ${subtotal}")
print(f"Membership discount amount: ${member_discount}, Membership Discount: {member_discount!=0}")
print(f"Bulk discount amount: ${bulk_discount}, Bulk Discount: {bulk_discount!=0}")
print(f"Loyalty discount: ${loyalty_discount}, Loyalty Discount:{loyalty_discount!=0}")
print(f"Total discount amount: ${all_discounts_stack}")
print(f"Subtotal with discounts: ${subtotal_with_discounts} ")
print(f'Tax amount: ${tax}')
print(f"Shipping cost: ${shipping}, Free shipping: {shipping>1500}")
print(f"Final total:${final_total}")
print(f"Total amount saved: ${all_discounts_stack}")