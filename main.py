from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from stegano import lsb
import datetime

root=Tk()
root.title("Steganography")
root.geometry("1030x1100")
root.resizable(width=False, height=False)
root.configure(background='black')


def select_image():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",
                                        filetypes=(("png files", "*.png"),("jpg files", "*.jpg"),("all files", "*.txt")))
    img=Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lb1.configure(image=img,width=350,height=350)
    lb1.image=img


def save_image():
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.basename(filename)
    save_path = f"secret_{base_name}_{current_time}.png"
    secret.save(save_path)
    clear_all()


def decode():
    global clear_message
    clear_message = lsb.reveal(filename)
    txt.delete("1.0",END)
    txt.insert(END,clear_message)


def encode():
    global secret
    message = txt.get("1.0",END)
    secret = lsb.hide(filename,message)

def clear_all():
    lb1.configure(image=None)
    txt.delete("1.0", END)

Label(root,text="Steganography",font="arial 25 bold",fg="red",bg="black").place(x=395,y=10)

#first frame
f=Frame(root,width=500,height=400,bg="white",relief=GROOVE)
f.place(x=10,y=80)

lb1 = Label(f,bg="white")
lb1.place(x=40,y=10)

#2 frame
f2=Frame(root,width=500,height=400,bg="white",relief=GROOVE)
f2.place(x=520,y=80)

txt = Text(f2,font="arial 25 bold",width=50,height=10,relief=GROOVE,wrap=WORD)
txt.place(x=0,y=0,width=500,height=400)

Scrollbar=Scrollbar(f2)
Scrollbar.place(x=480,y=0,height=400)
Scrollbar.config(command=txt.yview)
txt.config(yscrollcommand=Scrollbar.set)

#3rd frame
f3=Frame(root,bd=3,width=500,height=200,bg="black",relief=GROOVE)
f3.place(x=10,y=500)

Button(f3,text="Select Image",font="arial 15 bold",width=11,height=2,fg="red",bg="white",command=select_image).place(x=40,y=60)
Button(f3,text="Save Image",font="arial 15 bold",width=11,height=2,fg="red",bg="white",command=save_image).place(x=310,y=60)
Label(f3,text="Picture Option",font="arial 15 bold",fg="yellow",bg="black").place(x=175,y=10)

#4th frame
f4=Frame(root,bd=3,width=500,height=200,bg="black",relief=GROOVE)
f4.place(x=520,y=500)

Button(f4,text="Encode",font="arial 15 bold",width=11,height=2,fg="red",bg="white",command=encode).place(x=40,y=60)
Button(f4,text="Decode",font="arial 15 bold",width=11,height=2,fg="red",bg="white",command=decode).place(x=310,y=60)
Label(f4,text="Encode/Decode",font="arial 15 bold",fg="yellow",bg="black").place(x=175,y=10)

root.mainloop()