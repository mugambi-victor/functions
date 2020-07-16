 #syntax for py dictionaries
thisdict={"brand":"ford","model":"mustang","year":2010 }
print(thisdict)
#accessing a dictionary element
x=thisdict["model"]
#prints the value of the model key(i.e mustang)
print(x)
#merging two dictionaries
dict2={"name":"victor", "age":20, "gender":"male"}
def merge(thisdict,dict2):
	return(dict2.update(thisdict))
merge(thisdict,dict2)
print(dict2)