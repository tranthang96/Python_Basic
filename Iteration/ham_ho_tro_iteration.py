#Hàm hỗ trợ cho iteration 
# ++++Lưu ý ++++
"""
	Các hàm này buộc phải lấy giá trị iterable để xử lý, do đó nếu đưa vào 1 iterable thì ta không
	thể sử dụng iterable đó nữa
"""
#--- hàm tính tổng sum---
	# trả về giá trị của iterable và iterable chỉ chứa giá trị là một số. còn start chính là giá 
	# trị ban đầu, có nghĩa là cộng từ start lên, mặc định là 0
a = sum([1,2,3],10)   # cộng với giá trị ban đầu là 10 
print(a) 
#  print(next(a)) ==> không được nữa vì đã đưa con trỏ về cuối
#=====Tìm Max====
'''Cú pháp:
max(iterable, *[, default=obj, key=func])

Công dụng: Nhận vào một iterable.Tìm giá trị lớn nhất bằng key (mặc định là sử dụng operator >). 
Default là giá trị muốn nhận về trong trường hợp không lấy được bất kì giá trị nào trong iterable.

Dấu * chính là kí hiệu yêu cầu keyword-only argument. '''
it_1 = (i for i in range(5))
print(it_1)     #<generator object <genexpr> at 0x032AAAF0>
print(max(it_1, default="giá trị max không có"))  # 4
print(max([], default="giá trị max không có")) 	  # 
## tương tự với hàm min
print(min(it_1, default="giá trị max không có")) # do con trỏ ở cuối r
it_1 = (i for i in range(5))
print(min(it_1, default="giá trị max không có")) # trả về 0 
#======= Hàm sắp xếp =======
"""
Hàm sắp xếp – sorted
Cú pháp:
sorted(iterable, /, *, key=None, reverse=False)

Công dụng: Giống với phương thức sort của List object.

Ví dụ: """
it_1 = (7,8,6,4,9,10,33,3,2,4)
print(sorted(it_1))
it_1 = (7,8,6,4,9,10,33,3,2,4)
print(sorted(it_1,reverse=True))
