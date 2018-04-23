'''
Created on Feb 14, 2018

@author: Nick Govea
'''

import codecs

array1 = []


string1 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
l = len(string1)
print(l)



for c in string1:
    b =  int(c,16)
    binary_value = bin(b)[2:].zfill(4)
    array1.append(binary_value)
    

regular_text = codecs.decode(string1, 'hex')

print(array1)
#print(regular_text)

z = "".join(array1)

print("This is the hex part " + z)
print(z + '\n')


#'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',
ascii_array = ['21', '22', '23', '24', '25', '26', '27', '28', '29', '2A', '2B', '2C', '2D', '2E', '2F', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3A', '3B', '3C', '3D', '3E', '3F', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4A', '4B', '4C', '4D', '4E', '4F', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5A', '5B']#, '5C', '5D', '5E', '5F', '60',  '61', '62', '63', '64', '65', '66', '67', '68', '69', '6A', '6B', '6C', '6D', '6E', '6F', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7A', '7B', '7C', '7D', '7E', '7F']#'10', '11', '12', '13', '14', '15', '16', '17', '18', "19", '1A', '1B', '1C', '1D', '1E', '1F', '20',
 #]

    
    
for element in ascii_array:
        array2 = []
        array3 = []
        
        count = 0
        while(count < 69):
            letter = element
            array2.append(letter)
            count = count + 1
            
        print(array2)
        
        a = "".join(array2)
        #print(a)

        for n in a:
                b = int(n, 16)
                binary_value = bin(b)[2:].zfill(4)
                array3.append(binary_value)
                
        print(array3)
        m = "".join(array3)
        print("This is the letter " + element + " " + m)
        
        
        #print(z)
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
        
        convert = hex(int(string_array4,2))[2:].zfill(2)
        convert2 = convert.rstrip("L").lstrip("0x")
        print(convert2)
        
        regular= codecs.decode(convert2,'hex')
        print(regular)
        
        print('\n')
        
        
