import numpy as np
from scipy import signal as sp
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from tkinter import messagebox
import time

inicio = Tk()
inicio.title("Inicio")
inicio.configure(bg="grey12")

fr = LabelFrame(inicio, font= 40, text="LABORATORIO 1: GENERACIÓN Y\nOPERACIÓN DE SEÑALES", fg="goldenrod1", bg="grey12", padx=50, pady=60)
fr.pack(padx=5, pady=5) 

nom = Label(fr, text="Señales y sistemas\nDavid Eduardo Díaz de Moya\nProfesor:\nPedro Juan Narvaez Rosado", fg="goldenrod1", bg="grey12").grid(row=0,column=0)

def cerrar():
    menu=Tk()
    menu.title("Menu")
    menu.configure(bg="grey12")        
    t = np.arange(0,10,0.01)
    fr2=Frame(menu, bg="grey12", padx=10, pady=10)
    fr2.grid(row=0,column=0)
    fr8=Frame(menu, bg="grey12", padx=10, pady=10)
    fr8.grid(row=0,column=2)
    fr20=Frame(menu, bg="grey12", padx=10, pady=10)
    fr20.grid(row=0,column=1)
    fr9=LabelFrame(fr8, text="", bg="grey12", padx=10, pady=10)
    fr9.grid(row=3,column=0)
    fr90=Frame(menu, bg="grey12", padx=10, pady=10)
    fr90.grid(row=0,column=3)
    fr80=LabelFrame(fr90, bg="grey12", padx=10, pady=10)
    fr80.grid(row=0,column=3)
    
    fr7=LabelFrame(fr2, text="Seleccione x(t)/x[n]:", bg="grey12", fg="goldenrod1", padx=26, pady=20)
    fr7.grid(row=1,column=0)
    
    fr70=LabelFrame(fr20, text="Seleccione h(t)/h[n]:", bg="grey12", fg="goldenrod1", padx=26, pady=20)
    fr70.grid(row=1,column=0)
    
    str1 = StringVar(menu)
    str1.set("Parametro 1")
    str2 = StringVar(menu)
    str2.set("Parametro 2")
    str3 = StringVar(menu)
    str3.set("Parametro 3")
    str4 = StringVar(menu)
    str4.set("Parametro 4")
    str10 = StringVar(menu)
    str10.set("Parametro 1")
    str20 = StringVar(menu)
    str20.set("Parametro 2")
    str30 = StringVar(menu)
    str30.set("Parametro 3")
    str40 = StringVar(menu)
    str40.set("Parametro 4")
    fun = StringVar(menu)
    funh = StringVar(menu)
    eee = StringVar(menu)
    ee = StringVar(menu)
    
    global adver
    adver = 1
    
    
    
    def parametros(num):
        global nm
        nm = int(num)
        if nm == 1:
            str1.set("Amplitud")
            str2.set("Periodo")
            str3.set("")
            str4.set("")
            ent1.configure(state=NORMAL)
            ent2.configure(state=NORMAL)
            ent3.configure(state=DISABLED)
            ent44.configure(state=DISABLED)
            fun.set("Sinusoidal")
            y = np.sin((2*np.pi/10)*t)
        if nm == 2:
            str1.set("Amplitud")
            str2.set("Periodo")
            str3.set("")
            str4.set("")
            ent1.configure(state=NORMAL)
            ent2.configure(state=NORMAL)
            ent3.configure(state=DISABLED)
            ent44.configure(state=DISABLED)
            fun.set("Triangular")
            y = sp.sawtooth(t*2*np.pi/10,0.5)
        if nm == 3:
            str1.set("Amplitud")
            str2.set("Periodo")
            str3.set("")
            str4.set("")
            ent1.configure(state=NORMAL)
            ent2.configure(state=NORMAL)
            ent3.configure(state=DISABLED)
            ent44.configure(state=DISABLED)
            fun.set("Rectangular")
            y = sp.square(t*2*np.pi/10,0.5)
        if nm == 4:
            str1.set("Amplitud")
            str2.set("Exponente")
            str3.set("Inicio")
            str4.set("Fin")
            ent1.configure(state=NORMAL)
            ent2.configure(state=NORMAL)
            ent3.configure(state=NORMAL)
            ent44.configure(state=NORMAL)
            fun.set("Exponencial")
            y = np.exp(t)
        if nm == 5:
            str1.set("Inicio")
            str2.set("Fin")
            str3.set("")
            str4.set("")
            ent1.configure(state=NORMAL)
            ent2.configure(state=NORMAL)
            ent3.configure(state=DISABLED)
            ent44.configure(state=DISABLED)
            fun.set("Rampa 1")
            y=np.piecewise(t, [t>10/3], [lambda t: t-10/3])-np.piecewise(t, [t>20/3], [lambda t: t-20/3])
        if nm == 6:
            str1.set("Inicio")
            str2.set("Fin")
            str3.set("")
            str4.set("")
            ent1.configure(state=NORMAL)
            ent2.configure(state=NORMAL)
            ent3.configure(state=DISABLED)
            ent44.configure(state=DISABLED)
            fun.set("Rampa 2")
            y=10/3-np.piecewise(t, [t>10/3], [lambda t: t-10/3])+np.piecewise(t, [t>20/3], [lambda t: t-20/3])
        if nm == 7:
            str1.set("Inicio")
            str2.set("Fin")
            str3.set("")
            str4.set("")
            ent1.configure(state=NORMAL)
            ent2.configure(state=NORMAL)
            ent3.configure(state=DISABLED)
            ent44.configure(state=DISABLED)
            fun.set("Rampa 3")
            y=np.piecewise(t, [t<10/3], [lambda t: t,10/3])-np.piecewise(t, [t>20/3], [lambda t: t-20/3])
        if nm == 8:
            str1.set("Inicio")
            str2.set("Fin")
            str3.set("")
            str4.set("")
            ent1.configure(state=NORMAL)
            ent2.configure(state=NORMAL)
            ent3.configure(state=DISABLED)
            ent44.configure(state=DISABLED)
            fun.set("Colmillo")
            t2 = np.arange(0,10/3,0.01)
            a = max(t)
            expon = np.exp(t2)-1
            y1 = np.piecewise(t, [t<a/3], [lambda t: np.exp(t*10/a)-max(expon)-1])
            y2 = np.piecewise(t, [t>a/3], [lambda t: -np.exp((t-a/3)*10/a)+1])
            y3 = -np.piecewise(t, [t>(2*a)/3], [lambda t: -np.exp((t-a/3)*10/a)+1])
            y4 = np.piecewise(t, [t>(2*a)/3], [lambda t: np.exp((t-(2*a)/3)*10/a)-max(expon)-1])
            y = y1 + y2 + y3 + y4
        
        rdb1.configure(state=NORMAL)
        rdb2.configure(state=NORMAL)
        plt.figure(1)
        plt.clf()
        plt.title('x(t)/x[n]')
        plt.plot(t, y,'orange')
        plt.gcf().canvas.draw()
        
        
    def parametrosh(numh):
        global nmh
        nmh = int(numh)
        if nmh == 1:
            str10.set("Amplitud")
            str20.set("Periodo")
            str30.set("")
            str40.set("")
            ent10.configure(state=NORMAL)
            ent20.configure(state=NORMAL)
            ent30.configure(state=DISABLED)
            ent40.configure(state=DISABLED)
            funh.set("Sinusoidal")
            y = np.sin((2*np.pi/10)*t)
        if nmh == 2:
            str10.set("Amplitud")
            str20.set("Periodo")
            str30.set("")
            str40.set("")
            ent10.configure(state=NORMAL)
            ent20.configure(state=NORMAL)
            ent30.configure(state=DISABLED)
            ent40.configure(state=DISABLED)
            funh.set("Triangular")
            y = sp.sawtooth(t*2*np.pi/10,0.5)
        if nmh == 3:
            str10.set("Amplitud")
            str20.set("Periodo")
            str30.set("")
            str40.set("")
            ent10.configure(state=NORMAL)
            ent20.configure(state=NORMAL)
            ent30.configure(state=DISABLED)
            ent40.configure(state=DISABLED)
            funh.set("Cuadrada")
            y = sp.square(t*2*np.pi/10,0.5)
        if nmh == 4:
            str10.set("Amplitud")
            str20.set("Exponente")
            str30.set("Inicio")
            str40.set("Fin")
            ent10.configure(state=NORMAL)
            ent20.configure(state=NORMAL)
            ent30.configure(state=NORMAL)
            ent40.configure(state=NORMAL)
            funh.set("Exponencial")
            y = np.exp(-t)
        if nmh == 5:
            str10.set("Inicio")
            str20.set("Fin")
            str30.set("")
            str40.set("")
            ent10.configure(state=NORMAL)
            ent20.configure(state=NORMAL)
            ent30.configure(state=DISABLED)
            ent40.configure(state=DISABLED)
            funh.set("Rampa 1")
            y=np.piecewise(t, [t>10/3], [lambda t: t-10/3])-np.piecewise(t, [t>20/3], [lambda t: t-20/3])
        if nmh == 6:
            str10.set("Inicio")
            str20.set("Fin")
            str30.set("")
            str40.set("")
            ent10.configure(state=NORMAL)
            ent20.configure(state=NORMAL)
            ent30.configure(state=DISABLED)
            ent40.configure(state=DISABLED)
            funh.set("Rampa 2")
            y=10/3-np.piecewise(t, [t>10/3], [lambda t: t-10/3])+np.piecewise(t, [t>20/3], [lambda t: t-20/3])
        if nmh == 7:
            str10.set("Inicio")
            str20.set("Fin")
            str30.set("")
            str40.set("")
            ent10.configure(state=NORMAL)
            ent20.configure(state=NORMAL)
            ent30.configure(state=DISABLED)
            ent40.configure(state=DISABLED)
            funh.set("Rampa 3")
            y=np.piecewise(t, [t<10/3], [lambda t: t,10/3])-np.piecewise(t, [t>20/3], [lambda t: t-20/3])
        if nmh == 8:
            str10.set("Inicio")
            str20.set("Fin")
            str30.set("")
            str40.set("")
            ent10.configure(state=NORMAL)
            ent20.configure(state=NORMAL)
            ent30.configure(state=DISABLED)
            ent40.configure(state=DISABLED)
            funh.set("Colmillo")
            t2 = np.arange(0,10/3,0.01)
            a = max(t)
            expon = np.exp(t2)-1
            y1 = np.piecewise(t, [t<a/3], [lambda t: np.exp(t*10/a)-max(expon)-1])
            y2 = np.piecewise(t, [t>a/3], [lambda t: -np.exp((t-a/3)*10/a)+1])
            y3 = -np.piecewise(t, [t>(2*a)/3], [lambda t: -np.exp((t-a/3)*10/a)+1])
            y4 = np.piecewise(t, [t>(2*a)/3], [lambda t: np.exp((t-(2*a)/3)*10/a)-max(expon)-1])
            y = y1 + y2 + y3 + y4
        
        rdb1.configure(state=NORMAL)
        rdb2.configure(state=NORMAL)
        plt.figure(2)
        plt.clf()
        plt.title('h(t)/h[n]')
        plt.plot(t, y,'green')
        plt.gcf().canvas.draw()
        
    r = IntVar()
    q = IntVar()
    j = IntVar()
    ergesr = IntVar()
    
    Radiobutton(fr7, text="Sinusoidal", variable=r, value=1, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(1)).grid(sticky="W",row=1,column=0)
    Radiobutton(fr7, text="Triangular", variable=r, value=2, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(2)).grid(sticky="W",row=2,column=0)
    Radiobutton(fr7, text="Rectangular", variable=r, value=3, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(3)).grid(sticky="W",row=3,column=0)
    Radiobutton(fr7, text="Exponencial", variable=r, value=4, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(4)).grid(sticky="W",row=4,column=0)
    Radiobutton(fr7, text="Rampa 1", variable=r, value=5, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(5)).grid(sticky="W",row=5,column=0)
    Radiobutton(fr7, text="Rampa 2", variable=r, value=6, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(6)).grid(sticky="W",row=6,column=0)
    Radiobutton(fr7, text="Rampa 3", variable=r, value=7, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(7)).grid(sticky="W",row=7,column=0)
    Radiobutton(fr7, text="Colmillo", variable=r, value=8, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(8)).grid(sticky="W",row=8,column=0)
    
    Radiobutton(fr70, text="Sinusoidal", variable=ergesr, value=1, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametrosh(1)).grid(sticky="W",row=1,column=0)
    Radiobutton(fr70, text="Triangular", variable=ergesr, value=2, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametrosh(2)).grid(sticky="W",row=2,column=0)
    Radiobutton(fr70, text="Rectangular", variable=ergesr, value=3, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametrosh(3)).grid(sticky="W",row=3,column=0)
    Radiobutton(fr70, text="Exponencial", variable=ergesr, value=4, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametrosh(4)).grid(sticky="W",row=4,column=0)
    Radiobutton(fr70, text="Rampa 1", variable=ergesr, value=5, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametrosh(5)).grid(sticky="W",row=5,column=0)
    Radiobutton(fr70, text="Rampa 2", variable=ergesr, value=6, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametrosh(6)).grid(sticky="W",row=6,column=0)
    Radiobutton(fr70, text="Rampa 3", variable=ergesr, value=7, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametrosh(7)).grid(sticky="W",row=7,column=0)
    Radiobutton(fr70, text="Colmillo", variable=ergesr, value=8, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametrosh(8)).grid(sticky="W",row=8,column=0)
    
    fr3=LabelFrame(fr2, text="Digite parámetros:", bg="grey12", fg="goldenrod1", padx=10, pady=20)
    fr3.grid(row=9,column=0,padx=5)
    fr4=Frame(fr3,bg="grey12")
    fr4.grid(row=1,column=0, pady=5)
    fr5=Frame(fr3,bg="grey12")
    fr5.grid(row=2,column=0)
    fr6=Frame(fr3,bg="grey12")
    fr6.grid(row=3,column=0, pady=5)
    fr66=Frame(fr3,bg="grey12")
    fr66.grid(row=4,column=0, pady=5)
    par1=Label(fr4,textvariable=str1, width=12, anchor="e",bg="grey12",fg="goldenrod1").grid(row=0,column=0)
    par2=Label(fr5,textvariable=str2, width=12, anchor="e",bg="grey12",fg="goldenrod1").grid(row=0,column=0)
    par3=Label(fr6,textvariable=str3, width=12, anchor="e",bg="grey12",fg="goldenrod1").grid(row=0,column=0)
    par4=Label(fr66,textvariable=str4, width=12, anchor="e",bg="grey12",fg="goldenrod1").grid(row=0,column=0)
    ent1=Entry(fr4, text="", bg="grey28", fg="goldenrod1", width=4, bd=5, state=DISABLED)
    ent1.grid(sticky="E",row=0,column=1)
    ent2=Entry(fr5, text="", bg="grey28", fg="goldenrod1", width=4, bd=5, state=DISABLED)
    ent2.grid(sticky="E",row=0,column=1)
    ent3=Entry(fr6, text="", bg="grey28", fg="goldenrod1", width=4, bd=5, state=DISABLED)
    ent3.grid(sticky="E",row=0,column=1)
    ent44=Entry(fr66, text="", bg="grey28", fg="goldenrod1", width=4, bd=5, state=DISABLED)
    ent44.grid(sticky="E",row=0,column=1)
    
    fr30=LabelFrame(fr20, text="Digite parámetros:", bg="grey12", fg="goldenrod1", padx=10, pady=20)
    fr30.grid(row=9,column=0,padx=5)
    fr40=Frame(fr30,bg="grey12")
    fr40.grid(row=1,column=0, pady=5)
    fr50=Frame(fr30,bg="grey12")
    fr50.grid(row=2,column=0)
    fr60=Frame(fr30,bg="grey12")
    fr60.grid(row=3,column=0, pady=5)
    fr660=Frame(fr30,bg="grey12")
    fr660.grid(row=4,column=0, pady=5)
    par10=Label(fr40,textvariable=str10, width=12, anchor="e",bg="grey12",fg="goldenrod1").grid(row=0,column=0)
    par20=Label(fr50,textvariable=str20, width=12, anchor="e",bg="grey12",fg="goldenrod1").grid(row=0,column=0)
    par30=Label(fr60,textvariable=str30, width=12, anchor="e",bg="grey12",fg="goldenrod1").grid(row=0,column=0)
    par40=Label(fr660,textvariable=str40, width=12, anchor="e",bg="grey12",fg="goldenrod1").grid(row=0,column=0)
    ent10=Entry(fr40, text="", bg="grey28", fg="goldenrod1", width=4, bd=5, state=DISABLED)
    ent10.grid(sticky="E",row=0,column=1)
    ent20=Entry(fr50, text="", bg="grey28", fg="goldenrod1", width=4, bd=5, state=DISABLED)
    ent20.grid(sticky="E",row=0,column=1)
    ent30=Entry(fr60, text="", bg="grey28", fg="goldenrod1", width=4, bd=5, state=DISABLED)
    ent30.grid(sticky="E",row=0,column=1)
    ent40=Entry(fr660, text="", bg="grey28", fg="goldenrod1", width=4, bd=5, state=DISABLED)
    ent40.grid(sticky="E",row=0,column=1)
    
    
    fr77=LabelFrame(fr2, text="", bg="grey12", fg="goldenrod1", padx=7, pady=15)
    fr77.grid(row=8,column=0,pady=5)
    fr10=LabelFrame(fr8, text="Dominio:", bg="grey12", fg="goldenrod1", padx=54, pady=20)
    fr10.grid(row=1,column=0)
    asd=Label(fr77, textvariable=fun, width=14,bg="grey12",fg="green1",font=20, pady=10).grid(row=1,column=0)
    fku=Label(fr77, text="Función:",bg="grey12", fg="goldenrod1").grid(row=0,column=0)
    
    fr770=LabelFrame(fr20, text="", bg="grey12", fg="goldenrod1", padx=7, pady=15)
    fr770.grid(row=8,column=0,pady=5)
    asd=Label(fr770, textvariable=funh, width=14,bg="grey12",fg="green1",font=20, pady=10).grid(row=1,column=0)
    fku=Label(fr770, text="Función:",bg="grey12", fg="goldenrod1").grid(row=0,column=0)
    
    def accion(des):
        global p,tx,yx,th,yh,thi,tpro,tconv,yhf,val1,val2,val3,val4,val10,val20,val30,val40,rango,rangoh,tconvol,adver
        p=int(des)
        btn2.configure(state = NORMAL)
        if p == 1:
            intmuestr = 0.01
            if nm == 1:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(0,val2+0.01,0.01)
                yx = val1*np.sin((2*np.pi/val2)*tx)
                rango = val2
            if nm == 2:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(0,val2+0.01,0.01)
                yx = val1*sp.sawtooth(tx*2*np.pi/val2,0.5)
                rango = val2
            if nm == 3:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(0,val2+0.01,0.01)
                yx = val1*sp.square(tx*2*np.pi/val2,0.5)
                rango = val2
            if nm == 4:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=float(ent3.get())
                val4=float(ent44.get())
                tx = np.arange(val3,val4+0.01,0.01)
                yx = val1*np.exp(val2*tx)
                rango = val4-val3
            if nm == 5:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(val1,val2+0.01,0.01)
                yx = np.piecewise(tx, [tx>((val2-val1)/3)+val1], [lambda tx: tx-((val2-val1)/3)-val1])-np.piecewise(tx, [tx>2*((val2-val1)/3)+val1], [lambda tx: tx-2*((val2-val1)/3)-val1])
                rango = val2-val1
            if nm == 6:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(val1,val2+0.01,0.01)
                yx = ((val2-val1)/3)-np.piecewise(tx, [tx>((val2-val1)/3)+val1], [lambda tx: tx-((val2-val1)/3)-val1])+np.piecewise(tx, [tx>2*((val2-val1)/3)+val1], [lambda tx: tx-2*((val2-val1)/3)-val1])
                rango = val2-val1
            if nm == 7:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(val1,val2+0.01,0.01)
                yx = np.piecewise(tx, [tx<((val2-val1)/3)+val1], [lambda tx: tx-val1,(val2-val1)/3])-np.piecewise(tx, [tx>2*((val2-val1)/3)+val1], [lambda tx: tx-2*((val2-val1)/3)-val1])
                rango = val2-val1
            if nm == 8:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(val1,val2+0.01,0.01)
                t2 = np.arange(0,10/3,0.01)
                rango = val2-val1
                expon = np.exp(t2)-1
                y1 = np.piecewise(tx, [tx<val1+rango/3], [lambda tx: np.exp((tx-val1)*10/rango)-max(expon)-1])
                y2 = np.piecewise(tx, [tx>val1+rango/3], [lambda tx: -np.exp((tx-val1-rango/3)*10/rango)+1])
                y3 = -np.piecewise(tx, [tx>val1+(2*rango)/3], [lambda tx: -np.exp((tx-val1-rango/3)*10/rango)+1])
                y4 = np.piecewise(tx, [tx>val1+(2*rango)/3], [lambda tx: np.exp((tx-val1-(2*rango)/3)*10/rango)-max(expon)-1])
                yx = y1 + y2 + y3 + y4
            if nmh == 1:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(0,val20+0.01,0.01)
                yh = val10*np.sin((2*np.pi/val20)*th)
                rangoh = val20
            if nmh == 2:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(0,val20+0.01,0.01)
                yh = val10*sp.sawtooth(th*2*np.pi/val20,0.5)
                rangoh = val20
            if nmh == 3:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(0,val20+0.01,0.01)
                yh = val10*sp.square(th*2*np.pi/val20,0.5)
                
                rangoh = val20
            if nmh == 4:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=float(ent30.get())
                val40=float(ent40.get())
                th = np.arange(val30,val40+0.01,0.01)
                yh = val10*np.exp(val20*th)
                rangoh = val40-val30
            if nmh == 5:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(val10,val20+0.01,0.01)
                yh = np.piecewise(th, [th>((val20-val10)/3)+val10], [lambda th: th-((val20-val10)/3)-val10])-np.piecewise(th, [th>2*((val20-val10)/3)+val10], [lambda th: th-2*((val20-val10)/3)-val10])
                rangoh = val20-val10
            if nmh == 6:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(val10,val20+0.01,0.01)
                yh = ((val20-val10)/3)-np.piecewise(th, [th>((val20-val10)/3)+val10], [lambda th: th-((val20-val10)/3)-val10])+np.piecewise(th, [th>2*((val20-val10)/3)+val10], [lambda th: th-2*((val20-val10)/3)-val10])
                rangoh = val20-val10
            if nmh == 7:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(val10,val20+0.01,0.01)
                yh = np.piecewise(th, [th<((val20-val10)/3)+val10], [lambda th: th-val10,(val20-val10)/3])-np.piecewise(th, [th>2*((val20-val10)/3)+val10], [lambda th: th-2*((val20-val10)/3)-val10])
                rangoh = val20-val10
            if nmh == 8:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(val10,val20+0.01,0.01)
                t2 = np.arange(0,10/3,0.01)
                rangoh = val20-val10
                expon = np.exp(t2)-1
                y1 = np.piecewise(th, [th<val10+rangoh/3], [lambda th: np.exp((th-val10)*10/rangoh)-max(expon)-1])
                y2 = np.piecewise(th, [th>val10+rangoh/3], [lambda th: -np.exp((th-val10-rangoh/3)*10/rangoh)+1])
                y3 =-np.piecewise(th, [th>val10+(2*rangoh)/3], [lambda th: -np.exp((th-val10-rangoh/3)*10/rangoh)+1])
                y4 = np.piecewise(th, [th>val10+(2*rangoh)/3], [lambda th: np.exp((th-val10-(2*rangoh)/3)*10/rangoh)-max(expon)-1])
                yh = y1 + y2 + y3 + y4
            if (rango <= 0.1) or (rangoh <=0.1):
                messagebox.showerror(title="Error", message="No se puede realizar la gráfica con tan pocas muestras.\nPor favor digite un rango de muestras mayor o igual a 0.1 para garantizar una correcta visibilidad de cada función en el dominio continuo.", master = menu)
            else:
                plt.figure(1)
                plt.clf()
                plt.title('x(t)')
                plt.plot(tx, yx,'green')
                plt.gcf().canvas.draw()
                plt.figure(2)
                plt.clf()
                plt.title('h(t)')
                plt.plot(th, yh,'red')
                plt.gcf().canvas.draw()
            tpro = np.arange(np.amin(tx)-rangoh,np.amax(tx)+0.01+rangoh,intmuestr)
            tconv = np.arange(np.amin(tx)+np.amin(th),np.amax(tx)+np.amax(th)+0.01,intmuestr)
            tconvol = np.arange(np.amin(tx)+np.amin(th),np.amax(tx)+np.amax(th)+0.01,intmuestr)
        if p == 2:
            intmuestr = 1
            if nm == 1:
                val1=float(ent1.get())
                val2=int(ent2.get())
                val3=0
                val4=0
                tx = np.arange(0,val2+1,1)
                yx = val1*np.sin((2*np.pi/val2)*tx)
                rango = val2
            if nm == 2:
                val1=float(ent1.get())
                val2=int(ent2.get())
                val3=0
                val4=0
                tx = np.arange(0,val2+1,1)
                yx = val1*sp.sawtooth(tx*2*np.pi/val2,0.5)
                rango = val2
            if nm == 3:
                val1=float(ent1.get())
                val2=int(ent2.get())
                val3=0
                val4=0
                tx = np.arange(0,val2+1,1)
                yx = val1*sp.square(tx*2*np.pi/val2,0.5)
                rango = val2
            if nm == 4:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=int(ent3.get())
                val4=int(ent44.get())
                tx = np.arange(val3,val4+1,1)
                yx = val1*np.exp(val2*tx)
                rango = val4-val3
            if nm == 5:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(val1,val2+1,1)
                yx = np.piecewise(tx, [tx>((val2-val1)/3)+val1], [lambda tx: tx-((val2-val1)/3)-val1])-np.piecewise(tx, [tx>2*((val2-val1)/3)+val1], [lambda tx: tx-2*((val2-val1)/3)-val1])
                rango = int(val2-val1)
            if nm == 6:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(val1,val2+1,1)
                yx = ((val2-val1)/3)-np.piecewise(tx, [tx>((val2-val1)/3)+val1], [lambda tx: tx-((val2-val1)/3)-val1])+np.piecewise(tx, [tx>2*((val2-val1)/3)+val1], [lambda tx: tx-2*((val2-val1)/3)-val1])
                rango = int(val2-val1)
            if nm == 7:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(val1,val2+1,1)
                yx = np.piecewise(tx, [tx<((val2-val1)/3)+val1], [lambda tx: tx-val1,(val2-val1)/3])-np.piecewise(tx, [tx>2*((val2-val1)/3)+val1], [lambda tx: tx-2*((val2-val1)/3)-val1])
                rango = int(val2-val1)
            if nm == 8:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(val1,val2+1,1)
                t2 = np.arange(0,10/3,0.01)
                rango = val2-val1
                expon = np.exp(t2)-1
                y1 = np.piecewise(tx, [tx<val1+rango/3], [lambda tx: np.exp((tx-val1)*10/rango)-max(expon)-1])
                y2 = np.piecewise(tx, [tx>val1+rango/3], [lambda tx: -np.exp((tx-val1-rango/3)*10/rango)+1])
                y3 = -np.piecewise(tx, [tx>val1+(2*rango)/3], [lambda tx: -np.exp((tx-val1-rango/3)*10/rango)+1])
                y4 = np.piecewise(tx, [tx>val1+(2*rango)/3], [lambda tx: np.exp((tx-val1-(2*rango)/3)*10/rango)-max(expon)-1])
                yx = y1 + y2 + y3 + y4
            if nmh == 1:
                val10=float(ent10.get())
                val20=int(ent20.get())
                val30=0
                val40=0
                th = np.arange(0,val20+1,1)
                yh = val10*np.sin((2*np.pi/val20)*th)
                rangoh = val20
            if nmh == 2:
                val10=float(ent10.get())
                val20=int(ent20.get())
                val30=0
                val40=0
                th = np.arange(0,val20+1,1)
                yh = val10*sp.sawtooth(th*2*np.pi/val20,0.5)
                rangoh = val20
            if nmh == 3:
                val10=float(ent10.get())
                val20=int(ent20.get())
                val30=0
                val40=0
                th = np.arange(0,val20+1,1)
                yh = val10*sp.square(th*2*np.pi/val20,0.5)
                rangoh = val20
            if nmh == 4:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=int(ent30.get())
                val40=int(ent40.get())
                th = np.arange(val30,val40+1,1)
                yh = val10*np.exp(val20*th)
                rangoh = val40-val30
            if nmh == 5:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(val10,val20+1,1)
                yh = np.piecewise(th, [th>((val20-val10)/3)+val10], [lambda th: th-((val20-val10)/3)-val10])-np.piecewise(th, [th>2*((val20-val10)/3)+val10], [lambda th: th-2*((val20-val10)/3)-val10])
                rangoh = int(val20-val10)
            if nmh == 6:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(val10,val20+1,1)
                yh = ((val20-val10)/3)-np.piecewise(th, [th>((val20-val10)/3)+val10], [lambda th: th-((val20-val10)/3)-val10])+np.piecewise(th, [th>2*((val20-val10)/3)+val10], [lambda th: th-2*((val20-val10)/3)-val10])
                rangoh = int(val20-val10)
            if nmh == 7:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(val10,val20+1,1)
                yh = np.piecewise(th, [th<((val20-val10)/3)+val10], [lambda th: th-val10,(val20-val10)/3])-np.piecewise(th, [th>2*((val20-val10)/3)+val10], [lambda th: th-2*((val20-val10)/3)-val10])
                rangoh = int(val20-val10)
            if nmh == 8:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(val10,val20+1,1)
                t2 = np.arange(0,10/3,0.01)
                rangoh = val20-val10
                expon = np.exp(t2)-1
                y1 = np.piecewise(th, [th<val10+rangoh/3], [lambda th: np.exp((th-val10)*10/rangoh)-max(expon)-1])
                y2 = np.piecewise(th, [th>val10+rangoh/3], [lambda th: -np.exp((th-val10-rangoh/3)*10/rangoh)+1])
                y3 =-np.piecewise(th, [th>val10+(2*rangoh)/3], [lambda th: -np.exp((th-val10-rangoh/3)*10/rangoh)+1])
                y4 = np.piecewise(th, [th>val10+(2*rangoh)/3], [lambda th: np.exp((th-val10-(2*rangoh)/3)*10/rangoh)-max(expon)-1])
                yh = y1 + y2 + y3 + y4
               
            if (rango <= 7) or (rangoh <=7):
                messagebox.showerror(title="Error", message="No se puede realizar la gráfica con tan pocas muestras.\nPor favor digite un rango de muestras mayor o igual a 8 para garantizar una correcta visibilidad de cada función en el dominio discreto.", master = menu)
            else:
                plt.figure(1)
                plt.clf()
                plt.title('x[n]')
                plt.stem(tx, yx,'green')
                plt.gcf().canvas.draw()
                plt.figure(2)
                plt.clf()
                plt.title('h[n]')
                plt.stem(th, yh,'red')
                plt.gcf().canvas.draw()
                
            tpro = np.arange(np.amin(tx)-rangoh,np.amax(tx)+1+rangoh,intmuestr)
            tconv = np.arange(np.amin(tx)+np.amin(th),np.amax(tx)+np.amax(th)+1,intmuestr)
            
        yhf = np.flip(yh)
        

    
    rdb1=Radiobutton(fr10, text="Continuo", variable=q, value=1, bg="grey12", fg="goldenrod1", selectcolor="grey38", state=DISABLED, indicatoron=0, width=13, command=lambda: accion(1))
    rdb1.grid(sticky="W",row=1,column=0)
    rdb2=Radiobutton(fr10, text="Discreto", variable=q, value=2, bg="grey12", fg="goldenrod1", selectcolor="grey38", state=DISABLED, indicatoron=0, width=13, command=lambda: accion(2))
    rdb2.grid(sticky="W",row=1,column=1)
    fr11=LabelFrame(fr8, text="", bg="grey12", fg="goldenrod1", padx=10, pady=10)
    fr11.grid(row=2,column=0,pady=8)
    
    def mostrarconv():
        global tconv,tx,yx,th,yh,thi,tpro,tconv,yhf,val1,val2,val3,val4,val10,val20,val30,val40,rango,rangoh,tconvol,yconv,adver
        if adver == 1:
            messagebox.showwarning(title="Advertencia", message="Cuando se ejecuta convolución varias veces es probable que la interfaz se ponga lenta. Si se empieza a congelar la interfaz mientras ejecuta convolución, ciérrela y vuelvala a abrir.", master = menu)
            adver = 0
        if p == 1:
            intmuestr = 0.01
            if nm == 1:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(0,val2+0.01,0.01)
                yx = val1*np.sin((2*np.pi/val2)*tx)
                rango = val2
            if nm == 2:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(0,val2+0.01,0.01)
                yx = val1*sp.sawtooth(tx*2*np.pi/val2,0.5)
                rango = val2
            if nm == 3:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(0,val2+0.01,0.01)
                yx = val1*sp.square(tx*2*np.pi/val2,0.5)
                rango = val2
            if nm == 4:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=float(ent3.get())
                val4=float(ent44.get())
                tx = np.arange(val3,val4+0.01,0.01)
                yx = val1*np.exp(val2*tx)
                rango = val4-val3
            if nm == 5:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(val1,val2+0.01,0.01)
                yx = np.piecewise(tx, [tx>((val2-val1)/3)+val1], [lambda tx: tx-((val2-val1)/3)-val1])-np.piecewise(tx, [tx>2*((val2-val1)/3)+val1], [lambda tx: tx-2*((val2-val1)/3)-val1])
                rango = val2-val1
            if nm == 6:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(val1,val2+0.01,0.01)
                yx = ((val2-val1)/3)-np.piecewise(tx, [tx>((val2-val1)/3)+val1], [lambda tx: tx-((val2-val1)/3)-val1])+np.piecewise(tx, [tx>2*((val2-val1)/3)+val1], [lambda tx: tx-2*((val2-val1)/3)-val1])
                rango = val2-val1
            if nm == 7:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(val1,val2+0.01,0.01)
                yx = np.piecewise(tx, [tx<((val2-val1)/3)+val1], [lambda tx: tx-val1,(val2-val1)/3])-np.piecewise(tx, [tx>2*((val2-val1)/3)+val1], [lambda tx: tx-2*((val2-val1)/3)-val1])
                rango = val2-val1
            if nm == 8:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(val1,val2+0.01,0.01)
                t2 = np.arange(0,10/3,0.01)
                rango = val2-val1
                expon = np.exp(t2)-1
                y1 = np.piecewise(tx, [tx<val1+rango/3], [lambda tx: np.exp((tx-val1)*10/rango)-max(expon)-1])
                y2 = np.piecewise(tx, [tx>val1+rango/3], [lambda tx: -np.exp((tx-val1-rango/3)*10/rango)+1])
                y3 = -np.piecewise(tx, [tx>val1+(2*rango)/3], [lambda tx: -np.exp((tx-val1-rango/3)*10/rango)+1])
                y4 = np.piecewise(tx, [tx>val1+(2*rango)/3], [lambda tx: np.exp((tx-val1-(2*rango)/3)*10/rango)-max(expon)-1])
                yx = y1 + y2 + y3 + y4
            if nmh == 1:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(0,val20+0.01,0.01)
                yh = val10*np.sin((2*np.pi/val20)*th)
                rangoh = val20
            if nmh == 2:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(0,val20+0.01,0.01)
                yh = val10*sp.sawtooth(th*2*np.pi/val20,0.5)
                rangoh = val20
            if nmh == 3:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(0,val20+0.01,0.01)
                yh = val10*sp.square(th*2*np.pi/val20,0.5)
                
                rangoh = val20
            if nmh == 4:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=float(ent30.get())
                val40=float(ent40.get())
                th = np.arange(val30,val40+0.01,0.01)
                yh = val10*np.exp(val20*th)
                rangoh = val40-val30
            if nmh == 5:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(val10,val20+0.01,0.01)
                yh = np.piecewise(th, [th>((val20-val10)/3)+val10], [lambda th: th-((val20-val10)/3)-val10])-np.piecewise(th, [th>2*((val20-val10)/3)+val10], [lambda th: th-2*((val20-val10)/3)-val10])
                rangoh = val20-val10
            if nmh == 6:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(val10,val20+0.01,0.01)
                yh = ((val20-val10)/3)-np.piecewise(th, [th>((val20-val10)/3)+val10], [lambda th: th-((val20-val10)/3)-val10])+np.piecewise(th, [th>2*((val20-val10)/3)+val10], [lambda th: th-2*((val20-val10)/3)-val10])
                rangoh = val20-val10
            if nmh == 7:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(val10,val20+0.01,0.01)
                yh = np.piecewise(th, [th<((val20-val10)/3)+val10], [lambda th: th-val10,(val20-val10)/3])-np.piecewise(th, [th>2*((val20-val10)/3)+val10], [lambda th: th-2*((val20-val10)/3)-val10])
                rangoh = val20-val10
            if nmh == 8:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(val10,val20+0.01,0.01)
                t2 = np.arange(0,10/3,0.01)
                rangoh = val20-val10
                expon = np.exp(t2)-1
                y1 = np.piecewise(th, [th<val10+rangoh/3], [lambda th: np.exp((th-val10)*10/rangoh)-max(expon)-1])
                y2 = np.piecewise(th, [th>val10+rangoh/3], [lambda th: -np.exp((th-val10-rangoh/3)*10/rangoh)+1])
                y3 =-np.piecewise(th, [th>val10+(2*rangoh)/3], [lambda th: -np.exp((th-val10-rangoh/3)*10/rangoh)+1])
                y4 = np.piecewise(th, [th>val10+(2*rangoh)/3], [lambda th: np.exp((th-val10-(2*rangoh)/3)*10/rangoh)-max(expon)-1])
                yh = y1 + y2 + y3 + y4
            
            tpro = np.arange(np.amin(tx)-rangoh,np.amax(tx)+0.01+rangoh,intmuestr)
            tconv = np.arange(np.amin(tx)+np.amin(th),np.amax(tx)+np.amax(th)+0.01,intmuestr)
            yhf = np.flip(yh)
            
            if (rango <= 0.1) or (rangoh <=0.1):
                messagebox.showerror(title="Error", message="No se puede realizar la gráfica con tan pocas muestras.\nPor favor digite un rango de muestras mayor o igual a 0.1 para garantizar una correcta visibilidad de cada función en el dominio continuo.", master = menu)
            else:
                j = 0
                #yxi = np.zeros_like(tconv,float)
                yxi = np.zeros_like(tpro,float)
                yconv = np.zeros_like(tconv,float)
    
                while j <= 100*rango:
                    np.put(yxi,j+int(100*rangoh),yx[j])
                    #yxi[j+np.amin(th)+rangoh]=yx[j]
                    j=j+1
                
                j = 0
                yhi = np.zeros_like(tpro,float)
                while j <= int(100*rangoh):
                    np.put(yhi,j,yhf[j])
                    #yhi[j]=yhf[j]
                    j=j+1
                    
                plt.figure(3)
                plt.clf()
                plt.title('Procedimiento')
                plt.plot(tpro, yxi,'green')
                plt.plot(tpro, yhi, 'red')
                plt.gcf().canvas.draw()
                
                plt.figure(4)
                plt.clf()
                plt.title('Convolución')
                plt.plot(tconv, yconv,'blue')
                plt.gcf().canvas.draw()
                
                i = 0
                
                time.sleep(1)
                
                while i <= int(100*(rango + rangoh)):
                    xporh = np.multiply(yxi,yhi)
                    yconv[i] = np.sum(xporh)
                    plt.figure(4)
                    plt.clf()
                    plt.title('Convolución')
                    plt.plot(tconv, yconv,'blue')
                    plt.gcf().canvas.draw()
                    plt.figure(3)
                    plt.clf()
                    plt.title('Procedimiento')
                    plt.plot(tpro, yxi, 'green')
                    plt.plot(tpro, yhi, 'red')
                    plt.gcf().canvas.draw()
                    yhi = np.roll(yhi,int(rango+rangoh))   
                    time.sleep(.1/5)
                    i = i + int((rango+rangoh))
                yconvol=np.zeros_like(tconv)
                yconvolve=np.convolve(yx,yh,'full')
                for i in range(0, len(tconv)-1):
                    yconvol[i]=yconvolve[i]
                    
                plt.figure(4)
                plt.clf()
                plt.title('Convolución')
                plt.plot(tconv, yconvol,'blue')
                plt.gcf().canvas.draw()
            
        if p == 2:
            intmuestr = 1
            if nm == 1:
                val1=float(ent1.get())
                val2=int(ent2.get())
                val3=0
                val4=0
                tx = np.arange(0,val2+1,1)
                yx = val1*np.sin((2*np.pi/val2)*tx)
                rango = val2
            if nm == 2:
                val1=float(ent1.get())
                val2=int(ent2.get())
                val3=0
                val4=0
                tx = np.arange(0,val2+1,1)
                yx = val1*sp.sawtooth(tx*2*np.pi/val2,0.5)
                rango = val2
            if nm == 3:
                val1=float(ent1.get())
                val2=int(ent2.get())
                val3=0
                val4=0
                tx = np.arange(0,val2+1,1)
                yx = val1*sp.square(tx*2*np.pi/val2,0.5)
                rango = val2
            if nm == 4:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=int(ent3.get())
                val4=int(ent44.get())
                tx = np.arange(val3,val4+1,1)
                yx = val1*np.exp(val2*tx)
                rango = val4-val3
            if nm == 5:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(val1,val2+1,1)
                yx = np.piecewise(tx, [tx>((val2-val1)/3)+val1], [lambda tx: tx-((val2-val1)/3)-val1])-np.piecewise(tx, [tx>2*((val2-val1)/3)+val1], [lambda tx: tx-2*((val2-val1)/3)-val1])
                rango = int(val2-val1)
            if nm == 6:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(val1,val2+1,1)
                yx = ((val2-val1)/3)-np.piecewise(tx, [tx>((val2-val1)/3)+val1], [lambda tx: tx-((val2-val1)/3)-val1])+np.piecewise(tx, [tx>2*((val2-val1)/3)+val1], [lambda tx: tx-2*((val2-val1)/3)-val1])
                rango = int(val2-val1)
            if nm == 7:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(val1,val2+1,1)
                yx = np.piecewise(tx, [tx<((val2-val1)/3)+val1], [lambda tx: tx-val1,(val2-val1)/3])-np.piecewise(tx, [tx>2*((val2-val1)/3)+val1], [lambda tx: tx-2*((val2-val1)/3)-val1])
                rango = int(val2-val1)
            if nm == 8:
                val1=float(ent1.get())
                val2=float(ent2.get())
                val3=0
                val4=0
                tx = np.arange(val1,val2+1,1)
                t2 = np.arange(0,10/3,0.01)
                rango = val2-val1
                expon = np.exp(t2)-1
                y1 = np.piecewise(tx, [tx<val1+rango/3], [lambda tx: np.exp((tx-val1)*10/rango)-max(expon)-1])
                y2 = np.piecewise(tx, [tx>val1+rango/3], [lambda tx: -np.exp((tx-val1-rango/3)*10/rango)+1])
                y3 = -np.piecewise(tx, [tx>val1+(2*rango)/3], [lambda tx: -np.exp((tx-val1-rango/3)*10/rango)+1])
                y4 = np.piecewise(tx, [tx>val1+(2*rango)/3], [lambda tx: np.exp((tx-val1-(2*rango)/3)*10/rango)-max(expon)-1])
                yx = y1 + y2 + y3 + y4
            if nmh == 1:
                val10=float(ent10.get())
                val20=int(ent20.get())
                val30=0
                val40=0
                th = np.arange(0,val20+1,1)
                yh = val10*np.sin((2*np.pi/val20)*th)
                rangoh = val20
            if nmh == 2:
                val10=float(ent10.get())
                val20=int(ent20.get())
                val30=0
                val40=0
                th = np.arange(0,val20+1,1)
                yh = val10*sp.sawtooth(th*2*np.pi/val20,0.5)
                rangoh = val20
            if nmh == 3:
                val10=float(ent10.get())
                val20=int(ent20.get())
                val30=0
                val40=0
                th = np.arange(0,val20+1,1)
                yh = val10*sp.square(th*2*np.pi/val20,0.5)
                rangoh = val20
            if nmh == 4:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=int(ent30.get())
                val40=int(ent40.get())
                th = np.arange(val30,val40+1,1)
                yh = val10*np.exp(val20*th)
                rangoh = val40-val30
            if nmh == 5:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(val10,val20+1,1)
                yh = np.piecewise(th, [th>((val20-val10)/3)+val10], [lambda th: th-((val20-val10)/3)-val10])-np.piecewise(th, [th>2*((val20-val10)/3)+val10], [lambda th: th-2*((val20-val10)/3)-val10])
                rangoh = int(val20-val10)
            if nmh == 6:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(val10,val20+1,1)
                yh = ((val20-val10)/3)-np.piecewise(th, [th>((val20-val10)/3)+val10], [lambda th: th-((val20-val10)/3)-val10])+np.piecewise(th, [th>2*((val20-val10)/3)+val10], [lambda th: th-2*((val20-val10)/3)-val10])
                rangoh = int(val20-val10)
            if nmh == 7:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(val10,val20+1,1)
                yh = np.piecewise(th, [th<((val20-val10)/3)+val10], [lambda th: th-val10,(val20-val10)/3])-np.piecewise(th, [th>2*((val20-val10)/3)+val10], [lambda th: th-2*((val20-val10)/3)-val10])
                rangoh = int(val20-val10)
            if nmh == 8:
                val10=float(ent10.get())
                val20=float(ent20.get())
                val30=0
                val40=0
                th = np.arange(val10,val20+1,1)
                t2 = np.arange(0,10/3,0.01)
                rangoh = val20-val10
                expon = np.exp(t2)-1
                y1 = np.piecewise(th, [th<val10+rangoh/3], [lambda th: np.exp((th-val10)*10/rangoh)-max(expon)-1])
                y2 = np.piecewise(th, [th>val10+rangoh/3], [lambda th: -np.exp((th-val10-rangoh/3)*10/rangoh)+1])
                y3 =-np.piecewise(th, [th>val10+(2*rangoh)/3], [lambda th: -np.exp((th-val10-rangoh/3)*10/rangoh)+1])
                y4 = np.piecewise(th, [th>val10+(2*rangoh)/3], [lambda th: np.exp((th-val10-(2*rangoh)/3)*10/rangoh)-max(expon)-1])
                yh = y1 + y2 + y3 + y4
            
            tpro = np.arange(np.amin(tx)-rangoh,np.amax(tx)+1+rangoh,intmuestr)
            tconv = np.arange(np.amin(tx)+np.amin(th),np.amax(tx)+np.amax(th)+1,intmuestr)
            yhf = np.flip(yh)
            
            if (rango <= 7) or (rangoh <=7):
                messagebox.showerror(title="Error", message="No se puede realizar la gráfica con tan pocas muestras.\nPor favor digite un rango de muestras mayor o igual a 8 para garantizar una correcta visibilidad de cada función en el dominio discreto.", master = menu)
            else:
                j = 0
                #yxi = np.zeros_like(tconv,float)
                yxi = np.zeros_like(tpro,float)
                yconv = np.zeros_like(tconv,float)
    
                while j <= rango:
                    np.put(yxi,j+rangoh,yx[j])
                    #yxi[j+np.amin(th)+rangoh]=yx[j]
                    j=j+1
                
                j = 0
                yhi = np.zeros_like(tpro,float)
                while j <= rangoh:
                    np.put(yhi,j,yhf[j])
                    #yhi[j]=yhf[j]
                    j=j+1
                    
                plt.figure(3)
                plt.clf()
                plt.title('Procedimiento')
                plt.stem(tpro, yxi,'green')
                plt.stem(tpro, yhi, 'red')
                plt.gcf().canvas.draw()
                
                plt.figure(4)
                plt.clf()
                plt.title('Convolución')
                plt.stem(tconv, yconv,'blue')
                plt.gcf().canvas.draw()
                
                time.sleep(1)
                
                for i in range(0, int(rango) + int(rangoh) + 1):
                    xporh = np.multiply(yxi,yhi)
                    yconv[i] = np.sum(xporh)
                    plt.figure(4)
                    plt.clf()
                    plt.title('Convolución')
                    plt.stem(tconv, yconv,'blue')
                    plt.gcf().canvas.draw()
                    plt.figure(3)
                    plt.clf()
                    plt.title('Procedimiento')
                    plt.stem(tpro, yxi,'green')
                    plt.stem(tpro, yhi, 'red')
                    plt.gcf().canvas.draw()
                    yhi = np.roll(yhi,1)   
                    time.sleep(.3)
                yconvol=np.convolve(yx,yh,'full')
                plt.figure(4)
                plt.clf()
                plt.title('Convolución')
                plt.stem(tconv, yconvol,'blue')
                plt.gcf().canvas.draw()
                
        
        
    btn2=Button(fr10, text="Mostrar convolución", borderwidth = 5, bg="lawn green", fg="grey12", state=DISABLED, command=mostrarconv,padx=8,pady=7)
    btn2.grid(row=3,column=0,columnspan=2, pady=9)
    inicio.destroy()
    fig1 = plt.figure(figsize=(4,2),edgecolor="red",facecolor="lightgray")
    canv1 = FigureCanvasTkAgg(fig1, master=fr11)
    canv1.get_tk_widget().grid(row=4, column=1, padx=(1, 1), pady=(10, 10))
    canv1.get_tk_widget().configure(bg="grey20")
    fig2 = plt.figure(figsize=(4,2),edgecolor="red",facecolor="lightgray")
    canv2 = FigureCanvasTkAgg(fig2, master=fr9)
    canv2.get_tk_widget().grid(row=4, column=1, padx=(1, 1), pady=(10, 10))
    canv2.get_tk_widget().configure(bg="grey20")
    fig3 = plt.figure(figsize=(7,3.29),edgecolor="red",facecolor="lightgray")
    canv3 = FigureCanvasTkAgg(fig3, master=fr80)
    canv3.get_tk_widget().grid(row=4, column=1, padx=(1, 1), pady=(10, 10))
    canv3.get_tk_widget().configure(bg="grey20")
    fig4 = plt.figure(figsize=(7,3.29),edgecolor="red",facecolor="lightgray")
    canv4 = FigureCanvasTkAgg(fig4, master=fr80)
    canv4.get_tk_widget().grid(row=5, column=1, padx=(1, 1), pady=(10, 10))
    canv4.get_tk_widget().configure(bg="grey20")
btn=Button(fr, text="Iniciar ", borderwidth = 5, padx=20, pady=20, bg="goldenrod1", fg="grey12", command=cerrar)
btn.grid(row=2,column=0)

blnk = Label(fr, text="", pady=10, bg="grey12").grid(row=1,column=0)


inicio.mainloop()