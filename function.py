
# practicing functions/TDD

#function add two numbers
def add_numbers(n1, n2):
	#return 0
	return n1 + n2

#function divide two numbers
def div_numbers(n1, n2):
	#return 0
	return n1 / n2

#function calculate payment based on hours and rate
def payment(hours, rate):
	#return 0
	return hours*rate

#function occurences of a number in an array
def count_occur(arr1):
	#return 0 
	dictArr = {}
	for i in arr1:
		if i not in dictArr:
			dictArr[i]=0
		dictArr[i] += 1
	return dictArr

#function lookup provinces by Province code
def lookup_prov(prov, codepro):
	#return 0
	if codepro in prov.keys():
		print('Welcome to', prov[codepro])
		return codepro
	else:
		return 'Not in list'

