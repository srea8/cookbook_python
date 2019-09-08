##如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。 
###那么怎样才能从这个可迭代对象中解压出 N 个元素出来##

####   *的使用方法   ####
####  python3才能使用，python2不能使用   ####


###基本规则###
grades = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = grades
print (name)
print (email)
print (phone_numbers)


###list###
*trailing,current = [10,9,8,7,6,5,4,3,2,1]
print (trailing)



###*号调用###
records = [
	('foo',1,2),
	('bar','bar'),
	('foo',3,4),
]

def do_foo(x,y):
	print('foo',x,y)

def do_bar(s):
	print('bar',s)

for tag,*args in records:
	if tag == 'foo':
		do_foo(*args)
	if tag == 'bar':
		do_bar(*args)


###split划分###
line = 'nobody:nobody1:nobody2:nobody3:nobody4'
one,two,*three,four = line.split(':')
print (one)
print (four)


###递归调用###
items = [1,2,3,4,5,6,7,8,9,10]
def sum(items):
	head,*tail = items
	return head + sum(tail) if tail else head

print (sum(items))