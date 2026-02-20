#Tuple in python

c=()
print(type(c))


vijay=(1,2,3,4,5,6,7,89,8)
print(max(vijay))
print(min(vijay))
print(len(vijay))
print(sum(vijay))




#tuple - operations 5
'''
1.concat - operation 
2.Itaration - operation 
3.membership - operation 
4.Repetition - operation 
5.slicing - operation 
6.identify - operation
'''
#1.concat - operation 
c1=(1,2,3,'vijay',23,45)
c2=(112,345,65)
print(c1+c2)

#2.Iteration - opertaion
c=(1,2,3,4,5,6,7,8,9)
for i in c:
    print(i)
    
#3.membership - opertion 
c=(1,2,3,4,5,3,2,1) 
print(3 in c)  
print(9 in c ) 

#4.Repetition - opertion 
c=(1,23,54,87,5432,13)
print(c*2)


#5.slicing - operation
c=(1,3,65,78,90,76,445,67,98,34,7900,3)
print(c[2:4:2])

#6.identify - operation
t1=(12,34,44,55)
t2=(12,34,56,54)
print(t1 is t2)
