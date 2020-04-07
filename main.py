import tkinter as tk
from random import randint

ascii_test = ["!", "'", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5",
              "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
              "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]", "^", "_",
              "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z", "{", "|", "}", "~"]
pw = ""


def gen_password():
    global pw
    pw = ""
    for i in range(int(e1.get())):
        pw = pw + ascii_test[randint(0, 94)]
    e2.delete(0, tk.END)
    e2.insert(0, pw)


master = tk.Tk()

tk.Label(master,
         text="Password Length").grid(row=0)
tk.Label(master,
         text="Your Password").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)

tk.Button(master,
          text='Generate Password', command=gen_password).grid(row=3,
                                                               column=1,
                                                               sticky=tk.W,
                                                               pady=4)

tk.mainloop()
