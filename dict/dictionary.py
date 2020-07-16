#Write a Python script to merge two Python dictionaries.
def merge(dict1,dict2):
	return(dict2.update(dict1))

dict1={"name":"victor", "age":20 ,"gender":"male"}
dict2={"greeting":"hello","n":"victor"}
merge(dict1,dict2)
print(dict2)