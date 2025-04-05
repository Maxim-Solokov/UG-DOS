import os
import shutil
import hashlib
import linecache
import zipfile
import requests

def md5_encrypt(text):
    md5 = hashlib.md5()
    text_bytes = text.encode('utf-8')
    md5.update(text_bytes)
    encrypted_text = md5.hexdigest()
    return encrypted_text

def lang_print(lines):
    viewlang=linecache.getline(langForNow, lines).rstrip('\n')
    return viewlang

def config_check(lines, who):
    if who=='system':
        config_locate='./Configs/config.yml'
    else:
        config_locate='./Configs/'+who+'/config.txt'
    viewlang=linecache.getline(config_locate, lines).rstrip('\n')
    return viewlang

def lang_update(abc):
    try:
        if abc=="check":
            lang_pack=requests.get(url='https://github.com/Maxim-Solokov/UG-LP/releases/download/2.1.0/updatelog.txt')
            cache_pack_loc='./cache/latestlog.txt'
        if abc=="update":
            lang_pack=requests.get(url='https://github.com/Maxim-Solokov/UG-LP/releases/download/2.1.0/UG-LanguagePack-2-1-0.zip')
            cache_pack_loc='./cache/UGLanguagePack210.zip'
            lang_pack_loc=path()+'/Languages'
            lang_pack.raise_for_status()
            with open(cache_pack_loc, 'wb') as lang_cache:
                for chunk in lang_pack.iter_content(chunk_size=8192):
                    if chunk:
                        lang_cache.write(chunk)
            with zipfile.ZipFile(cache_pack_loc, 'r') as ext:
                    ext.extractall(lang_pack_loc)
        if abc=="local":
            lang_pack_loc=path()+'/Languages'
            lang_pack.raise_for_status()
            with zipfile.ZipFile(cache_pack_loc, 'r') as ext:
                    ext.extractall(lang_pack_loc)
    except:
        if abc=="check":
            print("[ERRR] Check Error")
        if abc=='update'and"local":
            print('[ERRR] Update Error')
            
def adduser(permission):
    add_name=input(lang_print(71))
    os.mkdir('./Users/user-'+add_name)
    os.mkdir('./Configs/Users/user-'+add_name)
    pwa=1
    pwb=2
    while pwa!=pwb:
        pwa=input(lang_print(72))
        pwb=input(lang_print(73))
        if pwa==pwb:
            break
        else:
             print(lang_print(74))
    config=open('./Configs/Users/user-'+add_name+'/config.yml', "w")
    config.close()
    write=open('./Configs/Users/user-'+add_name+'/config.yml', "w")
    pwsec=md5_encrypt(pwb)
    write.write(pwsec+'\n'+add_name+'\nguest')
    write.close()
    print("[INFO] "+lang_print(75))

def login(types):
    logged=False
    while not logged:
        if 'account' not in globals():
            account=input(lang_print(24))
        ac_check=os.path.exists('./Users/user-'+account)
        if ac_check==True:
            write='./Configs/Users/user-'+account+'/config.yml'
            passwd=input(lang_print(26))
            passwd_sec=md5_encrypt(passwd)
            passwd_2=linecache.getline(write, 1).rstrip('\n')
            if passwd_2==passwd_sec:
                if types=='loginning':
                    return account
                if types=='checking':
                    logged=True
                print('[INFO] '+lang_print(28)+account)
                break
            else:
                print(lang_print(27))
        else:
            print(lang_print(25))

def judge(var,abc):
    return var.startswith(abc)

def echo(var):
    try:
        words=var.split(" ")
        words.pop(0)
        result=" ".join(words)
    except(AttributeError, IndexError):
        result=var
    return result

def cm(var):
    try:
        words=var.split(" ")
        result=words
    except(AttributeError, IndexError):
        result=var
    return result

def cm_help():
    print(lang_print(36))
    print(lang_print(37))
    print(lang_print(38))
    print(lang_print(39))
    print(lang_print(40))
    print(lang_print(41))
    print(lang_print(42))
    print(lang_print(43))
    print(lang_print(44))
    print(lang_print(45))
    print(lang_print(46))
    print(lang_print(47))
    print(lang_print(48))
    print(lang_print(49))
    print(lang_print(50))
    print(lang_print(51))
    print(lang_print(52))
    print(lang_print(53))
    print(lang_print(54))
    print(lang_print(55))
    print(lang_print(56))
    print(lang_print(57))
    print(lang_print(58))
    print(lang_print(59))
    print(lang_print(60))
    print(lang_print(61))
    print(lang_print(62))
    print(lang_print(63))

