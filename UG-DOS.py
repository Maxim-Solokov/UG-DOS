import os
import shutil
import hashlib

operas=os.name
path=os.getcwd
running=True

print("UnderGround-Disk Operating Sys. Ver2.0 Working on "+operas+" System")
print("Copyright Undersoft (2025), All rights reserved.")

def changeline(file_path, line_number, text_to_insert):
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

    
    if line_number < 1 or line_number > len(lines):
        print(f"Error: Line number {line_number} is out of range.")
        return


    lines.insert(line_number - 1, text_to_insert + '\n') 

    with open(file_path, 'w') as file:
        file.writelines(lines)

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

def judge(var,abc):
    return var.startswith(abc)

def cm_echo(var1):
    try:
        listtemp = var1.split(" ")
        listtemp.pop(0)
        i1 = ""
        for item in listtemp:
            i1 += item + " "
    except:
        i1 = var1
    return i1

def cm_exit(var2):
    try:
        words=var2.split(" ")
        words.pop(0)
        result=" ".join(words)
    except(AttributeError, IndexError):
        result=var2
    return result

def main():
    while running==True:
        command_line=input(account+'@'+path()+' >')
        if judge(command_line, "echo"):
            command_line=cm_echo(command_line)
            print(command_line)
            return
        if judge(command_line, "exit"):
            command_line=cm_exit(command_line)
            if command_line=="confirm":
                quit()
            print("Are you really wanna exit UG-DOS? If yes, please use the command 'exit confirm'. you may destory your unsave data.")
            return
        else:
            print("'"+command_line+"' isn't a executable files, an avaliable command line or a UG-DOS Module Code.")


configure=False

used=os.path.exists('./Users')
used_2=os.path.exists('./Users/root')
if used==False:
    configure=False
    print("Loading UG-DOS Library... Please Wait")
    os.mkdir('./Users/')
    
    used_2=os.path.exists('./Users/root')
    if used_2==False:
        os.mkdir('./Users/root')
        print("Welcome to use the UG-DOS!")
        create_name=input("Please enter your Username:")
        os.mkdir('./Users/'+create_name)
        pwa=1
        pwb=2
        while pwa!=pwb:
                pwa=input("Please enter your Password:")
                pwb=input("Please enter your Password again:")
                if pwa==pwb:
                     break
                else:
                     print("ERR:The passwords entered don't match")
        config=open('./Users/'+create_name+'/userlib.txt', "w")
        config.close()
        write=open('./Users/'+create_name+'/userlib.txt', "w")
        pwsec=md5_encrypt(pwb)
        write.write(pwsec)
        write.close()
    
    print("Congratulations! Your's Account is ready to use!")
    configure=True

logged=False
while logged==False:
    account=input("Username:")
    ac_check=os.path.exists('./Users/'+account)
    if ac_check==True:
        write=open('./Users/'+account+'/userlib.txt', "r")
        passwd=input('Password:')
        passwd_sec=md5_encrypt(passwd)
        passwd_2=write.read()
        if passwd_2==passwd_sec:
            logged=True
            break
        else:
            print("ERR:Password incorrect.")
    else:
        print("ERR:Username Don't usable.")

print('Welcome,'+account)

while running==True:
    main()