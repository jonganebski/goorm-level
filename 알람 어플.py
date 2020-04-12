string = input() # abcda
K = int(input())

substrings = []
n = len(string) # 5
for i in range(n): # i = 0 1 2 3 4
	for j in range(n-i): # j = 1 2 3 4 5 
		substrings.append(string[j:j+i+1]) # [1:2] [2:3] ...
		# [1:3] [2:4]...
		#
print(substrings)
substrings = list(dict.fromkeys(substrings))
substrings.sort()
print(substrings)	
print(substrings[K-1])
