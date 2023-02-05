from cryptography.fernet import Fernet
import time

# Dictionary representing the morse code chart

Code_Dict = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----',
}

# ', ':'--..--', '.':'.-.-.-',
#    '?':'..--..', '/':'-..-.', '-':'-....-',
#    '(':'-.--.', ')':'-.--.-'

def encrypt(text):
    # Code For Encryption
    code = ""
    for letters in text:
        # for letters in text:
        if letters.isalpha() or letters.isdigit():
            if letters.isupper():
                code += letters + " "
            elif letters.islower():
                code += Code_Dict[letters.upper()] + " "
            else:
                code += Code_Dict[letters] + " "
        elif letters == " ":
            code += "^ "
        else:
            code += letters + " "
    return code
            

def decrypt(code):
    # Code For Decryption
    text = ""
    code1 = code.split(" ")
    keys = [i for i in Code_Dict]
    value = [Code_Dict[i] for i in Code_Dict]
    for data in code1:
        if data == '^':
            text += " "
        elif data.isupper() == False:
            if data in value:
                text += keys[value.index(data)].lower()
            else:
                text += str(data)
        else:
            text += str(data)
    return text

def convert(word):
    t = int(time.time())%10
    alp = "abcdefghijklmnopqrstuvwxyz"
    cycle = 2*alp
    output = ""
    cycle = cycle[t:26 + t]
    print(word, alp, cycle)
    for i in word:
        # print(i)
        index = alp.index(i)
        # print(i, cycle[index])
        output += cycle[index]
    t = str(t)
    output += t
    print(encrypt(output))
    return encrypt(output).encode('utf-8')

content = "cryptograph"
content = convert(content)
# with open("Tkinter_Password_Manager/User_data.json", "rb") as file:
#     content += file.read()
# print(content)

def cycle(word, t):
    # t = int(time.time())%10
    content = decrypt(word)
    alp = "abcdefghijklmnopqrstuvwxyz"
    cycle = 2*alp
    output = ""
    # cycle = cycle[26 - t:]
    # print(word, alp, cycle)
    for i in content:
        try:
            # print(i)
            index = alp.index(i)
            # print(i, cycle[index])
            output += cycle[26+index-t]
        except:
            output += ""
    t = str(t)
    output += t
    return output

# key = Fernet.generate_key()
# f = Fernet(key)
# en = f.encrypt(content)
# print(en)
# # print(f.decrypt(en))
# data = str(f.decrypt(en))[2:-1]
# # print(data)
# t = decrypt(data)
# t = int(t[-1:])
# # print(t[-1:])
# print(cycle(data, t))
# print(decrypt(str(f.decrypt(en))[2:]))


# a = convert("hello")
# print(a)
# print(decrypt(a))