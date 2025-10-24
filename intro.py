#!/bin/python
#print strings
print("Hello world!") #double quotes string
print('Hello world!') #single quotes string
print('''This line
runs on a
multiple lines''') # tripple quotes
print("This string is "+"awesome!") #concatenation
print("\n") #creates a new line
print("Test the new line")

#Maths
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS or BODMAS
print(50 ** 2) #exponents
print(25 ** 0.5) #square root
print(50 % 6) #takes what is left over
print(50 / 6) #division with remainder or float
print(50 // 6) #division with no remainder

#Variables and methods
quote = "All is fair in love and war"
print(quote)
print(quote.upper()) #uppercase method
print(quote.title()) #titlecase method
print(len(quote)) #count numbers of characters

name = "Yahboy" #string data
print(quote.lower()) #lowercase method
age = 55 # int or integer
gpa = 5.0 #float

print(int(gpa))
print(float(age))

print("My name is "+name+" and my age is "+str(age))

age += 1
print(age)
birthday = 1
age += birthday
print(age)

#Functions- they are bits of code that can perform a specific task
def who_am_i(): #funtion with no parameter
	name = "Yahboy" #local variable
	age = 29
	print("My name is "+name+" and my age is "+str(age))
who_am_i()
who_am_i()

def addHundred(num):
	print(num + 100)
addHundred(50)
addHundred(10)

def add(x, y):
	print(x + y)
add(5, 6)
add(10, 5)

def multi(x, y):
	return x * y
print(multi(2, 20))

def square_root(x):
	print(x ** 0.5)
square_root(64)

def new_line():
	print("\n")
new_line()


#Boolean Expressions (True or False)
bool1 = True
bool2 = 3 * 3 == 9
bool3 = False
bool4 = 3 * 3 != 9
print(bool1, bool2, bool3, bool4)

bool5 = "True"
print(type(bool5))
print(type(bool1))# to know the type

#Relational And Boolean operators
gThan = 7 > 5
lThan = 5 < 7
gThanEqualTo = 7>= 7
lThanEqualTo = 7 <= 7

test_and = (7 > 5) and (5 < 7)# True
test_and2 = (7 > 5) and (5 > 7) # False
test_or = (7 > 5) or (5 < 7)# True
test_or2 = (7 > 5) or (5 > 7)# True
test_not = not True #False  

#Conditional statement- if/else
def drink(money):
	if money >= 300:
		return "You've got yourself a drink!"
	else:
		return "No drink for you!"
print(drink(400))
print(drink(200))

def alcohol(age, money):
	if (age >= 18) and (money >= 500):
		print("We're getting you a drink!")
	elif (age >= 18) and (money < 500):
		print("Come back with more money")
	elif (age < 18) and (money >= 500):
		print("We only sell to 18 and above")
	else:
		print("Get a life")
alcohol(18, 500)
alcohol(18, 400)
alcohol(17, 500)
alcohol(17, 400)
new_line()

#List- have square brackets 
movies = ["Bee Keeper", "To Kill a Monkey", "Monkey Man", "Koto Aye"]
print(movies[1])#returns the second item in the list
print(movies[3])
print(movies[1:3])
print(movies[1:])
print(movies[-1])#prints the last item
print(len(movies))
movies.append("Train to Busan")
print(movies)
movies.insert(2, "Alchemy  of souls")
print(movies)
movies.pop()#removes last item
print(movies)
oyinMovies = ["All queens men", "Beauty in black"]
fav_movies = movies + oyinMovies
print(fav_movies)

grades = [["Dayo", 98], ["Gbenga", 70], ["Oyin", 100]]
dy_grade = grades[0][1]
print(dy_grade)
grades[2][1] = 99
print(grades)

#Tuples - have parenthesis () & can't be changed
sch_grades = ("a", "b", "c", "d")
print(sch_grades[1])

#Dictionaries - key/value pairs and written in curly brackets {}
drinks = {
	"fanta": 7,
	"coke": 10,
	"fearless": 8,
	"yogurt": 11
	}
print(drinks)

employees = {
	"finance": ["Dayo", "Gbenga", "Vivian"],
	"IT": ["Oyin", "Linda", "Yahboy"],
	"HR": ["Maureen", "Bob"]
	}
print(employees)
employees['Legal'] =["Mr. Frond"]#adds a new key/value pair\
print(employees)

employees.update({"sale": ["Dante", "Victoria"]})
print(employees)

it_department = employees.get("IT")
print(it_department)




