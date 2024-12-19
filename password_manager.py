from cryptography.fernet import Fernet

def key_write():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def key_load():
    with open("key.key", "rb") as file:
        data = file.read()
        return data
        


master_pass = input("Enter the master password: ")
key = key_load() + master_pass.encode()
fer = Fernet(key)

def view():
    # with open("Password.txt", "r") as f:
    #     for line in f.readlines():
    #         data = line.rstrip()
    #         user, passw = data.split("|")
    #         print("Username: " + user + ", Password: " + fer.decrypt(passw.encode()).decode())
            #str(fer.decrypt(passw.encode())) this is also wrong
    try:
        with open("Password.txt", "r") as f:
            for line in f.readlines():
                if "|" in line:
                    data = line.rstrip()
                    try:
                        user, passw = data.split("|")
                        decrypted_pass = fer.decrypt(passw.encode()).decode()
                        print(f"Username: {user}, Password: {decrypted_pass}")
                    except Exception as e:
                        print(f"Error decrypting password for user '{data}': {e}")
                else:
                    print(f"Malformed line skipped: {line}")
    except FileNotFoundError:
        print("Password file not found. Please add some passwords first.")
 

def add():
    name = input("Enter the username: ")
    pwd = input("Enter the password: ")
    
    with open("Password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") #str(fer.encrypt(pwd.encode())) this is wrong 

while True:
    mode = input("Would you like to add a new password or view a password (add, view) or enter 'q' to quite ? ")
    
    if mode == "q":
        break
        
    if mode == "add":
        add()
        
    elif mode == "view":
        view()
    
    else:
        print("Please enter a valid input !!!")
        continue

''' b'gAAAAABnYSzvbi3JE2bwImXbGExepFR9pLylZfM_-8NZNhOXZ5cQQlGAni7oqyMpxxrE5zXVDoNiCK1QqT28Je0TbUlj2lU9iQ==' 
'''