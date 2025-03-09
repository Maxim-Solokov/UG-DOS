import hashlib

def md5_encrypt(text):
    # 创建一个md5对象
    md5 = hashlib.md5()
    # 将字符串编码为字节
    text_bytes = text.encode('utf-8')
    # 更新md5对象
    md5.update(text_bytes)
    # 获取加密后的16进制字符串
    encrypted_text = md5.hexdigest()
    return encrypted_text

password = md5_encrypt("Our-World1223")
i =  input("请输入密码>>> ")
if md5_encrypt(i) == password:
    print("登陆成功！")