data = []
count = 0
with open ('original.txt', 'r')as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data)) 
print('資料讀取完畢總共有', len(data), '筆資料')


sum_len = 0
for d in data:
	sum_len += len(d)
print ('留言平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有', len(new), '筆資料小於100的字母')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print ('總共有', len(good), '筆留言有good')

good =  [d for d in data if 'good' in d]
print(good.strip())


#文字記述,查詢單字

wc = {} #word_counter
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
print(len(wc))

for word in wc:
	if wc[word] > 100:
		print(word, wc[word])

while True:
	word = input('請問想查什麼字?')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為:', wc[word])
	else:
		print('並沒有出現過此單字')
print('感謝使用本查詢功能')


