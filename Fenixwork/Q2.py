import itertools
from itertools import *

def count_no(word):
	letters=[''.join(i) for i in itertools.product(word,repeat=len(word))]
	# print(letters)


	count=0
	extra=[]

	for i in letters:
		temp=0
		br=0
		if i not in extra:
			extra.append(i)
		else:
			break	
		
		for ch in i:
			if br==0:
				if temp==0:
					if ch==word[temp] or ch==word[temp+1]:
						temp+=1
					else:
						br+=1
						break
				
				elif temp>0 and temp<len(i)-1:
					if ch==word[temp] or ch==word[temp+1] or ch==word[temp-1]:
						# print(count)
						temp+=1
					else:
						br+=1
						break
				elif temp==len(word)-1:
					if ch==word[temp] or ch==word[temp-1]:
						# print(count)
						break
					else:
						br=+1
						break
			
		if br==0:
			count+=1

	return count


T=int(input())
if T>=1 and T<=100:
	for j in range(T):

		word=input()
		if len(word)>=1 and len(word)<=5:
			count=count_no(word)
			print("Case #",T,":",count)
		else:
			print("Please take maximum length of string 5")
else:
	print("No. of test cases is not more than 100")