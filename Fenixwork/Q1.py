

def count_no(input_list):

	count=0
	print(input_list)

	# using insertion sorting algorithm
	for i in range(1, len(input_list)):
	 
	        key = input_list[i]
	        j = i-1
	        if key < input_list[j]:
	        	count+=1
	        while j >=0 and key < input_list[j] :
	                input_list[j+1] = input_list[j]
	                j -= 1
	        input_list[j+1] = key
	        print(input_list)
	        

	print(input_list)
	print(count)


T=int(input())
if T>=1 and T<=100:
	input_list=[]
	
else:
	print("No. of test cases is not more than 100")


for i in range(T):
	sentence=input()
	if all(x.isalpha() or x.isspace() for x in sentence):
		print("")
	else:
		print("Only alphabetical letters and spaces: no")
		break
	if len(sentence)>100:
		print("Each ​name  ​will ​ ​contain ​ ​at ​ ​most ​ ​100 ​ ​characters.")
		break
	t=' ','\t','\n','\r'
	if sentence.startswith(t) or sentence.endswith(t):
		print("name ​start with space ​or ​end ​​with ​​a ​​space.")
		break

	if sentence in input_list:
		print("name ​appear more ​​than ​​once ​​in ​​the ​​same ​​test ​​case")
		break
	input_list.append(sentence)

count_no(input_list)