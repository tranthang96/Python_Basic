#locals và globals
"""Thay đổi giá trị argument gián tiếp qua parameter
Nói về vấn đề này, bạn nên biết 2 thuật ngữ là pass by reference và pass by value.

Đầu tiên, thế nào là pass by reference. Giả sử bạn có một chiếc laptop. Thằng bạn nó muốn mượn dùng một
 ngày. Thế là bạn mang máy của mình cho nó mượn. Về nhà thằng bạn nó down phim, down game, cài virus.
 Sau một ngày, hắn đem trả lại bạn. Coi như chiếc laptop của bạn tan nát. 
 Việc bạn đưa laptop của mình cho thằng bạn cũng giống như việc pass by reference. 
 Có nghĩa là bạn đưa bản gốc.

Sang tuần sau. Thằng bạn lại đến mượn đồ tiếp và bây giờ là chiếc xe đạp. Bạn biết tỏng hắn kiểu gì 
cũng phá, liền lấy bảo bối là  “Gương nhân đôi”, sau đó bạn nhân bản chiếc xe đạp của bạn ra. Bạn
 lấy bản nhân bản đưa hắn mượn. Và bạn thấy đó, dù cho hắn có đạp nát chiếc xe kia thì xe của bạn 
 cũng không sao.Đó  gọi là bạn pass by value, đưa giá trị hoặc là “đưa bản sao”.

Trong Python, việc bạn CHỈ CÓ THỂ pass by value"""
var1 = "Tran Thang"
def ghi_ten(var2):
	print("Tên của bạn là", var2)
	print(var1) 	#var1 là biến toàn cục
	global x
	x = 3             # khi có global là biến toàn cục 
def test_x():
	x=55
	print(x)

test_x()        
ghi_ten("Thang")      # gọi hàm này mới có biến global x
print(x)
print(var1)
"""Giới thiệu hàm locals và globals
Cái tên hàm nói lên tất cả. Hàm locals cho ta biết được những biến local 
(những biến được khai báo trong hàm) nằm trong chương trình của chúng ta. Còn globals 
là hàm giúp chúng ta biết được những  biến global trong chương trình.

Kết quả trả ra của hai hàm này là một Dict. Với key là tên biến và value là giá trị của biến."""

print(locals())
print(globals())