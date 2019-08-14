"""Chúng ta sẽ cùng tìm hiểu phần cấu trúc trước:

for variable_1, variable_2, .. variable_n in sequence:

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
h = (1,2,3)
print(type(h))

h, k, t = (1,2,3) # unpacking