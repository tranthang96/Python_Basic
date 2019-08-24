"""Trong bài này, chúng ta sẽ cùng tìm hiểu những nội dung sau đây

Giới thiệu về Boolean trong Python
Boolean trong các toán tử so sánh
NOT, AND và OR
Các giá trị cũng là các Boolean
Syntaxnic sugar cho việc so sánh trong Python"""

print(233 == 9+3) #False
print ((5*0) != 0) # False . so sánh khác....
# so sánh 2 iterable
print("Thang"=="Thang") # bước tiến hành , so sánnh T=T => a=a.....
	#Lưu ý: Python so sánh các kí tự với nhau bằng cách đưa chúng về dưới dạng số bằng hàm ord. 
	# Bạn có thể tham khảo giá trị của nó trong ASCII Table.
print(ord('A')) # 65 
print("a")
print('a'>'ABC')  # so sánh a>A , a>B , nhưng a>A roài . miễn so sánh đằng sau.
#VD:
print('aaa'<'aaAbc')   #False
print('aaa'<'aaaAbc')  #True
#==== Toán tử is=====
"""
Đây là một toán tử dễ nhầm lần với toán tử ==. Nhưng thật sự thì nó rất đơn giản!

Từ is trong tiếng Việt (ở ngữ cảnh này – ngôn ngữ lập trình Python) có nghĩa là “là”. 
Còn toán tử == có nghĩa là bằng.

Bạn cũng không nên khắt khe việc đúng sai trong ví dụ này, nó chỉ giúp bạn hiểu sự khác
nhau giữa toán tử == và is thôi.

Thế nào là bằng (==)?

Bằng là toán tử so sánh khi nói về mặt giá trị.
Ví dụ: Chiều cao của Tèo bằng chiều cao của Tí
Thế nào là là (is)?

Là (is) trong trường hợp này là liên từ diễn giải định nghĩa, 
tính chất của một sự vật/sự việc/con người.
Ví dụ: Ta không thể nói “Chiều cao của Tèo là chiều cao của Tí” vì của Tèo là của Tèo, 
đâu phải của Tí. Nên nói là “Chiều cao của Tèo là chiều cao của Tèo” hoặc 
“Chiều cao của Tí là chiều cao của Tí”"""
lst = [1, 2, 3]
lst_ = [1, 2, 3]
print(lst_ == lst) 		# True
print(lst_ is lst) 	    # False
_lst = lst
print(_lst is lst)      # True
#Từ đây, ta có thể suy ra một kết luận. 
		#Khi so sánh hai giá trị (đối tượng) bằng toán tử == thì Python 
		#sẽ so sánh bằng giá trị của chúng. Còn nếu so sánh 
		#bằng toán tử is thì Python sẽ lấy giá trị của hàm id để so sánh
print(id(lst))
print(id(_lst))
# Lưu ý toán tử is với python 2x...
	#không nên so sánh 2 số
print(699 is 699)     # True
a = 69999
b = 69999
print(a is b)   # false trong cmd
#=====
a = -5
b = -5
a is b   #True

c = 256
d = 256
c is d   #True

a = 'abc'
b = 'abc'    #True
#Các số từ -5 đến 256 hoặc là một số chuỗi có số kí tự
# dưới 20 thì các biến có cùng một giá trị sẽ có cùng một giá trị trả về từ hàm id.

# NOT, AND và OR================================
"""Thật vậy, các giá trị đều là các boolean. 
Và đương nhiên, bạn có thể chuyển đối chúng thành các Boolean bằng hàm bool.

Mọi giá trị khi chuyển về Boolean đều là True trừ một số trường hợp sau

Số 0  
None
Rỗng

>>> bool(0)
False
>>> bool(None)
False
>>> bool('')
False
>>> bool([])
False
>>> bool(())
False
>>> bool(set())
False
>>> bool({})
False

Thêm một số trường hợp True

>>> bool(1)
True
>>> bool('abc')
True
>>> bool([1, 2, 3])
True

1 là True, 0 là False
Không quá quan trọng, nhưng cũng nên biết

>>> True + 1
2
>>> False + 1
1
>>> int(True)
1
>>> int(False)
0
"""

