#lấy giá trị value
# cú pháp : your_dict(key)

dic = {'name': 'Thang', 'member': 96 }
print(dic['name'])
# lấy key ko tồn tại trong dict thì báo lỗi

#========thay đổi giá trị=======
dic['name'] = 'Tran Thang'
print(dic)
#===== Nếu gán giá trị k tồn tại, thì tự động thêm nó vào
dic['tuoi'] = "rqwrt"
print(dic)
# cộng thêm giá trị
dic['name'] = dic['name'] + " BG"
print(dic)
