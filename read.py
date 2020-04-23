data = []
count = 0
with open ('original.txt', 'r')as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data)) 