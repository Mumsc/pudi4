# Python program to illustrate the use 
# of 'is' identity operator 
x1 = 5
print("type of x1: ",x1, type(x1))
if (type(x1) is int): 
	print ("true:IS INT") 
else: 
	print ("false :IS NOT INT")

# Python program to illustrate the 
# use of 'is not' identity operator 
x = 5.2
print("type of x: ",x, type(x))
if (type(x) is not int): 
	print ("true:",x,"IS NOT INT") 
else: 
	print ("false:",x,"IS INT")
