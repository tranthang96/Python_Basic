#sự khác biệt giữa hashale và unhashable
# hàm id : trả về một số nguyên int hoặc long int, 
# giá trị này là một giá trị duy nhất và không thay suốt chương trình (trả về địa chị của giá trị trong bộ nhớ)
b = 'Kteam'  #giá trị id sẽ thay đổi
c = 6		 # giá trị id ko thay đổi
a = id(b)
d = id(c)
print(a)
print(d)
#===== toán tử trong python 
#VD 
n = 69
print (n)
print(n+1)
print(n.__add__(1)) # n+1
print(n.__sub__(1)) # n-1
print(n.__mul__(2)) # n*2
print(n.__radd__(1)) # 1+ n ----right add. 
print(n.__rsub__(1)) # 1-n
print(n.__neg__())   # -n
# mỗi toán tử của mỗi đối tượng sẽ có một phương thức đi kèm, khác biệt giữa giữa has object và unhash object

"""
#=======================
Với hash object, bạn không thể thay đổi nội dung của nó.
Do đó, Python sẽ xin đủ khoảng trống để lưu trữ dữ liệu của bạn, 
không nhiều hơn và cũng không ít hơn. Giúp không hoang phí bộ nhớ của bạn. 
Thế nên, khi bạn cộng thêm một thứ gì đó, Python không biết nhét cái thứ bạn 
muốn cộng vào chỗ nào. Nên nó đành cuốn gói đi ra chỗ đó, 
tìm chỗ mới thoáng có đủ khoảng trống.
#======================
#Còn với unhash object. Là một đối tượng bạn thay đổi được nội dung, vì thế, 
Python luôn xin dư bộ nhớ để chừa chỗ cho các giá trị tiếp theo bạn có thể thêm vào. 
đã đề cập đến việc Tuple chiếm ít dung lượng hơn 
List vì Tuple là hash object
"""

