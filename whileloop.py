choice=int(input("eneter the operation you want to performn\n 1.celcius to fahrenheit\n 2.fahrenheit to celcius\n"))
if choice==1:
	a_celcius=float(input("enter temperature in celcius to convert fahrenheit"))
	f=(a_celcius*1.8)+32
	print(f)
elif choice==2:
	b_fahrenheit=float(input("enter temperature in fahrenheit to convert celcius"))
	c=(b_fahrenheit-32)/1.8
	print(c)
	


