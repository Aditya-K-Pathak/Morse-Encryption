from cryptography.fernet import Fernet

# content = b""
# with open("Tkinter_Password_Manager/Cryptograph.py", "rb") as file:
#     content += file.read()

# # import temp

# key = Fernet.generate_key()
# print(key)
# f = Fernet(key)
# en = f.encrypt(content)
# dd = f.decrypt(en)

# with open("Tkinter_Password_Manager/temp.py", "wb") as file:
#     file.write(en)
# with open("Tkinter_Password_Manager/keys.key", "wb") as file:
#     file.write(key)

def decode():
    content = b""
    data = b""
    key = b""
    with open("Tkinter_Password_Manager/temp.py", "rb") as file:
        content += file.read()

    with open ("Tkinter_Password_Manager/keys.key", "rb") as file:
        key = file.read()
        # print(key)
    
    with open ("Tkinter_Password_Manager/temp.py", "wb") as file:
        f = Fernet(key)
        data += f.decrypt(content)
        file.write(data)

    import temp
    a = temp.encrypt("Hello Sagar")
    print(temp.decrypt(a))

    key = Fernet.generate_key()
    f = Fernet(key)
    with open ("Tkinter_Password_Manager/temp.py", "wb") as file:
        en = f.encrypt(data)
        file.write(en)

    with open ("Tkinter_Password_Manager/keys.key", "wb") as file:
        file.write(key)
decode()