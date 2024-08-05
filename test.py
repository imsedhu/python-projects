#print hello and name
print("hello")
print("m.sedhuraman")


#simple interest
principalAmount = int(input("enter principal Amount: "))
timePeriod = int(input("enter the time period (in years): "))
rateOfInterest = float(input("enter the rate of interest: "))
simpleInterest = (principalAmount*timePeriod*rateOfInterest)/100
print("simple interest is: ",simpleInterest)


#square and cube from given number
number = int(input("Enter a number: "))
square = number ** 2
cube = number ** 3
print("Square value is:", square)
print("Cube valueis:", cube)

#sum and average of 5 subjects
tamil = int(input("enter the tamil mark:"))
english = int(input("enter the english mark:"))
maths = int(input("enter the maths mark:"))
science = int(input("enter the scienec mark:"))
socialscience = int(input("enter the socialscience mark:"))
total = tamil+english+maths+science+socialscience
average = total/5
print("sum of the subjects:",total)
print("average is:",average)

#swapping two number with third variable
a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
c=a
a=b
b=c
print("after swapping a:" , a)
print("after swapping b:" , b)

#swapping two number without third variable
a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
a = a+b
b = a-b
a = a-b
print("after swapping a:" , a)
print("after swapping b:" , b)

#area and perimeter of rectangele 
length = int(input("enter the length of rectangle:"))
width = int(input("enter the width of rectangle:"))
area = length*width
perimeter = 2*(length+width)
print("area of rectangle:", area)
print("perimeter of rectangle:", perimeter)

#area and perimeter of triangle
a = int(input("enter the length of first side:"))
b = int(input("enter the length of second side:"))
c = int(input("enter the length of third side:"))
perimeter = a+b+c
semi_perimeter = perimeter/2
area = (semi_perimeter*(semi_perimeter-a)*(semi_perimeter-b)*(semi_perimeter-c))**0.5
print("area of triangle is:", area)
print("perimeter of triangle is:", perimeter)