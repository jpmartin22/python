from cryptography.fernet import Fernet



master_pwd=input("whats your master password? ")

def write_key():
    key=Fernet.generate_key()
    with open('key.key','wb')as key_file:
        key_file.write(key)
write_key()        
def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            
            user, pwd = data.split("|")
            print("User:", user, "| Password:", pwd)
            
def add():
    name=input("Account Name : ")
    pwd=input("Password : ")
    with open("passwords.txt","a") as f:
        f.write(name + "|" +pwd +"\n")
while True:
    mode=input("To add a new password ,write add or To view it,write view and write q to quit:  ")
    if mode=="q":
        break
    elif mode=="view":
        view()

    elif mode=="add":
        add()
    else:
        print("Invalid mode!")    