#Mặc định hàm print sẽ ghi nội dung vào file sys.stdout. 
# Cũng nhờ vậy, bạn mới thấy được nội dung trên shell. 
# Đương nhiên, dựa vào đây, ta cũng có thể sử dụng hàm print như là phương thức write trong việc ghi file.
with open('printtext.txt', 'w') as h:
   print('printed by print function', file=h) # cách 3 dấu cách
with open('printtext.txt') as f:
   print(f.read())
from time import sleep # nhập hàm sleep từ thư viện time
# Nếu là True, nó sẽ yêu cầu bộ đệm xuất những gì có trong bộ đệm ra.
print('start...', end='sfdfff', flush=True)
sleep(1) # dừng chương trình 3 giây
print('end...')



your_name = "Henry"
your_great = "Hello! My name is "
print(your_great)
for c in your_great + your_name:
    print(c, end='', flush=True)
    sleep(0.1)
print()