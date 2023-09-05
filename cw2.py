my_name = input("whats you name")
my_age =int(input("whats yoour age "))
print(f"My name is {my_name} and I am {my_age} years old")
first_number=int(input("first number:"))
secound_number =int(input("second number:"))
operation = input("the operation:")
if operation=='+':
    print(first_number+secound_number)
elif operation=='-':
    print(first_number-secound_number)
elif operation=='*':
    print(first_number*secound_number)
elif operation=='/':
    print(first_number/secound_number)
else:
    print("the operation is not valid")

bus_capacity = 120
people_inbus=int(input("how many people are on the bus:")) 
people_outbus = int(input("how many people are outside the bus:"))
empty_seats = bus_capacity - people_inbus
if empty_seats>people_outbus:
 print("the empty seats is +empty_seats")
 print(f"the number of the empty seats is {empty_seats}")
elif empty_seats<=people_inbus:
    print("there is not empty seats")



