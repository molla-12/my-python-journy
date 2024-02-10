from cryptography.fernet import Fernet



def write_key():
    key = Fernet.generate_key()
    # wb write in byte
    with open("key.key","wb") as key_file:
        key_file.write(key)

def read_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key
pdw = input("what is your master password ")
key = read_key() + pdw.encode()
fer = Fernet(key)
        
mode = input("add new or view existing one ")
# b'hello' means write in bit 
def view():
    with open('passwords.txt','r') as r:
        # readline to list out each char in new line 
        for line in r.readlines():
            # rstrip to remov the new lin afre enach line
            # print(line.rstrip())
            # wnat to separat user name form the password
            data = line.rstrip()
            user, password= data.split("|")
            # add .decode to remve the byte
            print("user is name " + user +" and pasword is "+ str(fer.decrypt(password.encode()).decode()))

def add():
    name = input("account name: ")
    pwd = input("password")
# wuth to close file by it self w to rewrite remove and add the new one rite r read a mode append
    with open('passwords.txt','a') as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode()).decode()) + "\n")
        

if mode == "view":
    view()
elif mode == "add":
    add()
else:
    print("invalid mood man")

