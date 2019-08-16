#Generator là iterator, một dạng của iterable nhưng khác ở chỗ bạn không thể tái 
	#sử dụng. Vì sao lại như vậy? Generator không lưu trữ tất cả các giá trị của bạn 
	# ở bộ nhớ, mà nó sinh ra lần lượt
kteam_gen = (value for value in range(3))
for value in  kteam_gen:
	print(value)
#Bạn thấy đấy, không có giá trị nào được in ra.
 #Bởi vì khi nó sinh ra giá trị đầu tiên là 0, khi bạn kêu nó sinh tiếp giá trị 1, 
 #nó sẽ vứt bỏ giá trị 0 để nhường chỗ cho giá trị 1, và nếu bạn tiếp tục yêu cầu 
 #sinh thêm giá trị nó sẽ lại tiếp tục công việc như cũ cho tới khi kết thúc.
def square(lst):
	for num in lst:
		yield num**2

kteam_gen = square([1, 2, 3])
for value in kteam_gen:
	print(value)
