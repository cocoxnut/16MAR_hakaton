my_set = [4311, 4321, 5542, 5631, 9871]

for n in my_set:
	n = str(n)
	try:
		b = 0
		for i in range(len(n)):
			if int(n[i]) > int(n[i+1]):
				b+=1
	except:
		pass
	if b == 3:
		print(f'{n} True')
	else:
		print(f'{n} False')

