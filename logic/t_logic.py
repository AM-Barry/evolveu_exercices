
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
# def retour_num(a, b):
# 	if a > b :
# 		for n in range(a, b):

	








