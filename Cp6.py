m = int(99999999)
x=int(0)
number = int(0)
print('Задайте размер массива')
try:
	a=int(input())
	array=[0]*a
	for i in range(a):
		array[i]=int(input('Введите целочисленный элемент массива '))
	print('Введите дельта ')
	d = int(input())
except ValueError:
	print('Задано недопустимое значение ')
	m = int(99999999)
	x=int(0)
	number = int(0)
	print('Задайте размер массива')
	exit()
else: 
	for i in range(a):
		if array[i]<m:
			m = array[i]
for i in range(a):
	if (array[i]-m == d) | (array[i]+m == d):
		x=1
		number+=1
if x==0:
	print('Нет подходящих элементов массива, либо дельта меньше 0')
else:
	print('Количество элементов ', number)