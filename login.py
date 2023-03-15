from tkinter import *

root = Tk()
root.geometry("300x200")
root.title("Login")

# Labels
user_label = Label(root, text="Usuário:")
user_label.pack()
pass_label = Label(root, text="Senha:")
pass_label.pack()

# Inputs
user_input = Entry(root)
user_input.pack()
pass_input = Entry(root, show="*")
pass_input.pack()

# Login button
def login():
    username = user_input.get()
    password = pass_input.get()
    print("Username:", username)
    print("Password:", password)

login_button = Button(root, text="Login", command=login)
login_button.pack()

root.mainloop()
