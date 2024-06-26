from cryptography.fernet import Fernet

    
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key 

def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(keys) 


master_pwd = input("What is the master password? ")
keys = load_key() + master_pwd.encode()
fer = Fernet(keys)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()       #rstrip - skips new line in the console
            user, passw = data.split("|")
            print("User:",user, "| Password:", fer.decrypt(passw.encode()))


def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    # w - create a new file  and clears the existing file and over right the existing file
    # r - read a file
    # a - add something to existing file and create a new file if the file doesn't exist

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrpt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode!")
        continue