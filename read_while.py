data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1                                            # count = count + 1
		if count % 100000 == 0:
		    print(len(data))
print('Finish reading the file, it has', len(data), 'datas' )
print(len(data[0]))                                           # print length of the first review stream

sum_len = 0                                                   # calculate average words of all review stream
i = 0
while i <= 999999:
    sum_len += len(data[i])
    i += 1
print('The average', sum_len/1000000)