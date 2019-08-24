#Hàm xuất trong python
'''
	Vì sao cần hàm print, Nếu bạn hay dùng interactive prompt thì bạn nhân ra rằng, 
	kết quả luôn xuất hiện sau mỗi dòng code của bạn. Tuy nhiên, nó sẽ không như vậy 
	khi bạn viết những dòng code vào trong một file Python và chạy chương trình đó.

	Bạn cần một hàm giúp bạn xuất các nội dung mà bạn muốn cụ thể ở đây là xuất ra 
	Shell (terminal, command prompt, powershell,…). Đó là lí do hàm print ra đời!
Tìm hiểu cách sử dụng hàm print thông qua các parameter
Hàm print có cú pháp như sau

Cú pháp:
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

Chúng ta sẽ tìm hiểu parameter đầu tiên

*objects
* chính là packing argument. Ở đây hiểu nôm na sẽ là nó sẽ gom lại
 	các argument của bạn lại thành một Tuple.
'''
packing = 1, 2, 3, 4 # giống như gọi hàm function(1, 2, 3, 4)
print(packing)
# sep (separate – chia ra, phân ra)
'''
Giá trị mặc định của parameter này là một khoảng trắng. 
Khi các argument bạn ném vào cho hàm print để hàm print in ra nội dung, 
như đã biết là nó sẽ được gói vào một Tuple. Các giá trị trong Tuple sẽ 
được nối với nhau bằng parameter sep.

Lưu ý: Khi truyền giá trị vào cho parameter theo cách keyword argument thì sẽ không bị packing. 
Nghĩa là sẽ không bị gói vào trong giá trị của parameter object.'''
print("Tran", "Thang" , sep="**") #Tran**Thang
#======end (kết thúc bằng)======
"""Nếu bạn từng học qua ngôn ngữ lập trình C hoặc C++ hay là Java cũng có thể là C#. 
Bạn sẽ nhận thấy, mỗi lần print, chúng sẽ tự xuống dòng.

Đó là nhờ parameter end. Nó sẽ tự thêm một kí tự newline (\n) vào
cuối để có thể đưa con trỏ xuống dòng mới thay vì bạn phải tự thêm \n như 
một số ngôn ngữ lập trình khác (một số ngôn ngữ lập trình có hỗ trợ thêm 
phương thức giúp xuất nội dung và tự động xuống dòng)

Và đương nhiên, chúng ta cũng có thể thay đổi giá trị của parameter này."""
print('line 1')
print('line 2')
print('line 3')
print('a line without newline', end='|||') #không xuống dòng
print('a line without newline', end='\n')
# 
from time import sleep # nhập hàm sleep từ thư viện time

print('start....')
sleep(3) # dừng chương trình 3 giây
print('end...')
# sau 3s mới hiện 


print('start....', end='') # in ra nội dung và kết thúc bới một chuỗi  rỗng
sleep(3) # dừng chương trình 3 giây
print('end...')
"""
Lần này đã có khác biệt. Bạn sẽ không thấy gì xuất hiện ban đầu, mãi đến 3 giây sau 
bạn mới thấy dòng `start....end...`. Kết quả thì đúng, nhưng cách kết quả được xuất ra 
thì không giống như bạn nghĩ.

Vì sao lại vậy? Đó là do mỗi lần hàm print nhận được các giá trị bạn muốn in. 
Các giá trị đó được gói trong một Tuple. Tiếp đến, hàm print nạp từng giá trị trong Tuple vào bộ nhớ đệm. 
với bản 3.7.4 thì không bị như vậy nữa 
Hoặc khi kết thúc chương trình, những gì còn trong bộ đệm cũng sẽ được xuất ra."""

print('line 1\n', 'line2', end='')
sleep(3) # dừng chương trình 3 giây
print('end...')


print('line 1', 'lin\ne2', end='')
sleep(3) # dừng chương trình 3 giây
print('end...')