'''
Created on Feb 14, 2018

@author: Nick Govea
'''

# I am entering these comments bc I am tryng to push from my PC

import codecs

array1 = []
array2 = []
array3 = []
string1 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
l = len(string1)
print(l)



for c in string1:
    b =  int(c,16)
    binary_value = bin(b)[2:].zfill(4)
    array1.append(binary_value)
    

regular_text = codecs.decode(string1, 'hex')

print(array1)
print(regular_text)

z = "".join(array1)

print("This is the hex part " + z)






count = 0
while(count < 69):
    letter = '66'
    array2.append(letter)
    count = count + 1
    
print(array2)

a = "".join(array2)
print(a)




for n in a:
    b = int(n, 16)
    binary_value = bin(b)[2:].zfill(4)
    array3.append(binary_value)
    
print(array3)
m = "".join(array3)
print("This is the letter E " + m)


print(z)
print(m)



array4 = []

for p,q in zip(m,z):
    
    if p=='0' and q=='0':
        n = "0"
        #print("output=0")
    if p=='1' and q=='0':
        n = "1"
    if p=='0' and q=='1':
        n = "1"
    if p=='1' and q=='1':
        n="0"
        
    array4.append(n)
print(array4) 

string_array4 = "".join(array4)

print(string_array4)
print(hex(int(string_array4,2)))

almost = '7d5151555750591e737d194d1e5257555b1e5f1e4e514b505a1e51581e5c5f5d5150'

regular= codecs.decode(almost,'hex')
print(regular)

'''
    
#string_array4 = "".join(array4)

#print(string_array4)
'''