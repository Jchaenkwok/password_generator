import tkinter as tk
from random import randint

# List
ascii_tuple = ("!", "'", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5",
               "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
               "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]", "^", "_",
               "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
               "u", "v", "w", "x", "y", "z", "{", "|", "}", "~")
pw = ""


def gen_password():
    global pw
    pw = ""
    for i in range(int(e1.get())):
        pw = pw + ascii_tuple[randint(0, 93)]
    e2.delete(0, tk.END)
    e2.insert(0, pw)


def copy_password():
    master.clipboard_clear()
    master.clipboard_append(e2.get())
    master.update()


def fix():
    a = master.winfo_geometry().split('+')[0]
    b = a.split('x')
    w = int(b[0])
    h = int(b[1])
    master.geometry('%dx%d' % (w + 1, h + 1))


master = tk.Tk()

master.title('Password Generator')

tk.Label(master,
         text="Password Length").grid(row=0)
tk.Label(master,
         text="Your Password").grid(row=1)

# Create two entry objects
e1 = tk.Entry(master)
e2 = tk.Entry(master)

# Set entry object position
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# Quit button
tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
# Button to generate as password
tk.Button(master,
          text='Generate Password',
          command=gen_password).grid(row=3,
                                     column=1,
                                     sticky=tk.W,
                                     pady=4)
# Button to copy password to keyboard
tk.Button(master,
          text='Copy Password',
          command=copy_password).grid(row=3,
                                      column=2,
                                      sticky=tk.W,
                                      pady=4)

master.update()
master.after(0, fix)
tk.mainloop()
