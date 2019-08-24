# được giới hạn bời cặp ngoặc ()
# các phần tử của tuple được phân cách nhau bởi dấu ,
# tuple có khả năng chứa mọi giá trị
# tốc độ truy xuất của tuple nhanh hơn list
# dung lượng chiếm bộ nhớ nhỏ hơn list, bảo vệ dữ liệu của bạn sẽ không bị thay đổi
# có thể dùng làm key của dictionary
# toán tử giống với chuỗi
# 

#==============khởi tạo tuple=========
tup = ((13,4),1,2,3,4,5)
print(tup)
#lưu ý
tuple1 = (1) #hiểu là một số nguyên , nếu có 1 phần tử (1,) vì hiểu ngoặc trong toán tử
#====Với Tuple thì khái niệm Comprehension này không được áp dụng=====
tuple2 = (i for i in range(10)) #<generator object <genexpr> at 0x0106AAF0>
#==== comprehension hay
tuple3 = (i for i in range(10) if i%2==0)
print(tuple2)
 	#muốn sử dụng
e = tuple(tuple2)
f = tuple(tuple3)
print(e)
print(f)   #(0, 2, 4, 6, 8)
#=======================
d = tuple('Tran Thang')  #hiện thị danh sách từng giá trị trong biến ('T', 'r', 'a', 'n', ' ', 'T', 'h', 'a', 'n', 'g')
print(d)

