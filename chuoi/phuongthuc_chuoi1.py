#phương thức chuỗi 
a = 'tran viet thang hust.edu.vn'
#cắt chuỗi
b = a.split(' ',4) #cắt khoảng trắng , có thể thay khoảng trắng bằng kí tự khác, 4: số lần cắt
print(b)
# thêm rsplit : cắt từ bên phải
#=============partition: sự phân chia : nếu ko có trả kí tự trống===
c = a.partition('viet')
# rpartition chạy từ bên phải ,
print(c)
#========đếm chuỗi======
d = a.count('t') #đếm t trong chuỗi a
 #tương tự count([kí tự cần đếm],0,13) 0:kí tự bắt đầu chạy . 13: kí tự cuối.. thay linh hoạt
print (d)

#==========kiểm tra kí tự bắt đầu , trả về true hoặc false
e = a.startswith('tran') # true
f = a.endswith('aaaa') #false 
#===== tìm chuỗi 
timchuoi = a.find('n') #trả về vị trí . ko thấy thì -1 . tươn tự rfind
print(timchuoi)
#============tìm chuỗi
g = a.index('t') # tương tự find . k thấy báo lỗi chương trình
#============phương thức xác thực
h = a.islower() # kiểm tra chuỗi viết thường k
                # isupper kiểm tra chuỗi viết hoa ko
                # isdigit kiểm tra chuỗi đó có phải số hay ko?
                # isspace kiểm tra chuỗi là khoảng trắng hay ko?