
#this is a repository test


from datetime import datetime

def add_five(a):
	return a + 5

def my_max(num):
	max= num[0]
	for i in num:
		if i > max:
   			max=i
	return max

def my_min(num):
	min= num[0]
	for i in num:
		if i < min:
			min=i
	return min

def has_string(strlist, strings):
	hasString = []
	if strings in strlist:
		hasString.append(strings)
		return hasString

def to_date(dt):
    return datetime.strptime(dt, "%Y-%m-%d").date()

def date_diff(date1, date2):
	a = int(date1[9])
	b = int(date2[9])
	c = (a-b)
	return c

def mayan_days( dt, mdt):
	d0 = datetime.strptime(dt, "%Y-%m-%d").date()
	d1 = datetime.strptime(mdt, "%Y-%m-%d").date()
	delta = d0 - d1
	return delta.days

def contains(a,b):
	if b in a:
		return True

def add_contents(numlist):
	total = 0
	for i in numlist:
		total+=i
	return total

def lookup(dictio,num):
	strreturned = ''
	for i in dictio.keys():
		if dictio[i] == dictio[num]:
			strreturned = dictio[i]
	return strreturned+' mine'		