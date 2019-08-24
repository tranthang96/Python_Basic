#căn lề python
"""Dưới đây là 3 cách căn lề cơ bản của phương thức format
	{:(c)<n}  // căn lề trái
	{:(c)>n}  // căn lề phải
	{:(c)^n}  // căn lề giữa
"""
#căn giữa tổng 20 kí tự. hoặc center
StrA='{:^20}'.format('Thắng')
StrB='{:*^20}'.format('Thắng')
#=====================
print(StrA)
print(StrB)
#================================
#căn trái 
StrC="{:<5}".format("abc") 
	#hoặc
a = "abc"
StrL=a.ljust(30,'-')  # ljust([khoảng cách],[kí tự])
print(StrL)
	#căn trái tổng cộng 5 kí tự
print(StrC)
#===================================
#căn phải hoặc rjust.
StrD='{:*>20}'.format("avc")
print(StrD)
#====================test 1=================
# phần định dạng
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Tran Thang', 'Viet Nam')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'ABc', 'Canada')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')

# phần xuất kết quả
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)