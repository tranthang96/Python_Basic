# phương thức với tuple
# giống vs tuple
# khi nào nên chọn tuple thay cho list
	# tuple không cho phép thay đổi nội dung bên trong
	# tốc độ tuple nhanh hơn list
	# dung lượng trong bộ nhớ nhỏ hơn list (chiếm trên ram)
	# bảo vệ dữ liệu sẽ không bị thay đổi
	# có thể dùng làm key dictionary
#VD:
#---- phương thức count : đếm số lần xuất hiện thằng con trong nó---
a = (1,2,3,4)
b = a.count(1)
print(b) # = 1