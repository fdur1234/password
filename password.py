# 密碼重試程式
# password  = '1234'
# 讓使用者重復輸入密碼
# 最多輸入3次
# 如果正確輸 就印出'登入成功！'
# 如果不正確 就印出'密碼錯誤！ 還有_次機會'

password = '1234'
i = 3
while i > 0:
    i = i - 1 
    pwd = input('請輸入密碼：')
    if pwd == password:
        print('登入成功！')
        break
    else:
        print('密碼錯誤')
        if i > 0:
            print('還有', i,'次機會' )
        else:
            print('不能再登入了！')