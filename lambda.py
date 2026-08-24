#1
x = int(input("Enter your age "))
hello = lambda: "you are eligible to vote" if x > 18 else "you are not eligible to vote"

print(hello())

#2 

b = int(input("Enter first number "))
d = int(input("Enter second number "))
f = int(input("Enter third number "))

max_num = lambda: print("The maximum number is", max(b, d, f))

print(max_num())

#3

t  = int(input("enter a number"))

check = lambda: "it is less than 0" if t < 0 else "it is equal to 0" if t == 0 else "it is greater than 0"

print(check())

#4 

length  = 5
width = 12
area = lambda: length * width
print("The area of rectangle is", area())

#5

principle = int(input("Enter principle amount "))
rate = int(input("Enter rate of interest "))
time = int(input("Enter time in years "))
interest = lambda: (principle * rate * time) / 100
print("The simple interest is", interest())

#6 

celcius = int(input("Enter temperature in celsius "))
fahrenheit = lambda: (celcius * 9/5) + 32

print("The temperature in fahrenheit is", fahrenheit())

#7

marks = int(input("Enter marks "))
grade = lambda: "A" if marks >= 80 else "B" if marks >= 60 else "C"
print("The grade is", grade())

#8 

list_price = int(input("Enter list price "))
discount = int(input("Enter discount percentage "))

final_price = lambda: list_price - (list_price * discount / 100)
print("The final price after discount is", final_price())

#9

num = int(input("Enter a number "))
check_d = lambda: "It is divisible by 3 and 5" if num % 3 == 0 and num % 5 == 0 else "It is not divisible by both 3 and 5"
print(check_d())

#10 

price = int(input("Enter price of the product "))
tax  = lambda: price + (price * 0.18)
print("The price after adding 18% tax is", tax())
