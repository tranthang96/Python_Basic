# Phương thức với set
# Set không quan tâm đến phần tử trong set - cắt và indexing ko được hỗ trợ
#===== clear======
set1 = {1,2,3,4}
print(set1)
set1.clear()
print(set1)
#===== pop ====
#Công dụng: #Kết quả trả về một giá trị được lấy ra từ Set,
	# đồng thời loại bỏ giá trị đã lấy ra khỏi Set ban đầu

		   #Nếu là set rỗng, sẽ có lỗi
set1 = {1,2,3,4}
set2 = set1.pop() 
print(set1)  #{2, 3, 4}
print(set2)	 #  1

#=========Phương thức remove====
	#Công dụng: Loại bỏ giá trị value ở trong Set. Nếu như value không 
	#ở trong Set, thông báo lên lỗi KeyError.
set1.remove(3) #{2, 4}
print(set1)
#========= Phương thức discard====
# giống với remove, nhưng chuyền giá trị không có trong set thì k bị báo lỗi
set1.discard(7)
print(set1)
# copy 
a = {1, 2}
b = a.copy()
# add
#Cú pháp:
#<Set>.add(value)

#Công dụng: Thêm value vào trong set. Nếu như value đã có trong Set thì bỏ qua
a.add(4)
print(a)
# =========Set không phải là một hash object=====
print(id(a))			#cùng 1 giá trị
a.add(5)
print(id(a))            #cùng giá trị trên 