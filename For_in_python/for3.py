"""Có lẽ bây giờ những comprehension không còn phức tạp với các bạn nữa.

Comprehension là một công cụ rất hiệu quả của Python để xử lí rất nhiều việc mà chỉ cần một dòng.

Bên cạnh đó. Người ta còn so sánh những comprehension và những đoạn code với chức năng tương tự thì comprehension có tốc độ nhanh hơn.

Lời tác giả:

	Mọi người sẽ phải Ồ lên khi thấy bạn có một comprehension chỉ tốn một dòng và thời gian thực thi nhanh hơn.
Thế nên bạn nên luyện tập sử dụng comprehension thường xuyên.
	Sau này khi kết hợp với anonymous function là lambda bạn sẽ tạo ra được những thứ mang đậm thương hiệu one-liner.
Python không khó. Quan trọng là bạn phải nằm lòng các API của Python (các chức năng mà ngôn ngữ hỗ trợ) là một trong những thứ đó
Ta có thể tổng quát đơn giản cú pháp của một comprehension như sau

Cú pháp:
[ output-expression for-statement optional-predicate ]

Sử dụng [ cho List, các bạn có thể sử dụng các cặp ngoặc khác nhưng phải để output-expression phù hợp với kiểu dữ liệu.
 Như dict thì bạn phải để output-expression là một cặp key-value."""

list_=['--'.join((a.capitalize(), b.upper() + c.lower())) for a, b, c in [('tran', 'than', 'hust'), ('chia', 'sẻ', 'FREE')]]
print(list_)

{key:value + 1 for key, value in (('Kteam', 69), ('Tèo', 50), ('Tũn', 14), ('Free Education', 93)) if value % 2 != 0}
#{'Kteam': 70, 'Free Education': 94}
#Giới thiệu hàm enumerate
"""Cú pháp:
enumerate(iterable[, start])

Nếu start không được gửi vào thì mặc định là 0

Hàm này là một generator nhờ câu lệnh yield trong hàm. Nó sẽ tạo ra mỗi giá trị là một cặp gồm số thứ tự và giá trị có cấu trúc như sau

(start + 0, seq[0]), (start + 1, seq[1]), (start + 2, seq[2]), ..."""
student_list = ['Long', 'Trung', 'Giàu', 'Thành']
a=list(enumerate(student_list,2))
print(a)