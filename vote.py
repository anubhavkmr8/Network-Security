import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import crypto
from crypto.Util import Counter
from crypto import Random
from crypto.Util.number import *
import libnum

root = Tk()
auth_user = ["Topkek", "Bruh", "Moment", "Chad", "Bigoof", "BigShaq"]
uwu = {"Topkek": 327899108708369633, "Bruh": 542703099050939579, "Moment": 792236074464042287,
       "Chad": 648309335121487147, "Bigoof": 442097132972513201, "BigShaq": 430907665878862709}
existing_user = []
candidate = ["Bob Ross", "Van Gogh"]
candidate_res = {"Bob Ross": 0, "Van Gogh": 0}
msg = StringVar()
msg2 = StringVar()
bits = 30

f = open("user_priv.txt", "r")

for i in f:
    auth_user.append(i)

f.close()


def keygenerate():
    p = crypto.Util.number.getPrime(bits, randfunc=crypto.Random.get_random_bytes)
    q = crypto.Util.number.getPrime(bits, randfunc=crypto.Random.get_random_bytes)

    phi = (p - 1) * (q - 1)
    n = p * q

    e = 65537
    d = (libnum.invmod(e, phi))
    return ((e, n), (d, n))


def encrypt(privkkey, plaintext):
    key, n = privkkey
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher


def decrypt(pubkkey, ciphertext):
    key, n = pubkkey
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)


def public_enc(privkkey, data):
    key, n = privkkey
    S = [pow(i, key, n) for i in data]
    return S


def public_dec(pubkkey, data):
    key, n = pubkkey
    D = [pow(i, key, n) for i in data]
    return D


CTFpub, CTFpriv = keygenerate()
user_priv = (0, 0)
user_pub = (0, 0)


def check(oof, name):
    for i in oof:
        if i == name:
            return True
    return False


def getkey():
    msg2 = ip1.get("1.0", 'end-1c')
    msg = ip3.get("1.0", 'end-1c')
    msg = int(msg)
    pub = (65537, uwu[msg2])
    priv = (msg, uwu[msg2])
    return (pub, priv)


def BR():
    global user_priv
    global user_pub
    msg = ip1.get("1.0", 'end-1c')
    if check(auth_user, msg):
        if check(existing_user, msg) == False:
            user_pub, user_priv = getkey()
            pt = "Bob Ross"
            user_sign = encrypt(user_priv, pt)
            ct_enc = public_enc(CTFpub, user_sign)
            ct_dec = public_dec(CTFpriv, ct_enc)
            user_dec = decrypt(user_pub, ct_dec)
            if user_dec == pt:
                candidate_res["Bob Ross"] += 1
                existing_user.append(msg)


def VG():
    global user_priv
    global user_pub
    msg = ip1.get("1.0", 'end-1c')
    if check(auth_user, msg):
        if check(existing_user, msg) == False:
            user_pub, user_priv = getkey()
            pt = "Van Gogh"
            user_sign = encrypt(user_priv, pt)
            ct_enc = public_enc(CTFpub, user_sign)
            ct_dec = public_dec(CTFpriv, ct_enc)
            user_dec = decrypt(user_pub, ct_dec)
            if user_dec == pt:
                candidate_res["Van Gogh"] += 1
                existing_user.append(msg)


def get_result():
    ip2.delete("1.0", 'end-1c')
    for i in candidate:
        upd = i + " " + str(candidate_res[i])
        ip2.insert(END, upd + '\n')


frame1 = Frame(root)
frame1.pack()
ip1 = Text(frame1, height=2, width=100)
ip1.insert(INSERT, "Enter your name")
ip1.pack(side=LEFT, fill=BOTH, expand=YES)

frame2 = Frame(root)
frame2.pack()
ip3 = Text(frame2, height=1, width=200)
ip3.insert(INSERT, "Enter your private key")
ip3.pack(side=LEFT, fill=BOTH, expand=YES)

frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)
frame6 = Frame(root)
frame7 = Frame(root)
frame8 = Frame(root)
frame3.pack()
frame4.pack()
frame5.pack()
frame6.pack()
frame7.pack()
frame8.pack()

br = Button(frame3, text="Bob Ross", command=BR)
br.pack(side=LEFT)
vg = Button(frame4, text="Van Gogh", command=VG)
vg.pack(side=LEFT)
# kr = Button(frame5, text = "Keanu Reeves", command = KR)
# kr.pack(side = LEFT)
# ms = Button(frame6, text = "Michael Scott", command = MS)
# ms.pack(side = LEFT)
ip2 = Text(frame7, height=4, width=100)
ip2.pack(side=LEFT, fill=BOTH, expand=YES)
result = Button(frame8, text="RANKING", command=get_result)
result.pack(side=RIGHT)
root.mainloop()
