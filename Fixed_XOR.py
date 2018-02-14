'''
Created on Feb 13, 2018

@author: Nick Govea
'''


#------ This section converts the Hex strings to binary values and stores the values in array1 and array2

array1 = []
array2 = []
for c in "1c0111001f010100061a024b53535009181c":
    b = int(c, 16)
    binary_value = bin(b)[2:].zfill(4)
    array1.append(binary_value)
    
for n in "686974207468652062756c6c277320657965":
    b = int(n, 16)
    binary_value = bin(b)[2:].zfill(4)
    array2.append(binary_value)



#-------- This section prints out array1 and array2 to verify that binary values are correct.    

print(array1)
print(array2)


#------- This section joins the values in the arrays to form one long string value in each array.

z = "".join(array2)
s = "".join(array1)
print(s)
print(z)

#------- This section outlines the XOR logic, it cycles through each character in each array and stores the respective XOR value in array3.

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
    

#------- This section joins the values in array3 to form one long string of 1's and 0's

string_array3 = "".join(array3)


#----- This section takes the binary XOR string and converts it into a Hex string and prints it out.
                 
print(string_array3) 
print(hex(int(string_array3,2)))