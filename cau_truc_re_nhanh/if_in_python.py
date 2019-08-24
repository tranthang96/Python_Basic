# if trong python
# khối xác định nằm chung 1 dòng tab...
#if expression:

    # If-block
a = 0
b = 3
if a<1:
	print('a nhỏ hơn 1')
	print("a có gia tri nho hon 0")
	if b>0:
		print("b lớn hơn 0")
print("kết thúc if")
#+========if - elif======
a=3 
if a>5: #false, tiếp tục nhảy đến elif tiếp theo
	print("a lớn hơn 5")
elif a>4:  #false, tiếp tục nhả đến elif
	print("a lớn hơn 4")
elif a==3:	#true, thoát khoải khối lệnh , k thực hiện if sau đó kể cả đúng
	print("a bằng 3")
elif a<4:			# không được thực hiện vì bên trên đã đúng
	print("a nhỏ hơn 4") 
print('-------kết thúc if-elif nhiều trường hợp')
# if---- eles----
if(a==4):
	print("a = 3")
else:
	print("a khác 4")


