from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import os
from stegano import lsb

root = Tk()
root.title("Steganography")
root.geometry("1030x800")
root.resizable(width=False, height=False)
root.configure(background='black')

# Function to select an image file
def select_image():
    try:
        global filename
        filename = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select file",
            filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*"))
        )
        if filename:
            img = Image.open(filename)
            img = ImageTk.PhotoImage(img)
            lb1.configure(image=img, width=350, height=350)
            lb1.image = img
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while selecting the image: {str(e)}")

# Function to save the encoded image
def save_image():
    try:
        if 'secret' not in globals():
            raise Exception("No image to save. Please encode a message first.")
        save_path = filedialog.asksaveasfilename(
            initialdir=os.getcwd(),
            title="Save Image",
            defaultextension=".png",
            filetypes=(("png files", "*.png"), ("all files", "*.*"))
        )
        if save_path:
            secret.save(save_path)
            clear_all()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the image: {str(e)}")

# Function to decode the hidden message in the image
def decode():
    try:
        if 'filename' not in globals():
            raise Exception("No image selected. Please select an image first.")
        clear_message = lsb.reveal(filename)
        txt.delete("1.0", END)
        txt.insert(END, clear_message)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while decoding the message: {str(e)}")

# Function to encode a message into the image
def encode():
    try:
        if 'filename' not in globals():
            raise Exception("No image selected. Please select an image first.")
        message = txt.get("1.0", END)
        global secret
        secret = lsb.hide(filename, message)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while encoding the message: {str(e)}")

# Function to clear the image and text
def clear_all():
    lb1.configure(image=None)
    txt.delete("1.0", END)

# GUI setup
Label(root, text="Steganography", font="arial 25 bold", fg="red", bg="black").place(x=395, y=10)

f = Frame(root, width=500, height=400, bg="white", relief=GROOVE)
f.place(x=10, y=80)

lb1 = Label(f, bg="white")
lb1.place(x=40, y=10)

f2 = Frame(root, width=500, height=400, bg="white", relief=GROOVE)
f2.place(x=520, y=80)

txt = Text(f2, font="arial 25 bold", width=50, height=10, relief=GROOVE, wrap=WORD)
txt.place(x=0, y=0, width=500, height=400)

Scrollbar = Scrollbar(f2)
Scrollbar.place(x=480, y=0, height=400)
Scrollbar.config(command=txt.yview)
txt.config(yscrollcommand=Scrollbar.set)

f3 = Frame(root, bd=3, width=500, height=200, bg="black", relief=GROOVE)
f3.place(x=10, y=500)

Button(f3, text="Select Image", font="arial 15 bold", width=11, height=2, fg="red", bg="white", command=select_image).place(x=40, y=60)
Button(f3, text="Save Image", font="arial 15 bold", width=11, height=2, fg="red", bg="white", command=save_image).place(x=310, y=60)
Label(f3, text="Picture Option", font="arial 15 bold", fg="yellow", bg="black").place(x=175, y=10)

f4 = Frame(root, bd=3, width=500, height=200, bg="black", relief=GROOVE)
f4.place(x=520, y=500)

Button(f4, text="Encode", font="arial 15 bold", width=11, height=2, fg="red", bg="white", command=encode).place(x=40, y=60)
Button(f4, text="Decode", font="arial 15 bold", width=11, height=2, fg="red", bg="white", command=decode).place(x=310, y=60)
Label(f4, text="Encode/Decode", font="arial 15 bold", fg="yellow", bg="black").place(x=175, y=10)

root.mainloop()
