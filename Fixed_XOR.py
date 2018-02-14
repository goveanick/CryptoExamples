'''
Created on Feb 13, 2018

@author: Nick Govea
'''


array1 = []
array2 = []
for c in "1c0111001f010100061a024b53535009181c":
    b = int(c, 16)
    binary_value = bin(b)[2:].zfill(4)
    array1.append(binary_value)
    
for n in "686974207468652062756c6c277320657979":
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
    	n = "0"
        #print("output=0")
    if a=='0' and d =='1':
    	n = "1"
        #print("output=1")
    if a=='1' and d=='0':
    	n = "1"
        #print("output=1")
    if a=='1' and d=='1':
    	n = "0"
        #print("output=0")

    array3.append(n)
    

string_array3 = "".join(array3)


                 
print(string_array3) 
print(hex(int(string_array3,2)))
#print(hex(int(string_array3))