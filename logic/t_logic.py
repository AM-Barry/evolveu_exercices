
'''4. What a function is :a function a method or a block of code 
    The two things you can do to a function: define it and call it
    What the input / output and name i: input()-->are parameters a function receive--> 
    output -->what a function returns
    Describe how Python knows how many lines are in a function: by indentating
    5. Describe how to execute a function : by calling it
'''
# 7 math operators funtions
def dummy_tests(a,b):
	#return 0
	ad = a + b
	su = a - b
	mu = a * b
	di = a / b
	mo = a % b
	fl = a // b
	ex = a ** b
	return ad, su, mu, di, mo, fl, ex

# modulo function
def mod(a, b):
	#return 0
	return a % b

# floot function
def flo(a, b):
	#return 0
	return a // b

# exponent function
def expo(a, b):
	#return 0
	return a ** b

# function largest number
def largest_num(a, b, c):
	#return 0
	if (a > b) and (a > c):
 		return a
	elif (b > a) and (b > c):
		return b
	else:
		return c

# function to return list of numbers
# using while loop
def retour_num(a, b):
	resul = []
	i = 1
	if a<b:
		r = range(a,b)
		while i < len(r):
			resul.append(r[i])
			i+=1
		return resul
	elif a == b:
		return 'you entered same numbers'
	else:
		r = range(b,a)
		while i < len(r):
			resul.append(r[i])
			i+=1
		return resul

#using for loop
def retour_num(a, b):
	resul = []
	i = 1
	if a<b:
		r = range(a,b)
		for i in range(i,len(r)):
			resul.append(r[i])
			i+=1
		return resul
	elif a == b:
		return 'you entered same numbers'
	else:
		r = range(b,a)
		for i in range(i,len(r)):
			resul.append(r[i])
			i+=1
		return resul

#odd numbers function
def odd_number(a, b):
	resul = []
	i = 1
	if a<b:
		r = range(a,b)
		for i in range(i,len(r)):
			if r[i] % 2 != 0:
				resul.append(r[i])
				i+=1
		return resul
	elif a == b:
		return 'you entered same numbers'
	else:
		r = range(b,a)
		for i in range(i,len(r)):
			if r[i] % 2 != 0:
				resul.append(r[i])
				i+=1
		return resul

#even numbers function
def even_number(a, b):
	resul = []
	i = 1
	if a<b:
		r = range(a,b)
		for i in range(i,len(r)):
			if r[i] % 2 == 0:
				resul.append(r[i])
				i+=1
		return resul
	elif a == b:
		return 'you entered same numbers'
	else:
		r = range(b,a)
		for i in range(i,len(r)):
			if r[i] % 2 == 0:
				resul.append(r[i])
				i+=1
		return resul

# List the 6 comparison operators python has:
# <, >, <=, >=, ==, !=

#Write a single function that shows how to use the 6 comparison operators. 
def comp_operators(a, b):
	if a < b:
		print(b ,'greater than', a)
	elif a > b:
		print(a ,'greater than', b)
	elif a == b:
		print(a ,'equal', b)
	elif a != b:
		print(a ,'diffrent to', b)
	elif a <= b:
		print(a ,'less than or greater than', b)
	else:
		print(b ,'less than or greater than', a)

#largest number of a list function
def content_list(mylist):
	return mylist

def largest_list(mylist):
	max = 0
	if len(mylist) != 0:
		for i in mylist:
			if i > max:
				max = i
		return max
	else:
		return 'empty list'

#longest character from a list function
def longest_charac(mylist):
	count=0
	if len(mylist) != 0:
		for i in mylist:
			if len(i) > count:
				count = len(i)
				word = i
		return ('the logest string is: ' + word)
	else:
		return'empty list'








