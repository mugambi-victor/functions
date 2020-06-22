#Write a Python program to remove the characters which have odd index values of a given string.
x="victor"
for i in range(len(x)):
	if i%2==0:
		print(x[i],end=',')