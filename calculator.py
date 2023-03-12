from tkinter import*
import tkinter.font as font
import math

expression = ""

root = Tk()
root.title("Kalkulator")
root["bg"] = "#EDE7F6"
root.geometry("325x425")

myfont  = font.Font(size=15)

e = Entry(root,width=25,borderwidth=0)
e["font"]= myfont
e["bg"] = "#EDE7F6"
e.grid(row = 0,columnspan=4,pady=20,padx=20)

def cetak(nilai):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)+str(nilai))
    
def tambah():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "penjumlahan"
    n_awal = float(nomor_awal)
    e.delete(0,END)
    
def kurang():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "pengurangan"
    n_awal = float(nomor_awal)
    e.delete(0,END)
    
def bagi():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "pembagian"
    n_awal = float(nomor_awal)
    e.delete(0,END)
    
def kali():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "perkalian"
    n_awal = float(nomor_awal)
    e.delete(0,END)

def pangkat():
    nomor_awal = e.get()
    global n_awal
    n_awal = float(nomor_awal)
    e.delete(0,END)
    e.insert(0,n_awal **2)

def hapus():
    e.delete(0,END)

def hapusperkarakter():
    e.delete(len(e.get())-1, END)

def samadengan():
    nomor_akhir = e.get()
    
    e.delete(0,END)
    if mtk == "penjumlahan":
        result = round(n_awal + float(nomor_akhir), 10)
        e.insert(0,result)
        
    elif mtk == "pengurangan":
        result = round(n_awal - float(nomor_akhir), 10)
        e.insert(0,result)
        
    elif mtk == "pembagian":
        try:
            hitung = round(n_awal / float(nomor_akhir), 10)
            e.insert(0,hitung)
            
        except ZeroDivisionError:
            e.insert(0,"Gabisa dibagi nol dong kak")
            
    elif mtk == "perkalian":
        result = round(n_awal * float(nomor_akhir), 10)
        e.insert(0,result)
    elif mtk == "sisabagi":
        e.insert(0,n_awal % float(nomor_akhir))
    
#perintah untuk membuat tombol angka dan decimal
button   = Button(root,text="1",padx = 30,bg="#9575CD",fg="white", pady = 20, command=lambda:cetak(1))
button2  = Button(root,text="2",padx = 30,bg="#9575CD",fg="white", pady = 20,command=lambda:cetak(2))
button3  = Button(root,text="3",padx = 30,bg="#9575CD",fg="white", pady = 20,command=lambda:cetak(3))
button4  = Button(root,text="4",padx = 30,bg="#9575CD",fg="white", pady = 20,command=lambda:cetak(4))
button5  = Button(root,text="5",padx = 30,bg="#9575CD",fg="white", pady = 20,command=lambda:cetak(5))
button6  = Button(root,text="6",padx = 30,bg="#9575CD",fg="white", pady = 20,command=lambda:cetak(6))
button7  = Button(root,text="7",padx = 30,bg="#9575CD",fg="white", pady = 20,command=lambda:cetak(7))
button8  = Button(root,text="8",padx = 30,bg="#9575CD",fg="white", pady = 20,command=lambda:cetak(8))
button9  = Button(root,text="9",padx = 30,bg="#9575CD",fg="white", pady = 20,command=lambda:cetak(9))
button0  = Button(root,text="0",padx = 30,bg="#9575CD",fg="white", pady = 20,command=lambda:cetak(0))
decimal  = Button(root,text=".",padx = 30,bg="#B39DDB",fg="white", pady = 20,command=lambda: cetak('.'))

#perintah untuk membuat tombol operator
tam = Button(root,text="+",padx = 30,bg="#B39DDB",fg="white", pady = 20,command=tambah)
kur = Button(root,text="-",padx = 30,bg="#B39DDB",fg="white", pady = 20,command=kurang)
bag  = Button(root,text="/",padx = 30,bg="#B39DDB",fg="white", pady = 20,command=bagi)
kal = Button(root,text="X",padx = 30,bg="#B39DDB",fg="white", pady = 20,command=kali)
pang = Button(root,text="^2",padx = 30,bg="#B39DDB",fg="white", pady = 20,command=pangkat)

hap = Button(root,text="C",padx = 30,bg="#B39DDB",fg="white", pady = 20,command=hapus)
equal = Button(root,text="=",padx = 70,bg="skyblue", pady = 20,command=samadengan)
delete = Button(root,text="Del",padx = 30,bg="#B39DDB",fg="white", pady = 20,command=hapusperkarakter)

#perintah untuk menempatkan tombol angka dan decimal
button.grid(row=3,column=0,pady=2)
button2.grid(row=3,column=1,pady=2)
button3.grid(row=3,column=2,pady=2)
button4.grid(row=2,column=0,pady=2)
button5.grid(row=2,column=1,pady=2)
button6.grid(row=2,column=2,pady=2)
button7.grid(row=1,column=0,pady=2)
button8.grid(row=1,column=1,pady=2)
button9.grid(row=1,column=2,pady=2)
button0.grid(row=4,column=1,pady=2)
decimal.grid(row=4,column=0, pady=2)

#perintah untuk menempatkan tombol operator
tam.grid(row=2,column=3,pady=2)
kur.grid(row=3,column=3,pady=2)
bag.grid(row=4,column=2,pady=2)
kal.grid(row=4,column=3,pady=2)
hap.grid(row=1,column=3,pady=2)
equal.grid(row=5,column=2,columnspan=2)
pang.grid(row =5,column=0,pady=2)
delete.grid(row=5,column=1,pady=2)


root.mainloop()