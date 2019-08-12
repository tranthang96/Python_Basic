#ma tran trong python
#list chứa một list khác 
a=[[1,2,3],[4,5,6]]
print(a)
print(a[0])
print(a[1])
print(a[1][2])

#+++++++lưu ý+++++++
	#không được gán list này sang list khác nếu không có mục đích++
b=[1,2,3]
c=b
print(b)
print(c)
c[0]='Thang'
print(b)
print(c)      #giá trị của b thay đổi b[0]='Thang'
  # khi gán như vậy thì 2 giá trị cùng trỏ tới 1 nơi...}
#+++++list(): có tác dụng copy không làm thay đổi giá trị với 1 mảng vd a[0] 
#. còn với giá trị thuộc a[0][1] thì thay đổi cả mảng ban đầu++++
d=list(b)
d[0]=123
print(b)
print(d)