def main():
    logged=True
    while logged==True:
        command_line=input(account+'@'+path()+' >')
        if judge(command_line, "echo"):
            command_line=echo(command_line)
            print(command_line)
            return
        if judge(command_line, "exit"):
            command_line=cm(command_line)
            if command_line=="--confirm"or"-c":
                print(lang_print(68))
                quit()
            print("[WARN] "+lang_print(66))
            confirm=input("y/N")
            if confirm=='y':
                print(lang_print(68))
                quit
            return
        if judge(command_line, "help"):
            command_line=cm_help()
            return
        if judge(command_line, "adduser"):
            command_line=cm(command_line)
            if command_line=='--admin'or'-a':
                add_name=input(lang_print(71))
                os.mkdir('./Users/user-'+add_name)
                os.mkdir('./Configs/Users/user-'+add_name)
                pwa=1
                pwb=2
                while pwa!=pwb:
                    pwa=input(lang_print(72))
                    pwb=input(lang_print(73))
                    if pwa==pwb:
                        break
                    else:
                        print(lang_print(74))
                config=open('./Configs/Users/user-'+add_name+'/config.yml', "w")
                config.close()
                write=open('./Configs/Users/user-'+add_name+'/config.yml', "w")
                pwsec=md5_encrypt(pwb)
                write.write(pwsec+'\n'+add_name+'\nadmin')
                write.close()
                print("[INFO] "+lang_print(75))
            elif command_line=='--guest'or'-g':
                add_name=input(lang_print(71))
                os.mkdir('./Users/user-'+add_name)
                os.mkdir('./Configs/Users/user-'+add_name)
                pwa=1
                pwb=2
                while pwa!=pwb:
                    pwa=input(lang_print(72))
                    pwb=input(lang_print(73))
                if pwa==pwb:
                    break
                else:
                    print(lang_print(74))
                config=open('./Configs/Users/user-'+add_name+'/config.yml', "w")
                config.close()
                write=open('./Configs/Users/user-'+add_name+'/config.yml', "w")
                pwsec=md5_encrypt(pwb)
                write.write(pwsec+'\n'+add_name+'\nguest')
                write.close()
                print("[INFO] "+lang_print(75))
        else:
            print("[ERRR] '"+command_line+"'"+lang_print(33))

operas=os.name
path=os.getcwd
configured=True
used=os.path.exists('./Configs/Users/user?')
used_2=os.path.exists('./Users/root')
running=True
langForNow=config_check(1, "system")
if not used:
    try:
        shutil.rmtree('./cache/')
        shutil.rmtree('./Configs/')
        shutil.rmtree('./Users/')
        shutil.rmtree('./Languages/')
    except:
        print(" ")
    configured=False
    print("[INFO] Loading UG-DOS Library... Please Wait")
    os.mkdir('./Users')
    os.mkdir('./Configs')
    os.mkdir('./Configs/Users')
    os.mkdir('./cache')
    os.mkdir('./Languages')
    lang_update("update")
    print("Please choose your language./请选择语言")
    print("Supported languages:zh_CN, zh_TW, zh_HK, ru_RU, en_US")
    langForNow=1
    lang_set=open('./Configs/config.yml', 'w')
    lang_check=os.path.exists(langForNow)
    langSetting=False
    while not langSetting:
        if lang_check:
            langForNow='./Languages/'+input('Language=')+'.yml'
            lang_set.write(langForNow)
            langSetting=True
        else:
            print('Language wrong or not support.')
    if used==False:
        os.mkdir('./Users/user-root')
        os.mkdir('./Configs/Users/user-root')
        print(lang_print(12))
        print(lang_print(13))
        print(lang_print(14))
        pwa=1
        pwb=2
        while pwa!=pwb:
            pwa=input(lang_print(15))
            pwb=input(lang_print(18))
            if pwa==pwb:
                break
            else:
                 print("[ERRR] "+lang_print(19))
        config_root=open('./Configs/Users/user-root/config.yml', "w")
        config_root.close()
        write_root=open('./Configs/Users/user-root/config.yml', "w")
        pwsec_root=md5_encrypt(pwb)
        write_root.write(pwsec_root+'\nroot\nadmin')
        write_root.close()
        create_name=input(lang_print(16))
        os.mkdir('./Users/user-'+create_name)
        os.mkdir('./Configs/Users/user-'+create_name)
        pwa=1
        pwb=2
        while pwa!=pwb:
            pwa=input(lang_print(17))
            pwb=input(lang_print(18))
            if pwa==pwb:
                break
            else:
                 print("[ERRR] "+lang_print(19))
        config=open('./Configs/Users/user-'+create_name+'/config.yml', "w")
        config.close()
        write=open('./Configs/Users/user-'+create_name+'/config.yml', "w")
        pwsec=md5_encrypt(pwb)
        write.write(pwsec+'\n'+create_name+'\nguest')
        write.close()
        print("[INFO] "+lang_print(20))
        done=open('./Configs/Users/user?', 'w')
        done.close
    else:
        configure=True

print("\n"+lang_print(23))

account=login('loginning')

print("UnderGround-Disk Operating Sys. Ver2.1.0. Working on "+operas+" System")
print("Copyright Undersoft (2025), All rights reserved.")
lang_update("")

logged=True
while logged==True:
    main()