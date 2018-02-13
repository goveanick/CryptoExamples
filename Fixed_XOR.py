
array = []
for c in "1c01"
	b = int(c,16)
	print(b)
	binary_value = bin(b)[2:].zfill(4)
	array.append(binary_value)

print(array)
s = "".join(array)
print(s)