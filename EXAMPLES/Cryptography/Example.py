from cryptography.fernet import Fernet
import os
import time
import subprocess
import platform
def encrypt():
    try:
        keyfile = input('input keyfilename eg "mykey.key": ')
        ftbe = input('input file name eg "grades.csv": ')
        with open(keyfile, 'rb') as mykey:
            key = mykey.read()

        f = Fernet(key)

        with open(ftbe, 'rb') as original_file:
            original = original_file.read()

        encrypted = f.encrypt(original)

        with open (f'{ftbe[:-4]}_enc.csv', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
            os.remove(ftbe)
        clear()
        success('Encryption')
    except Exception as error:
        clear()
        print(f'Something has gone wrong see error below then please try again\n{error}')
def decrypt():
    try:
        keyfile = input('input keyfilename eg "mykey.key": ')
        ftbd = input('input file name eg "grades.csv": ')

        with open(keyfile, 'rb') as mykey:
            key = mykey.read()

        f = Fernet(key)

        with open(ftbd, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
    
        decrypted = f.decrypt(encrypted)

        with open(f'{ftbd[:-4]}_dec.csv', 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
            print(decrypted)
            os.remove(ftbd)
        clear()
        success('Decryption')
    except Exception as error:
        clear()
        print(f'Something has gone wrong see error below then please try again\n{error}')

def generate_key():
    try:
        key = Fernet.generate_key()
        keyname = input('input keyname here eg "keyone.key": ')
        with open(keyname, 'wb') as mykey:
            mykey.write(key)
        clear()
        success('Key Generation')
    except Exception as error:
        clear()
        print(f'Something has gone wrong see error below then please try again\n{error}')

def delfile():
    try:
        os.remove(input('Write filename here eg "mykey.key": '))
        clear()
        success('File Removal')
    except Exception as error:
        clear()
        print(f'Something has gone wrong see error below then please try again\n{error}')

def list_files():
    try:
        clear()
        for filename in os.listdir():
            print(filename)
            time.sleep(0.3)
        time.sleep(2.5)
    except Exception as error:
        clear()
        print(f'Something has gone wrong see error below then please try again\n{error}')

def rename_file():
    try:
        filetorename = input('Which file would you like to rename eg"avcpadufhsioduh.cvs": ')
        newfilename = input('What would you like the new file name to be? eg "readablename.cvs": ')
      
        os.rename(f'\{filetorename}', f'\{newfilename}')
        clear()
        success('File Renaming')
    except Exception as error:
        clear()
        print(f'Something has gone wrong see error below then please try again\n{error}')

def clear():
    try:
        pass
    except Exception as error:
        clear()
        print(f'Something has gone wrong see error below then please try again\n{error}')

def success(operationname):
    print(f'{operationname} Operation Successfull')

def menuexit():
    booleen = input('---------------------------------\nWould you like to execute another function? y/n \nAnswer Here: ')
    if booleen.lower() == 'y':
        pass
    elif booleen.lower() == 'n':
        exit()
    else:
        print('An error occured please try again')
        menuexit()

def start():
    while True:
        choice = int(input('---------------------------------\n1.Generate a key \n2.Encrypt\n3.Decrypt\n4.File Disposal\n5.List all files in dir\n6.Rename File\n7.Exit...\nInput choice below\n---------------------------------\n'))
        if choice == 1:
            generate_key()
            menuexit()
        elif choice == 2:
            encrypt()
            menuexit()
        elif choice == 3:
            decrypt()
            menuexit()
        elif choice == 4:
            delfile()
            menuexit()
        elif choice == 5:
            list_files()
            menuexit()
        elif choice == 6:
            rename_file()
            menuexit()
        elif choice == 7:
            print('Goodbye!')
            time.sleep(0.5)
            exit()
        else:
            print('Not a valid input')

start()
