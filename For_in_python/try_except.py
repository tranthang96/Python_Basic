#for trong python
length = 3
iter_ = (x for x in range(length)) #0,1,2
c = 0
while 1:
    print(next(iter_))
    c+=1
    try: 
    	print(next(iter_))
    except StopIteration:     #Bắt lỗi
    	break