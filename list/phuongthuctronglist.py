#phương thức trong list
#---- phương thức count : đếm số lần xuất hiện thằng con trong nó---
a = [1,2,3,4,[1,2,3]]
b = a.count(1)
print(b) # = 1
#--- phương thức index : trả về vị trí xuất hiện
c = a.index(3)
print(c) # = 2
#--- phương thức copy : trả về 1 list tương tự . tạo ra 1 bản sao
d = a.copy()
print(a)
print(d)  # nhân bản. gốc thay đổi nhân bản k thay đổi/...
#---- clear : xoá mọi phần tử trong list
e = a.clear()      
print(a)           # a =[]
print(e)		   # e = None 
#---- phương thức append : thêm phần tử vào list
a = [1,2,3,4]
print(a)
a.append([3,4])
print(a)              # [1, 2, 3, 4, [3, 4]]
#--- phương thức extend : lấy phần tử nhỏ thêm vào..
a = [1,2,3,4]
a.extend([5,6])
print(a)  #[1, 2, 3, 4, 5, 6]
a.extend([5,6,[7,8]])
print(a)   #[1, 2, 3, 4, 5, 6, 5, 6, [7, 8]]
#---- phương thức insert(i, [phần tử]) . thêm phần tử vào vị trí i
       #nếu i lớn hơn số phần tử list. nó thêm vào cuối
a.insert(3,[2,4])
print(a) #[1, 2, 3, [2, 4], 4, 5, 6, 5, 6, [7, 8]]

#---pop: bỏ đi phần tử thứ i trong list
c = a.pop(3)
print(a)  #[1, 2, 3, 4, 5, 6, 5, 6, [7, 8]]
print(c)  #[2, 4]
#--- remove(x) xoá đi phần tử đầu tiên là x. nếu x không có trong list nó bị lỗi
a.remove(1) 
print(a) #[2, 3, 4, 5, 6, 5, 6, [7, 8]]
#--- đảo ngược list : reverse()---------
a.reverse()
print(a) #[[7, 8], 6, 5, 6, 5, 4, 3, 2]
#--- sắp xếp list: sort-----------
a = [9,5,8,2,9]
a.sort()
print(a) #[2, 5, 8, 9, 9] , không chứ [lồng: []]
		#lưu ý: phải cùng kiểu dữ liệu..
a = ["a","r","a","f","t","b","s"]
a.sort()
print(a)
a = [9,5,8,2,9]
a.sort(reverse=True) # sắp xếp xong r đảo : True, False thì k đảo
print(a) #[9, 9, 8, 5, 2]