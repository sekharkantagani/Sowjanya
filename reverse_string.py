str="Rithanya ammu"
lst=str.split()
rev_str=[]
for i in lst:
	i=i[::-1]
	rev_str=rev_str+i
	res=" ".join(rev_str)
print(res)
