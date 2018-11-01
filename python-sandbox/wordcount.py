#coding: utf-8

# from collections import Counter

# m = raw_input().split()
# count = Counter(m)
# for word, cnt in count.most_common():
# 	print word, cnt.sorted()

text = raw_input().rstrip().split(' ')

length = len(text) 

a=[[text[0],0]]
# b=0

for i in range(length):
	# c=b
	for j in range(len(a)):
		if text[i]==a[j][0]:
			a[j][1]+=1
			# b+=1
			break
		elif j==(len(a)-1):
			a.append([text[i],1])
			
for i in range(len(a)):
	print a[i][0],a[i][1]



































