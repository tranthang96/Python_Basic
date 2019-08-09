#gán giá cho biến 
a = 12.123456789101112131415;
print(a);
print(type(a));

#lấy toàn bộ nội dung thư viện decimal
#từ thư viện decimal -> import toàn bộ vào
from decimal import*

#lấy tối đa 50 chữ số phần thập phân + phần nguyên
getcontext().prec = 50;

d = Decimal(10)/Decimal(3);

print(type(d))

print(d);
