#Set là một container, tuy nhiên không được sử dụng nhiều bằng LIST hay TUPLE.

#Một Set gồm các yếu tố sau:

	#Được giới hạn bởi cặp ngoặc {}, tất cả những gì nằm trong đó là những phần tử của Set.
	#Các phần tử của Set được phân cách nhau ra bởi dấu phẩy (,).
	#Set không chứa nhiều hơn 1 phần tử trùng lặp
	#Set chỉ có thể chứa các hashable object nhưng chính nó không phải là một hashable object. Do 
	# đó, bạn không thể chứa một set trong một set.
#=======Khởi tạo==============
set_1 = {1,334}
set_2 = {'Tran Thang',3,5} # chứa gì cũng dc, nhưng k chứa set, list (k lưu unhashable)
print(set_1)
print(type(set_1))
#=======Không chứa nhiều hơn 1 phần tử giống nhau======
set_3 = {1,1,1,1}
print(set_3)  #relust {1}
# không thể tạo empty (trống ) set
set_4 = {}
print(type(set_4)) # <class 'dict'>
# Sử dụng Set Comprehension
set_5 = {value for value in range(4)}
print(set_5)
# Sử dụng constructor Set : sẽ tạo ra 1 set ..k tạo ra cái khác
set_6 = set((1,3,4,5,3,3,3,3,3))
set_7 = set("Tran Thang")
print(set_6)   # bỏ 3 còn 1
print(set_7)
# tạo empty set
set_8 = set()
print(type(set_8)) #<class 'set'>
#toán tử in
print(1 in {1,2,3,4}) #....
# toán tử - 
	#Công dụng: Kết quả trả về là một Set gồm các phần 
	#  tử chỉ tồn tại trong Set1 mà không tồn tại trong Set2
print ({1,2,4,5,6,7}-{1,2,3})
#..... ============
"""Toán tử &
Cú pháp:
<Set1> & <Set2>

Công dụng: Kết quả trả về là một Set chứa các phần tử vừa tồn 
tại trong Set1 vừa tồn tại trong Set2
"""
print ({1,2,4,5,6,7}&{1,2,3}) #{1,2}
## tương tự toán tử hoặc |
print ({1,2,4,5,6,7}|{1,2,3}) #{1, 2, 3, 4, 5, 6, 7}

# toán tử so ^: Kết quả trả về là một Set chứa tất cả các phần tử chỉ tồn tại ở một trong hai Set
print ({1,2,4,5,6,7}^{1,2,3}) #{3, 4, 5, 6, 7}