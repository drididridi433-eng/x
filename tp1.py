from PyQt5.uic import *
from PyQt5.QtWidgets import *
from random import*
from pickle import dump,load
from numpy import array
t=array([dict()]*100)
def remplir():
    ch=w.ln.text()
    if not(int(ch)>2 or ch.isdecimal()):
        QMessageBox.critical(w,"erreur","verifier n")
    else:
        f=open("entier.txt","w")
        x=randint(10,99999)
        f.write(str(x)+'\n')
        f.close()
        QMessageBox.information(w,"succes","fichier remplit")
def affiche_texte():
    w.lw.clear()
    r1=w.r1.isChecked()
    r2=w.r2.isChecked()
    if(r1):
        w.lw.addItem('totale')
        f=open("entier.txt","r")
        ch=f.read()
        w.lw.addItem(ch)
    else:
        w.lw.addItem("ligne par ligne")
        f=open("entier.txt","r")
        lig=f.readline()
        while(lig!=""):
            lig=lig[:len(lig)-1]
            w.lw.addItem(lig+'\n')
            ch=f.readline()
        f.close()
def generer():
    f=open("entier.txt","r")
    n=0
    lig=f.readline()
    while(lig!=""):
        lig=lig[:len(lig)-1]
        t[n]=int(lig)
        n=+1
        lig=f.readline()
    f.close()
    ok=True
    while(ok):
        ok=False
        for i in range(n-1):
            if(t[i]<t[i+1]):
                a=t[i]
                t[i]=t[i+1]
                t[i+1]=a
                ok=True
          
    f2=open("tri.dat","wb")
    for i in range(n):
        e=dict()
        x=t[i]
        e["nb"]=x
        e["inverse"]=inverse(str(x))
        dump(e,f2)
    f2.close()
    QMessageBox.information(w,"succes","tri realisie")
def inverse(x):
    ch=""
    for i in range(len(x)):
        ch=x[i]+ch
def afficher_bin():
    f2=open("tri.dat","rb")
    l=0
    s=0
    fin=False
    while not fin:
        try:
            e=load(f2)
            w.tw.InsertRow(l)
            w.tw.setItem(l,0,QtableWidgetItem(str(e['nb'])))
            w.tw.setItem(l,1,QtableWidgetItem(str(e['inverse'])))
            l=l+1
            s=s+e['nb']
            
        except:
            fin=True
    f2.close()
    rs=w.res.setText(str(s))
def effacer():
    w.ln.clear()
    w.lw.clear()
    w.tw.setRowCount(0)
def quitter():
    w.close()

app = QApplication([])
w= loadUi ("C:/Users/dridi/Desktop/mtp/classe/tp1.ui")
w.show()
w.bt1.clicked.connect ( remplir)
w.bt2.clicked.connect (generer )
w.bt4.clicked.connect ( affiche_texte)
w.bt3.clicked.connect ( effacer )
w.bt5.clicked.connect ( afficher_bin )
w.bt6.clicked.connect (quitter )

app.exec_()