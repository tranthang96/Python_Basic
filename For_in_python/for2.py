"""
Kiểu dữ liệu range (dãy số)
Bạn gặp kiểu dữ liệu này suốt các phần liên quan đến comprehension hoặc là liên quan đến iterator object.

Đây là một kiểu dữ liệu rất đặc biệt vì ta có thể lấy nhiều giá trị từ nó nhưng bản 
chất thì nó không lưu giữ những giá trị mà chúng ta lấy. Trước khi đến với điều thú vị này, 
chúng ta cùng ngó tổng quát về kiểu dữ liệu này.

Chúng ta có hai cách khởi tạo.

Cách khởi tạo thứ nhất
Cú pháp:  
range(stop)

Với cách này, ta sẽ tạo một dãy số bắt đầu bằng số 0 và kết thúc là stop – 1. 
Dãy số này là một cấp số cộng với công sai là 1."""
i = range(3) 
print(type(i))    #<class 'range'>
#range có hỗ trợ indexing
print(i[1])

# khởi tạo cách 2 : range(start, stop[, step])
a=list(range(0,8,2))      # đến start, start+step : stop - step
print(a)
#
lst = [5, (1, 2, 3), {'abc', 'xyz'}]
for i in range(len(lst)):
	print(lst[i])
#Sự khác nhau giữa sequence scan và indexing scan
"""
Trong bài trước, bạn thấy rằng ta không cần dùng tới hàm range vẫn có thể duyệt hết các 
phần tử của một List. Vậy điều gì khiến chúng ta đôi lúc phải dùng tới hàm range để xử lí một List?

Đó là khi ta cần update (cập nhật) List. Hãy xem hai ví dụ sau đây:
"""
#Đầu tiên là sequence scan
lst = [1, 2, 3]
for value in lst:
	value += 1
print(lst)          #giá trị không thay đổi
# indexing scan
for value in range(len(lst)):
	lst[value] +=1
print(lst)          # giá trị đã thay đổi
