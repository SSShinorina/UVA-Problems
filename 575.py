while True:
	n = input()
	if n == '0':
		break
	n = n[::-1]
	 
	d = 0
	for i, v in enumerate(n):
		d += int(v)*( (2**(i+1)) - 1)
		
	print(d)
	exit
	exit
exit
