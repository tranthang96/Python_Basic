# Giới hạn bởi cặp ngoặc vuông
# Các phần tử của list được cách nhau bởi dấu phẩy , 
# Có khả năng chứa mọi giá trị của đối tượng trong python , bao gồm chính nó

#==========list_basic==============
  #==list rỗng===
abcd = []
#=========khởi tạo===
array = [1,2,3,4,'Tran Thang']
#or
array1 = [[[1,2,3],[4,5]],["hay khong"]]
#===========list Comprehension===================
'''tao ra 1 list . cho i trong khoảng 0-30. i*2'''
a = [i*2 for i in range(30)]
print(a)
print('\n')
'''tao list khó hơn'''
b = [[i,i*3,i+i] for i in range(1,5)]
print(b)
#============constructor list==========
c = list([1,2,3])       #list(interable) interable : là một cấu trúc tập hợp
d = list('Tran Thang')  #hiện thị danh sách từng giá trị trong biến ['T', 'r', 'a', 'n', ' ', 'T', 'h', 'a', 'n', 'g']
print(c)
print(d)
#====== toán tử cộng list======================
a=[1,2]
a+=['one', 3] #[1, 2, 'one', 3]
print(a) # 1 chuỗi + list không được. vd a = "thang"
#======= nhân list =========
a = [3,4]
a = a*2   #[3, 4, 3, 4]
print(a)  #không thể nhân 2 list với nhau 
#===== toán tử in=====
"""kiểm tra phần tử có nằm trong list ko"""
a=[1,2,3,4,5,6]
b= 1 in a #true
#============Indexing và cắt List trong Python============
a = [1,2,3,4,'Tran Thang',[6,1]]
b = a[0]               #lấy phần tử a0
d = a[1:3]             #không lấy thằng 3
c = a[5][0]
f = a[-1]
print(b)
print(d)
print(c)
print(f)
#=========thay đổi một phần tử trong list=====
'''gọi nó ra roài gán cho nó giá trị mới'''
a[0]=44
print(a[0])
print(a)
#===============================================