# ========================Modules============================

import random
from tkinter import *
from tkinter import messagebox as tmsg
from PIL import Image, ImageTk
import json
import Cryptograph as crptgrph

# ========================Screen============================

root = Tk()
root.title("Password Manager")
root.minsize(700, 700)
root.maxsize(800, 800)
File_Path = "I:/Users/Aditya Pathak/Downloads/Documents/Tkinter/100-days/Tkinter_Password_Manager/User_data.json"


# ==================Required Definitions===================

def gen_pass():

    # ===================Generates a random password for the user===================

    lwr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
    upr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
    digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    spc = ["~", "!", "@", "#", "$", "%", "&", "*",
           "{", "}", "(", "0", "[", "]", "<", ">", "/"]
    char = [lwr, upr, digit, spc]

    Pass = ""
    # ===================Stores the password in string===================
    for i in range(random.randint(8, 17)):
        Pass += str(random.choice(random.choice(char)))
    password.insert(0, Pass)


def add():

    # ===================Saves the password in a json file===================
    # Checks for the availability of required fields
    if website.get() == "" or username.get() == "" or password.get() == "":
        tmsg.showinfo(title="Error", message="All fields are mandatory")

    else:

        # ===================Asks for confirmation before saving===================
        cnf = tmsg.askyesno(
            title="Confirm", message="Are you sure to save these data/credentials")
        if cnf:

            # ===================If found true===================
            with open(File_Path, "r") as file:
                # Reads the data and update the data
                old_data = json.load(file)
                # print(old_data)
                old_data[(crptgrph.encrypt(username.get()))] = {
                    "Website": (crptgrph.encrypt(website.get())),
                    "Password": (crptgrph.encrypt(password.get()))
                }

            with open(File_Path, "w") as file:
                # ===================Saves the Updated data===================
                json.dump(old_data, file, indent=4)
                website.delete(0, END)
                username.delete(0, END)
                password.delete(0, END)


def find_pass():
    # ===================Finds password and website name by taking username===================
    msg = ""

    if username.get():
        try:
            with open(File_Path, "r") as file:
                # ===================Opens the file in read mode===================
                content = json.load(file)
                content = content[crptgrph.encrypt(username.get())]
                msg += "Website: " + \
                    (crptgrph.decrypt(content["Website"])) + "\n"
                msg += "Username: " + (crptgrph.decrypt(username.get())) + "\n"
                msg += "Password: " + \
                    (crptgrph.decrypt(content["Password"])) + "\n"
                website.insert(0, (crptgrph.decrypt(content["Website"])))
                password.insert(0, (crptgrph.decrypt(content["Password"])))
                # print(content)

        except KeyError:
            tmsg.showinfo("Key Error", "No Such Data Exists in Our Databas")

        else:
            tmsg.showinfo(title="Found", message=msg)

    else:
        # ===================Shows a warning to give username input===================
        tmsg.showwarning(title="Invalid Operation",
                         message="Invalid Operation\nEnter Username/ UID for successful operation")


def refresh():
    # ===================Clear Entry Label===================
    website.delete(0, END)
    password.delete(0, END)
    username.delete(0, END)


# ========================Foreground Image============================

image = Image.open(
    "I:/Users/Aditya Pathak/Downloads/Documents/Tkinter/100-days/Lock.png")
pic = ImageTk.PhotoImage(image)
label = Label(image=pic)
label.place(x=25, y=63)

# ========================Text Labels============================

Label(text="Password Manager", font=("Arial", 40,
      "underline"), foreground="red").place(x=140)
Label(text="Website Name:", font=("Arial", 13)).place(x=100, y=500)
Label(text="Username:", font=("Arial", 13)).place(x=100, y=520)
Label(text="Password:", font=("Arial", 13)).place(x=100, y=540)

# ========================Entry Widget============================

website = Entry(width=30, relief="solid")
website.place(x=250, y=500)
username = Entry(width=30, relief="solid")
username.place(x=250, y=520)
password = Entry(width=30, relief="solid")
password.place(x=250, y=540)

# ========================Button Widget===========================

Button(text="Generate Password", command=gen_pass).place(
    x=475, y=560, width=110)
Button(text="Save", command=add).place(x=350, y=560, width=110)
Button(text="Find Password", command=find_pass).place(x=225, y=560, width=110)
Button(text="Clear Entry", command=refresh).place(x=100, y=560, width=110)

root.mainloop()
