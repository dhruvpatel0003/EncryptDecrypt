from tkinter import *
from tkinter import messagebox
# from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import Toplevel
FONT = ("Arial", 18, "bold")
key = 2

window = Tk()
window.config(bg="blue",width=400,height=500,padx=50,pady=50)
window.title("Encrypt to Decrypt")

def clearE():
    text_box1.delete(1.0,"end-1c")

def clearD():
    text_box2.delete(1.0,"end-1c")

def encrypt():
    q_ = text_box1.get(1.0,"end-1c")
    go_encrypt(q_)

def go_encrypt(string):
    # print(string)
    str = ''
    for i in range(0, len(string)):
        position = ord(string[i]) + key

        if position > 90 and position < 100:
            str += chr(90 - 26 + (key - (90 - ord(string[i]))))
        elif position > 122:
            str += chr(122 - 26 + (key - (122 - ord(string[i]))))
        else:
            str += chr(position)

    text_box2.insert(END, f"{str}")

def go_decrypt():
    string = text_box2.get(1.0,"end-1c")
    str = ''
    for i in string:
        position = ord(i) - key
        print("Inside the function", position)
        if position < 65 and i.isalpha():
            str += chr(90 - (65 - position - 1))
        elif position < 97 and i.isalpha():
            str += chr(122 - (97 - position - 1))
        else:
            str += chr(position)

    text_box1.insert(END,f"{str}")

text_box1 = Text(window,width=50,height=10,bg="white",font=FONT,highlightcolor="black",highlightthickness=10,highlightbackground="black")
text_box1.focus()
text_box1.insert(END,'')
text_box1.grid(row=0,column=0)

text_box2 = Text(width=50,height=10,bg="white",font=FONT,highlightcolor="black",highlightthickness=10,highlightbackground="black")
text_box2.grid(row=0,column=2)

button_encrypt = Button(text="Encrypt",fg="black",bg="white",font=FONT,command=encrypt)
button_encrypt.grid(row=2,column=0)

button_decrypt = Button(text="Decrypt",fg="black",bg="white",font=FONT,command=go_decrypt)
button_decrypt.grid(row=2,column=2)

clear_buttonE = Button(text="ClearE",fg='black',bg="white",font=FONT,command=clearE,borderwidth=10)
clear_buttonE.grid(row=3,column=1)

clear_buttonD = Button(text="ClearD",fg='black',bg="white",font=FONT,command=clearD,borderwidth=10)
clear_buttonD.grid(row=4,column=1)

name_lable = Label(width=50,height=10,text="DhruvPatel",font=("Arial",15,"bold"))
name_lable.grid(row=9,column=0,columnspan=6)


def click():
    content = askopenfile(mode='r', filetypes=[('Text File', '*.txt')])
    go_encrypt((content.read()))


menubar = Menu(window)
sub_menu = Menu(menubar)
filemenu = sub_menu.add_command(label="File",command=click)
sub_menu.add_separator()
sub_menu.add_command(label="Cancle",command=window.quit)
menubar.add_cascade(label="File",menu=sub_menu)
window.config(menu=menubar)

def help_():
    messagebox.showinfo("Help","You are not allow to take help ")
sub_menu2 = Menu(menubar)
sub_menu2.add_command(label="Help",command=help_)
menubar.add_cascade(label="Help",menu=sub_menu2)
window.config(menu=menubar)

window.mainloop()