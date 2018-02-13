'''
Created on Feb 8, 2018

@author: Nick
'''

import codecs

x = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

regular_text = codecs.decode(x, 'hex')
encodes_to_base64 = codecs.encode(regular_text, 'base64')

encode = encodes_to_base64.decode()
regular_text = regular_text.decode()

print(regular_text)
print(encode)
