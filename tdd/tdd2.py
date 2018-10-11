
from datetime import datetime

def add_five(a):
	return a + 5

def my_max(num):
	if len(num) != 0:
		max= num[0]
		for i in num:
			if i > max:
   				max=i
		return max
	return None

def my_min(num):
	if len(num) != 0:
		min= num[0]
		for i in num:
			if i < min:
				min=i
		return min
	return None

def has_string(strlist, strings):
	hasString = []
	if strings in strlist:
		hasString.append(strings)
		return hasString

def to_date(dt):
    return datetime.strptime(dt, "%Y-%m-%d").date()

def date_diff(dt1, dt2):
	d1 = datetime.strptime(dt1, "%Y-%m-%d").date()
	d2 = datetime.strptime(dt2, "%Y-%m-%d").date()
	if d1 > d2 :
		delta = d1 - d2
		return delta.days
	else :
		delta = d2 - d1
		return delta.days
	return delta.days

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
	if len(dictio) != 0:
		if num in dictio:
			return dictio[num] + ' mine'
		return ' mine'
	return 'Empty dictionary'