from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
import os

class AnaMenu:

    def __init__(self):
        self.acilan_sayfalar = []
        try:
            self.ayar_dosyasi = open(f"C:/Users/{os.getlogin()}/ayar_dosyasi.txt","r")
            
        except:
            self.ayar_dosyasi = open(f"C:/Users/{os.getlogin()}/ayar_dosyasi.txt","w+")
            self.ayar_dosyasi.write("boyut=15=yaziRenk=white=arkaplan_rengi=black")
            self.ayar_dosyasi.close()
            
            self.ayar_dosyasi = open(f"C:/Users/{os.getlogin()}/ayar_dosyasi.txt")

        self.ayarlar = self.ayar_dosyasi.readlines()
        self.ayar_dosyasi.close()
        
        self.pencere = tk.Tk()
        self.pencere.geometry("370x250")
        self.pencere.title("Metin Editörü")
        self.pencere.wm_iconbitmap('logo.ico')
        #self.pencere.overrideredirect(True)
        
        self.tabControl = ttk.Notebook(self.pencere)
        
        self.dosya = tk.Frame(self.tabControl)
        self.ayar = tk.Frame(self.tabControl)
        self.acilan_sayfalar.append(self.ayar)
        
        self.tabControl.add(self.dosya, text= ' Dosya ')
        self.tabControl.add(self.ayar, text= 'Ayarlar')
        self.tabControl.pack(expand = 1, fill = "both")
        
        ttk.Button(self.dosya,text = "Dosyayı Aç", command = self.dosya_ac).place(x = 0, y = 1)
        #ttk.Button(self.dosya,text = "Oluştur").place(x = 0, y = 24)

        tk.Button(self.ayar,text = "✓",fg = "red",bg = "white", command = self.boyutu_onayla, height=0).place(x = 220, y = 1)
        try:
            self.boyut_test = tk.Label(self.ayar,text = " Boyut ", bg = self.ayarlar[0].split("=")[5],fg = self.ayarlar[0].split("=")[3],font = ("classic",10))
        except:
            self.ayar_dosyasi = open(f"C:/Users/{os.getlogin()}/ayar_dosyasi.txt","w+")
            self.ayar_dosyasi.write("boyut=14=yaziRenk=red=arkaplan_rengi=purple")
            self.ayar_dosyasi = open(f"C:/Users/{os.getlogin()}/ayar_dosyasi.txt")
            self.ayarlar = self.ayar_dosyasi.readlines()
            self.boyut_test = tk.Label(self.ayar,text = " Boyut ", bg = self.ayarlar[0].split("=")[5],fg = self.ayarlar[0].split("=")[3],font = ("classic",10))

        
        self.boyut_test.pack(anchor='se', side = "top")
        
        ttk.Button(self.ayar,text = "   Yazı  Boyutu  ").place(x = 43, y = 1)
        self.yazi_boyut = tk.Entry(self.ayar, width = 8)
        self.yazi_boyut.place(x = 160,y = 1)
        self.yazi_boyut.insert(0,self.ayarlar[0].split("=")[1])

        ttk.Button(self.ayar,text = "   Yazı Rengi      ").place(x = 43, y = 23)
        self.yazi_rengi = tk.Entry(self.ayar, width = 8)
        self.yazi_rengi.place(x = 160,y = 25)
        self.yazi_rengi.insert(0,self.ayarlar[0].split("=")[3])
        
        ttk.Button(self.ayar,text = "Arkaplan Rengi").place(x = 43, y = 45)
        self.arkaplan_rengi = tk.Entry(self.ayar, width = 8)
        self.arkaplan_rengi.place(x = 160,y = 50)
        self.arkaplan_rengi.insert(0,self.ayarlar[0].split("=")[5])
        
        self.surekli_guncelle()
        self.pencere.mainloop()
        
    def boyutu_onayla(self):
        try:
            self.boyut_test["font"] = ("classic",int(self.yazi_boyut.get()))
            self.boyut_test["fg"] = self.yazi_rengi.get()
            self.boyut_test["bg"] = self.arkaplan_rengi.get()
            self.ayar_dosyası = open(f"C:/Users/{os.getlogin()}/ayar_dosyasi.txt","w+")
            self.ayar_dosyası.write("boyut="+str(self.yazi_boyut.get())+"=yaziRenk="+str(self.yazi_rengi.get())+"=arkaplan_rengi="+str(self.arkaplan_rengi.get()))
            self.ayar_dosyası.close()
        except:pass
        

    def surekli_guncelle(self):
        try:self.boyut_test["font"] = ("classic",int(self.yazi_boyut.get()))
        except:pass

        try:self.boyut_test["fg"] = self.yazi_rengi.get()
        except:pass

        try:self.boyut_test["bg"] = self.arkaplan_rengi.get()
        except:pass
        
        self.pencere.after(300,self.surekli_guncelle)

    def dosya_ac(self):
        try:
            self.secilen_dosya = filedialog.askopenfile(filetypes=(('Txt Dosyası', '.txt'),))

            dosyayi_oku = open(self.secilen_dosya.name,encoding = "utf-8")
            dosya_adi = self.secilen_dosya.name.split("/")[-1][:-4]

            self.ayar_dosyası = open(f"C:/Users/{os.getlogin()}/ayar_dosyasi.txt","r")
            self.ayar_boyutu = self.ayar_dosyası.readlines()
            
            self.acilan_dosya = ttk.Frame(self.pencere)
            self.acilan_dosya.pack_propagate(False)
            self.tabControl.add(self.acilan_dosya, text = dosya_adi)
            self.acilan_sayfalar.append(self.acilan_dosya)

            ttk.Button(self.acilan_dosya,text = "Kaydet", command = self.kaydet).place(x = 0, y = 0)
            ttk.Button(self.acilan_dosya,text = "X", command = lambda : self.kapat(self.tabControl.index('current')-1)).pack(anchor="ne")                
                        
            self.metin = ScrolledText(self.acilan_dosya,fg = self.ayar_boyutu[0].split("=")[3],bg = self.ayar_boyutu[0].split("=")[-1],font = ("Consolas",int(self.ayar_boyutu[0].split("=")[1])),width=1000, height=1000)
            self.metin.pack()

            for i in dosyayi_oku:
                self.metin.insert(tk.INSERT,i)
            
            self.tabControl.select(len(self.acilan_sayfalar))
        
        except:pass
        
    def kaydet(self):
        self.dosyayi_yaz = open(self.secilen_dosya.name,"w+",encoding = "utf-8")
        self.dosyayi_yaz.write(self.metin.get("1.0", tk.END))
        self.dosyayi_yaz.close()
        
    def kapat(self,index):
        self.acilan_sayfalar[index].destroy()
        self.acilan_sayfalar.remove(self.acilan_sayfalar[index])

uyg = AnaMenu()
