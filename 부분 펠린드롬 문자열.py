string = input()
substrings = []

for i in range(len(string)): # i = 0, 1, 2, 3
	substring = ''
	for n in range(i, len(string)): # n = 0~3, 1~3, 2~3, 
		substring += string[n]
		substrings.append(substring)
# print(substrings)

palindromes = []
for i in substrings:
	if len(i) == 1:
		palindromes.append(i)
	elif i == i[::-1]:
		palindromes.append(i)
# print(palindromes)

length = []
for i in palindromes:
	length.append(len(i))
print(max(length))	
	
