from tkinter import *


def Encrypt():
    dec.delete(1.0, END)
    s = enc.get("1.0", 'end-1c')
    ans = ""
    for i in s:
        if 'a' <= i <= 'z':
            i = chr(ord('z') + ord('a') - ord(i))
        elif 'A' <= i <= 'Z':
            i = chr(ord('A') + ord('Z') - ord(i))
        ans = ans + str(i)
    dec.insert(0.0, ans)


def Decrypt():
    enc.delete(1.0, END)
    s = dec.get("1.0", 'end-1c')
    ans = ""
    for i in s:
        if 'a' <= i <= 'z':
            i = chr(219 - ord(i))
        elif 'A' <= i <= 'Z':
            i = chr(155 - ord(i))
        ans = ans + str(i)
    enc.insert(0.0, ans)


root = Tk()
root.geometry("1000x600")
root.title('Atbash Cipher')

frame1 = Frame(root)
frame2 = Frame(root)

frame1.grid(row=0, column=0, sticky=W)
frame2.grid(row=0, column=1, sticky=E)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

enc = Text(frame1, height=30, width=75, wrap=WORD)
enc.insert(INSERT, 'Enter the text to be encrypted')
dec = Text(frame2, height=30, width=75, wrap=WORD)
dec.insert(INSERT, "Enter the text to be decrypted")
enc.grid(sticky=W)
dec.grid(sticky=E)

btn1 = Button(frame1, text='Encrypt', bg="purple", fg="white", command=Encrypt)
btn2 = Button(frame2, text='Decrypt', bg="green", fg="white", command=Decrypt)
btn1.grid(sticky=S)
btn2.grid(sticky=S)

root.mainloop()
