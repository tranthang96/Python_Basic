"""Chúng ta sẽ cùng tìm hiểu phần cấu trúc trước:

for variable_1, variable_2, .. variable_n in sequence: (sequence: danh sách nào đó)

    # for-block

Sequence ở đây là một iterable object (có thể là iterator hoặc là một dạng object cho phép 
sử dụng indexing hoặc thậm chí không phải hai kiểu trên).
Lưu ý: Nếu sequence là một iterator object thì việc dùng vòng lặp duyệt qua cũng sẽ tương 
tự như bạn sử dụng hàm next.

Ở cấu trúc vòng lặp này, bạn có thể for bao nhiêu biến theo sau cũng được. 
Nhưng phải đảm bảm một điều rằng, nếu bạn for với n biến thì mỗi phần tử trong 
sequence cũng phải bao gồm n (không lớn hơn hoặc nhỏ hơn) giá trị để unpacking (gỡ)
 đưa cho n biến của bạn.

Bạn đưa vào vòng for gồm 3 biến h, k , t.

Bây giờ là nói về cách hoạt động của vòng lặp for này.

Bước 1: Vòng for sẽ bắt đầu bằng cách lấy giá trị đầu tiên của sequence.

Bước 2: Giá trị đầu tiên này có 3 giá trị. Bạn đưa vào 3 biến. Kiểm tra hợp lệ.

Bước 3: unpacking 3 giá trị này và lần lượt gán giá trị này cho ba biến h, k, t.

Dưới đây là một ví dụ unpacking:"""
h = (1,2,3)     #khởi tạo 1 tuple
print(type(h))

h, k, t = (1,2,3) # unpacking

# VD
iter_ = (x for x in range(3))
for value in iter_:            # với mỗi phần tử nằm trong danh sách này thực hiện đoạn code , coi như value = next(iter_)
	print("giá trị:",value)
# Sử dụng vòng lặp để xử lí các iterator và Dict
Hust = {"name": "Tran Thang", "MSSV": "CB180122"}
print(Hust.items())
'''Dict-items không phải là một iterator object. Cũng không phải là một object cho phép bạn indexing. 
Nhưng nó vẫn là một iterable, nên ta có thể dùng một constructor nào đó để biến đổi nó về 
một thứ dễ xem xét hơn. Chẳng hạn thế này.'''
list_value = list(Hust.items())
print(list_value)
print(list_value[0])
print(list_value[1])
# ==> cách có vòng lặp duyệt 1 dict
for var1,var2 in list_value:
	print(var1,var2)
#====> Hoặc
for var1,var2 in Hust.items():
	print(var1,var2)
#=======break===
for var1,var2 in Hust.items():
	if var1 == "MSSV":
		break
	print(var1,var2)
for char in "TranViet Thang":
	if char == " ":       # gặp khoảng trắng break.
		break
	else:
		print(char)
for char in "TranViet Thang":
	if char == " ":       # gặp khoảng trắng continue. gặp khoảng trắng thoát ra k thực hiện else:
		continue
	else:
		print(char)


				