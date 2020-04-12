testcase = input()
items = []
for i in range(int(testcase)):
	season, regular = input().split()
	season = int(season)
	regular = int(regular)
	item = 0
	while season + regular >= 12 and season >= 5:
		if regular % 7 == 0 and regular >= 7:
			regular -= 7
		elif regular % 7 != 0 and regular >= 7:
			regular -=7
		elif regular < 7:
			regular = regular
		season -= 5
		item += 1
		print(regular)
	# print(season, regular)
	items.append(item)

for i in items:
	print(i)
