File là một thứ rất quen thuộc đối với những người sử dụng máy tính. Bạn thao tác,tạo lập file hằng ngày. Nó có thể là một bức hình, một văn bản tài liệu, một file thực thi và nhiều nhiều thứ khác nữa.

Trong Python, file có 2 loại:

+ Text File

Được cấu trúc như một dãy các dòng, mỗi dòng bao gồm một dãy các kí tự và một dòng tối thiểu là một kí tự dù cho dòng đó là dòng trống.
Các dòng trong text file được ngăn cách bởi một kí tự newline và mặc định trong Python chính là kí tự escape sequence newline \n.

+ Binary File

Các file này chỉ có thể được xử lí bởi một ứng dụng biết và có thể hiểu được cấu trúc của file này.
Và chúng ta ở đây với mức độ cơ bản chỉ xử lí text file.

* Mở file trong python
Khỏi phải bàn, muốn thao tác với file, ta phải mở file. Mà muốn mở file, ta cũng cần phải có file.

Ở đây, sẽ tạo một file, và sau đó mở CMD ở ngay trong thư mục chứ file đó để không gặp nhiều khó khăn trong việc xử lí đường dẫn (Việc xử lí đường dẫn, sẽ giới thiệu cách xử lí bằng thư viện os trong tương lai).

Tên file sẽ là: text.txt


open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
cơ bản quan tâm file và mode
mode:

r : Mở để đọc. đây là mặc định
r+: Mở để đọc và ghi
w : Mở để ghi, trước đó sẽ xoá hết nội dung của file hiện có. Nếu file không tồn tại, sẽ tạo ra một file mới có tên là tên file chúng ta truyền vào
w+: Mở để đọc và ghi, trước đó sẽ xoá hết nội dung của file hiện có. Nếu file không tồn tại, sẽ tạo ra một file mới có tên là tên file chúng ta truyền vào
a : Mở để ghi. Nếu file không tồn tại, sẽ tạo ra một file mới có tên là tên file chúng ta truyền vào
a+: Mở để ghi, đọc. Nếu file không tồn tại, sẽ tạo ra một file mới có tên là tên file chúng ta truyền vào



