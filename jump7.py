 for i in range(1,101):
	if i % 10 == 7 or i % 7 == 0 or int(i / 10) == 7 :
	    i = i + 1
	    continue
	else:
		print(i)
             i = i + 1  
