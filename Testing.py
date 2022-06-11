connect = True

while connect == True:
	number = input('Число: ')
	procent = input('Процент: ')
	while type(number) != int:
		try:
			number = int(number)
			procent = int(procent)
		except ValueError:
			print('Вводи целочисленные значения!')
			number = input('Число: ')
			print()
	      procent = input('Процент: ')
			print()

	while type(procent) != int:
		try:
			procent = int(number)
			procent = int(procent)
		except ValueError:
			print('Вводи целочисленные значения!')
			number = input('Число: ')
			print()
	      procent = input('Процент: ')
			print()
	
	finish = number / 100 * procent

	print('Ваш ответ: ', float(finish))

