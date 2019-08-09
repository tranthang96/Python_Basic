"""
Đây là một ghi chú trong python
nó giống như 1 comment

"""
chuoi1='Tran Viet Thang'
print(chuoi1)
name='Thắng'
adress = 'Ha Noi'
result = f'Name: {name} \nĐịa chỉ: {adress}'
print(result)

""" Toán tử nhân chuỗi"""
strA="Hay lắm "
strB=strA*5
print(strB + "\t")

"""toán tử in
trả về giá trị true hoặc flase
true: trong chuối chứa giá trị
flase: trong chuỗi không chứa giá trị"""
test = "i"
kq = test in chuoi1
print(kq) #true

#lay tung ki tu trong chuoi
print(chuoi1[1])  # 0-T 1-r 2-a .... in ra r

#truy cap phần tử cuối cùng
a = len(chuoi1) #đo độ dài chuỗi
print(chuoi1[a-1]) #chuoi bat dau tu 0, vi vay phai tru 1

#cat chuỗi
catchuoi = chuoi1[1:3] #lấy từ 1 đến vị trí 3 . k lấy vị trí 3
print(catchuoi)
#lay het chuoi
catchuoi = chuoi1[3:None]
print(catchuoi)
# cắt chuỗi có bước nhảy
catchuoi = chuoi1[None:None:2] #nhay 2 bước . giá trị âm thì nhảy ngược lại
print(catchuoi)