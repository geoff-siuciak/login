from passlib.context import CryptContext
import pandas as pd
from tkinter import *
from tkinter import font
from tkinter import Entry


def login():
    hpContent.pack_forget()
    loginContent.pack()


def newUser():
    hpContent.pack_forget()
    newUserContent.pack()


def loginBack():
    clearEntry()
    loginContent.pack_forget()
    hpContent.pack()


def clearEntry():
    userName.delete(first=0, last=15)
    passWord.delete(first=0, last=15)


def newUserBack():
    newUserContent.pack_forget()
    hpContent.pack()
    clearNewEntry()


def clearNewEntry():
    userName_n.delete(first=0, last=15)
    passWord_n.delete(first=0, last=15)
    passWord2_n.delete(first=0, last=15)


def mainInvalid():
    loginContent.pack_forget()
    invalidLogin.pack()


def okMain():
    invalidLogin.pack_forget()
    loginContent.pack()


def ok():
    badPassContent.pack_forget()
    newUserContent.pack()


def checkNewUserPass():
    user_name = str(userName_n.get())
    pass_word = str(passWord_n.get())
    pass_word_confirm = str(passWord2_n.get())

    userNames = pd.read_csv('user_data.log',
                            header=None)
    nameList = userNames.iloc[:, 0].tolist()
    userExists = nameList.count(user_name)

    if pass_word == pass_word_confirm and 3 <= len(user_name) <= 15 and userExists == 0:

        hashed_pass_word = encrypt_password(pass_word)

        with open('user_data.log', 'a') as f:
            print(user_name, file=f)
        with open('key_data.log', 'a') as f:
            print(hashed_pass_word, file=f)

        newUserBack()

    else:
        newUserContent.pack_forget()
        badPassContent.pack()


def enter():
    user_name = str(userName.get())
    pass_word = str(passWord.get())

    userNames = pd.read_csv('user_data.log',
                            header=None)
    keys = pd.read_csv('key_data.log',
                       header=None)

    nameList = userNames.iloc[:, 0].tolist()
    keysList = keys.iloc[:, 0].tolist()

    if user_name in nameList:
        index = nameList.index(user_name)
        hashed = keysList[index]
        if check_encrypted_password(pass_word, hashed) is True:
            print("login successful")
            hp.destroy()
            exit()
        else:
            mainInvalid()
    else:
        mainInvalid()


# passlib default setup
pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000)


def encrypt_password(password):
    return pwd_context.encrypt(password)


def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)


# Password GUI homepage
# Window and title block frame
hp = Tk()
hp.title("getPing")
hp.configure(background='black')

# fonts
titleFont = font.Font(family="Helvetica", size=18, slant="italic")
labelFont = font.Font(family="Helvetica", size=12, slant="italic")

# homepage content frame
hpContent = Frame(hp)
hpContent.config(background='black')
mainLabel = Label(hpContent, text="login", font=titleFont,
                  bg="black", fg="white", width=15, height=4)
mainLabel.pack()
button1 = Button(hpContent, text='login', command=lambda: login(), width=15, height=1,
                 font=labelFont, bg="black", state="normal", fg="white")
button1.pack()
button2 = Button(hpContent, text='new user', command=lambda: newUser(), width=15, height=1,
                 font=labelFont, bg="black", state="normal", fg="white")
button2.pack()
bottomLabel = Label(hpContent, bg="black", width=20, height=3)
bottomLabel.pack()

# initialize with homepage frame packed
hpContent.pack()

# new user frame
newUserContent = Frame(hp)
newUserContent.config(background='black')
mainLabel = Label(newUserContent, text="login", font=titleFont,
                  bg="black", fg="white", width=15, height=4)
mainLabel.pack()
unLabel = Label(newUserContent, text="user name", font=labelFont,
                bg="black", fg="white", width=15, height=1)
unLabel.pack()

userName_n = Entry(newUserContent, width=20)
userName_n.pack()

pwLabel_n = Label(newUserContent, text="password", font=labelFont,
                  bg="black", fg="white", width=15, height=1)
pwLabel_n.pack()
passWord_n = Entry(newUserContent, width=20, show="*")
passWord_n.pack()

pwLabel2_n = Label(newUserContent, text="re-enter password", font=labelFont,
                   bg="black", fg="white", width=15, height=1)
pwLabel2_n.pack()
passWord2_n = Entry(newUserContent, width=20, show="*")
passWord2_n.pack()

spaceLabel = Label(newUserContent, bg="black", width=20, height=2)
spaceLabel.pack()

confirmButton = Button(newUserContent, text='confirm', font=labelFont,
                       bg="black", fg="white", width=15, height=1,
                       command=lambda: checkNewUserPass())
confirmButton.pack()

backButton = Button(newUserContent, text='back', font=labelFont,
                    bg="black", fg="white", width=15, height=1,
                    command=lambda: newUserBack())
backButton.pack()

bottomLabel2 = Label(newUserContent, bg="black", width=20, height=3)
bottomLabel2.pack()

# login frame
loginContent = Frame(hp)
loginContent.config(background='black')
mainLabel = Label(loginContent, text="login", font=titleFont,
                  bg="black", fg="white", width=15, height=4)
mainLabel.pack()
unLabel = Label(loginContent, text="user name", font=labelFont,
                bg="black", fg="white", width=15, height=1)
unLabel.pack()
userName = Entry(loginContent, width=20)
userName.pack()

pwLabel = Label(loginContent, text="password", font=labelFont,
                bg="black", fg="white", width=15, height=1)
pwLabel.pack()
passWord = Entry(loginContent, width=20, show="*")
passWord.pack()

spaceLabel = Label(loginContent, bg="black", width=20, height=2)
spaceLabel.pack()

enterButton = Button(loginContent, text='enter', font=labelFont,
                     bg="black", fg="white", width=15, height=1,
                     command=lambda: enter())
enterButton.pack()

backButton = Button(loginContent, text='back', font=labelFont,
                    bg="black", fg="white", width=15, height=1,
                    command=lambda: loginBack())
backButton.pack()

bottomLabel2 = Label(loginContent, bg="black", width=20, height=3)
bottomLabel2.pack()

# invalid password frame
badPassContent = Frame(hp)
badPassContent.config(background='black')
mainLabel = Label(badPassContent, text="login", font=titleFont,
                  bg="black", fg="white", width=15, height=4)
mainLabel.pack()
errorLabel = Label(badPassContent, text="invalid entry", font=labelFont,
                   bg="red", fg="black", width=15, height=1)
errorLabel.pack()
okButton = Button(badPassContent, text='ok', font=labelFont,
                  bg="black", fg="white", width=15, height=1,
                  command=lambda: ok())
okButton.pack()
bottomLabel2 = Label(badPassContent, bg="black", width=20, height=3)
bottomLabel2.pack()

# main login invalid entry
invalidLogin = Frame(hp)
invalidLogin.config(background='black')
mainLabel = Label(invalidLogin, text="login", font=titleFont,
                  bg="black", fg="white", width=15, height=4)
mainLabel.pack()
errorLabel = Label(invalidLogin, text="invalid entry", font=labelFont,
                   bg="red", fg="black", width=15, height=1)
errorLabel.pack()
okButton_main = Button(invalidLogin, text='ok', font=labelFont,
                       bg="black", fg="white", width=15, height=1,
                       command=lambda: okMain())
okButton_main.pack()
bottomLabel2 = Label(invalidLogin, bg="black", width=20, height=3)
bottomLabel2.pack()

hp.mainloop()
