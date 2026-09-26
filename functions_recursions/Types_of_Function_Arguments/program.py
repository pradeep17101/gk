#Name=T.Pradeep
#lab=07
#roll=25341A05K1


#Task1: Positional and Keyword Arguments

def student_info(name, roll_no, branch):
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Branch:", branch)

student_info("Pradeep", 101, "CSE")
student_info(branch="CSE", name="Pradeep", roll_no=101)

#Output:
#Name: Pradeep
#Roll No: 101
#Branch: CSE
#Name: Pradeep
#Roll No: 101
#Branch: CSE


#Task2: Default Arguments

def calculate_price(price, tax_rate=18, discount=0):
    tax = price * tax_rate / 100
    return price + tax - discount

print("Final Price:", calculate_price(1000))
print("Final Price:", calculate_price(1000, 10))
print("Final Price:", calculate_price(1000, 10, 100))

#Output:
#Final Price: 1180.0
#Final Price: 1100.0
#Final Price: 1000.0


#Task3: Variable-Length Arguments (*args)

def total_marks(*marks):
    return sum(marks), sum(marks) / len(marks)

total, average = total_marks(80, 75, 90)
print("Total:", total, "Average:", average)

total, average = total_marks(80, 75, 90, 85, 70)
print("Total:", total, "Average:", average)

total, average = total_marks(95)
print("Total:", total, "Average:", average)

#Output:
#Total: 245 Average: 81.66666666666667
#Total: 400 Average: 80.0
#Total: 95 Average: 95.0


#Task4: Keyword Variable-Length Arguments (**kwargs)

def build_profile(**details):
    print("Profile")
    for key, value in details.items():
        print(key.capitalize() + ":", value)

build_profile(name="Pradeep", age=19, city="Hyderabad", hobby="Cricket")

build_profile(name="Siddu", age=17, city="Delhi")

#Output:
#Profile
#Name: Pradeep
#Age: 19
#City: Hyderabad
#Hobby: Cricket
#Profile
#Name: Siddu
#Age: 17
#City: Delhi


#Task5: Combining All Argument Types

def order_summary(customer, *items, discount=0, **extra):
    print("Customer:", customer)
    print("Items:")
    for item in items:
        print("-", item)
    print("Discount:", discount, "%")
    print("Extra Info:")
    for key, value in extra.items():
        print(key.replace("_", " ").capitalize() + ":", value)

order_summary("Pradeep", "Laptop", "Mouse", discount=10,
              delivery_address="Hyderabad", gift_wrap=True)

#Output:
#Customer: Pradeep
#Items:
#- Laptop
#- Mouse
#Discount: 10 %
#Extra Info:
#Delivery address: Hyderabad
#Gift wrap: True