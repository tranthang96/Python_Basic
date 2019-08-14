#block trong python
'''
# Với đa số ngôn ngữ lập trình hiện nay, thường dùng cặp dấu ngoặc { } để phân chia các block.

Riêng đối với Python lại sử dụng việc định dạng code để suy ra các block. 
Đây là điều giúp code Python luôn luôn phải đẹp mắt.

Một số điều lưu ý về việc định dạng code block trong Python:
	Câu lệnh mở block kết thúc bằng dấu hai chấm (:), sau khi sử dụng câu lệnh có dấu hai chấm (:) 
		buộc phải xuống dòng và lùi lề vào trong và có tối thiểu một câu lệnh để không bỏ trống block.
	Những dòng code cùng lề thì là cùng một block.
	Một block có thể có nhiều block khác.
	Khi căn lề block không sử dụng cả tab lẫn space.
	Nên sử dụng 4 space để căn lề một block
'''
#Câu lệnh mở block kết thúc bằng dấu hai chấm (:)
a=3
if a==3:
	print("aaaaaa")
#hoặc
if a==3: 
	print("aa"); print("aaaaaff"); # vẫn là 1 1block
a = float(input("Nhap vao 3 số a=:" ))
b = float(input("Nhap vao 3 số b=:" ))
c = float(input("Nhap vao 3 số c=:" ))

if(a<b<c): print("giá trị lớn nhất là : ",c)
if(a<c<b): print("giá trị lớn nhất là : ",b)

