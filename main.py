#1

def show_message():
    print("Welcome to python")

show_message()

#2

def show_name():
    s = input("Enter your name")
    print(s)
    return s

print(show_name())

#3

def show_number():
    print(50)

print(show_number())

#4

def print_subject():
    f = input("Enter your favroute subject")
    print(f)
    return f

print(print_subject())

#5 

def add(u,i):
    return u + i

print(add(10,20))

#6

def multiply(a,b):
    return a * b

print(multiply(6,8))
#7

def greet_student(greet):
    print("Hello", greet)

greet_student("Chanchal")

#8

def display_marks(Hindi,English,Math):
    print("Hindi:",Hindi, "\n","English", English, "\n", Math)

print(display_marks(89,65,55))

#9

def square(sq):
    return sq**2

print(square(5))

#10 

def square(sq3):
    return sq3**3

print(square(5))

#11

def subtract(a,b):
    return a - b

print(subtract(50,15))

#12

def area_rectangle():
    length = int(input("Enter the length of rectangle: "))
    breadth = int(input("Enter the breadth of rectangle: "))
    area = length * breadth
    print("Area of rectangle:", area)

print(area_rectangle())

#13

def get_age():
    age = int(input("Enter your age: "))
    print("Your age is:", age)
    return age

print(get_age())

#14

def get_city():
    city = input("Enter your city: ")
    print("You live in:", city)
    return city

print(get_city())

#15

def calculate_total(price, quantity):
    total = price * quantity
    print("Total price:", total)
    return total

print(calculate_total(10, 5))


#16

def find_average(num1,num2,num3):
    average = (num1 + num2 + num3) / 3
    print("Average:", average)
    return average

print(find_average(10, 20, 30))

#17 

def check_number(num):
    if num > 0:
        print("Positive number")
    else:
        print("negative  number")

print(check_number(-5))

#18

def largest(nu1,nu2):
    if nu1 > nu2:
        print(nu1, "is the largest number")
    else:
        print(nu2, "is the largest number")

print(largest(10, 20))

#19

def is_even(num):
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")

print(is_even(7))

#20

def calculate_discount(price,discount):
    discounted_price = price - (price * discount / 100)
    print("Discounted price:", discounted_price)
    return discounted_price

print(calculate_discount(100, 10))
