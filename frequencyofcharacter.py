


test_str = "mycaptain"

 
all_freq = {} 

for i in test_str: 
	if i in all_freq: 
		all_freq[i] += 1
	else: 
		all_freq[i] = 1
print ("Count of all characters in mycaptain  is :\n "
										+ str(all_freq)) 
