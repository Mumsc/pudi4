def overlapping(list1,list2): 
	c=0
	d=0
	for i in list1: 
		c+=1
	for i in list2: 
		d+=1
	for i in range(0,c): 
		for j in range(0,d): 
			if(list1[i]==list2[j]): 
				return 1
	return 0

# creating an list 1
list1 = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements for list 1: ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    list1.append(ele) # adding the element 
      
print(list1)

# creating an list 2
list2 = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements for list2: ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    list2.append(ele) # adding the element 
      
print(list2)

if(overlapping(list1,list2)): 
	print("overlapping") 
else: 
	print("not overlapping")

