'''
Created on Feb 13, 2018

@author: Nick Govea
'''


array1 = []
array2 = []
for c in "1c":
    b = int(c, 16)
    binary_value = bin(b)[2:].zfill(4)
    array1.append(binary_value)
    
for n in "68":
    b = int(n, 16)
    binary_value = bin(b)[2:].zfill(4)
    array2.append(binary_value)

    
print(array1)
print(array2)
z = "".join(array2)
s = "".join(array1)
print(s)
print(z)

array3 = []
for a,d in zip(s,z):
      
    if a=='0' and d == '0':
        print("output=0")
    if a=='0' and d =='1':
        print("output=1")
    if a=='1' and d=='0':
        print("output=1")
    if a=='1' and d=='1':
        print("output=0")
    


                 
print(array3) 