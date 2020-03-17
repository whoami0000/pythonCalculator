from tkinter import *

def yaz(x):
    s = len(giris.get())
    giris.insert(s,str(x))
    #print(x)

hesap = 5
s1 = 0

def islemler(x):
    global hesap
    hesap = x
    global s1
    s1 = float(giris.get())
    print(hesap)
    print(s1)
    giris.delete(0,'end')

s2 = 0
def hesapla():
    global s2
    s2 = float(giris.get())
    print(s2)
    global hesap
    sonuc=0
    if (hesap==0):
        sonuc = s1+s2
    elif(hesap==1):
        sonuc = s1-s2
    elif (hesap == 2):
        sonuc = s1 * s2
    elif (hesap == 3):
        sonuc = s1 / s2
    giris.delete(0,'end') #temizledikten sonra;
    giris.insert(0,str(sonuc)) # sonucu yaz


window = Tk()
window.geometry("250x300")

giris = Entry(font="Verdana 14 bold",width=15,justify="right")
giris.place(x=20,y=20)

buttonArray = []

for i in range(1,10):
    buttonArray.append(Button(text=str(i),font="Verdana 14 bold",command=lambda x=i:yaz(x)))

count=0

for i in range(0,3):
    for j in range(0,3):
        buttonArray[count].place(x=20+j*50,y=50+i*50)
        count+=1

islemArray = []

for i in range(0,4):
    islemArray.append(Button(font="Verdana 14 bold",command = lambda x=i:islemler(x))) #width = 2 diyerek hepsini aynı boyutta yapabiliriz butonları

islemArray[0]['text'] = "+"
islemArray[1]['text'] = "-"
islemArray[2]['text'] = "*"
islemArray[3]['text'] = "/" #tkinter butona göre boyut ayarlıyor.

for i in range(0,4):
    islemArray[i].place(x=170,y=50+50*i)

sb = Button(text="0",font="Verdana 14 bold",command=lambda x=0:yaz(x)) #sıfır butonu
sb.place(x=20,y=200)

nb = Button(text=".",font="Verdana 14 bold",width=1,command=lambda x=".":yaz(x)) #nokta butonu
nb.place(x=70,y=200)

eb = Button(text="=", fg = "RED" ,font="Verdana 14 bold",width=1,command=hesapla) # eşittir butonu
eb.place(x=120,y=200)

window.mainloop()