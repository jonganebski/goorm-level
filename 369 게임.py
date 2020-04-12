endnum = int(input())
clap = 0
for n in range(1, endnum):
	stringnum = str(n)
	# print(stringnum)
	for s in stringnum:
		# print(s)
		if s == '3' or s == '6' or s == '9':
			clap += 1
			# print('clap')
print(clap)
