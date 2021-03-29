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

fr = LabelFrame(inicio, font= 40, text="TALLER 1: SERIES DE FOURIER", fg="goldenrod1", bg="grey12", padx=50, pady=60)
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
    fr8.grid(row=0,column=1)
    fr90=Frame(menu, bg="grey12", padx=10, pady=10)
    fr90.grid(row=0,column=10)
    fr9=LabelFrame(fr90, bg="grey12", padx=10, pady=10)
    fr9.grid(row=0,column=0,padx=5,pady=5)
    fr99=LabelFrame(fr90, bg="grey12", padx=10, pady=10)
    fr99.grid(row=1,column=0,padx=5,pady=5)
    fr7=LabelFrame(fr2, text="Seleccione la señal:", bg="grey12", fg="goldenrod1", padx=26, pady=20)
    fr7.grid(row=1,column=0,pady=10)
    str1 = StringVar(menu)
    str1.set("# de armónicos")
    str2 = StringVar(menu)
    str2.set("Amplitud")
    str3 = StringVar(menu)
    str3.set("Periodo")
    str4 = StringVar(menu)
    str4.set("Inicio")
    str5 = StringVar(menu)
    str5.set("Fin")
    fun = StringVar(menu)
    eee = StringVar(menu)
    ee = StringVar(menu)
    global adver
    adver = 1
    
    def parametros(num):
        global nm, y, adver
        nm = int(num)
        if nm == 1:
            fun.set("Rampa 1")
            y1 = np.piecewise(t, [t>10/3], [lambda t: np.exp(t-10/3)-1])
            y2 = -np.piecewise(t, [t>20/3], [lambda t: np.exp(t-10/3)-np.exp((20/3)-10/3)])
            y = y1 + y2
        if nm == 2:
            fun.set("Rampa 2")
            y=np.piecewise(t, [t<10/3], [lambda t: t,10/3])-np.piecewise(t, [t>20/3], [lambda t: t-20/3])
        if nm == 3:
            fun.set("Rampa 3")
            y=np.piecewise(t, [t>10/3], [lambda t: t-10/3])-np.piecewise(t, [t>20/3], [lambda t: t-20/3])
        if nm == 4:
            fun.set("Colmillo 1")
            t2 = np.arange(0,10/3,0.01)
            a = max(t)
            expon = np.exp(t2)-1
            y1 = np.piecewise(t, [t<a/3], [lambda t: np.exp(-(t-a/3)*10/a)-1])
            y2 = -np.piecewise(t, [t>a/3], [lambda t: np.exp(-(t-2*a/3)*10/a)-max(expon)-1])
            y3 = np.piecewise(t, [t>2*a/3], [lambda t: np.exp(-(t-2*a/3)*10/a)-max(expon)-1])
            y4 = np.piecewise(t, [t>2*a/3], [lambda t: np.exp(-(t-a)*10/a)-1])
            y = y1 + y2 + y3 + y4
        if nm == 5:
            fun.set("Colmillo 2")
            t2 = np.arange(0,10/3,0.01)
            a = max(t)
            expon = np.exp(t2)-1
            y1 = -np.piecewise(t, [t<a/3], [lambda t: np.exp(t*10/a)-max(expon)-1])
            y2 = np.piecewise(t, [t>a/3], [lambda t: np.exp((t-a/3)*10/a)-1])
            y3 = -np.piecewise(t, [t>2*a/3], [lambda t: np.exp((t-a/3)*10/a)-1])
            y4 = -np.piecewise(t, [t>2*a/3], [lambda t: np.exp((t-2*a/3)*10/a)-max(expon)-1])
            y = y1 + y2 + y3 + y4
        ent1.configure(state=NORMAL)
        ent2.configure(state=NORMAL)
        ent3.configure(state=NORMAL)
        ent44.configure(state=NORMAL)
        ent45.configure(state=NORMAL)
        btn2.configure(state=NORMAL)
        plt.figure(1)
        plt.clf()
        plt.title('Señal')
        plt.plot(t, y,'red')
        plt.gcf().canvas.draw()
        if adver == 1:
            messagebox.showwarning(title="Advertencia", message="La señal se generará entre el punto inicial y final establecido. El periodo es exclusivamente para la señal recreada en series de Fourier. Si selecciona un periodo menor a la distancia entre el punto inicial y final de la señal, esta se va a recortar hasta el punto donde termine dicho periodo.", master = menu)
            adver = 0
    r = IntVar()
    q = IntVar()
    j = IntVar()
    Radiobutton(fr7, text="Rampa 1", variable=r, value=1, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(1)).grid(sticky="W",row=1,column=0)
    Radiobutton(fr7, text="Rampa 2", variable=r, value=2, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(2)).grid(sticky="W",row=2,column=0)
    Radiobutton(fr7, text="Rampa 3", variable=r, value=3, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(3)).grid(sticky="W",row=3,column=0)
    Radiobutton(fr7, text="Colmillo 1", variable=r, value=4, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(4)).grid(sticky="W",row=4,column=0)
    Radiobutton(fr7, text="Colmillo 2", variable=r, value=5, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(5)).grid(sticky="W",row=5,column=0)
    fr3=LabelFrame(fr2, text="Digite parámetros:", bg="grey12", fg="goldenrod1", padx=10, pady=20)
    fr3.grid(row=9,column=0,padx=5,pady=5)
    fr4=Frame(fr3,bg="grey12")
    fr4.grid(row=1,column=0)
    fr5=Frame(fr3,bg="grey12")
    fr5.grid(row=2,column=0)
    fr6=Frame(fr3,bg="grey12")
    fr6.grid(row=3,column=0)
    fr66=Frame(fr3,bg="grey12")
    fr66.grid(row=4,column=0)
    fr67=Frame(fr3,bg="grey12")
    fr67.grid(row=5,column=0)
    par1=Label(fr4,textvariable=str1, width=12, anchor="e",bg="grey12",fg="goldenrod1").grid(row=0,column=0)
    par2=Label(fr5,textvariable=str2, width=12, anchor="e",bg="grey12",fg="goldenrod1").grid(row=0,column=0)
    par3=Label(fr6,textvariable=str3, width=12, anchor="e",bg="grey12",fg="goldenrod1").grid(row=0,column=0)
    par4=Label(fr66,textvariable=str4, width=12, anchor="e",bg="grey12",fg="goldenrod1").grid(row=0,column=0)
    par5=Label(fr67,textvariable=str5, width=12, anchor="e",bg="grey12",fg="goldenrod1").grid(row=0,column=0)
    ent1=Entry(fr4, text="", bg="grey28", fg="goldenrod1", width=4, bd=5, state=DISABLED)
    ent1.grid(sticky="E",row=0,column=1)
    ent2=Entry(fr5, text="", bg="grey28", fg="goldenrod1", width=4, bd=5, state=DISABLED)
    ent2.grid(sticky="E",row=0,column=1)
    ent3=Entry(fr6, text="", bg="grey28", fg="goldenrod1", width=4, bd=5, state=DISABLED)
    ent3.grid(sticky="E",row=0,column=1)
    ent44=Entry(fr66, text="", bg="grey28", fg="goldenrod1", width=4, bd=5, state=DISABLED)
    ent44.grid(sticky="E",row=0,column=1)
    ent45=Entry(fr67, text="", bg="grey28", fg="goldenrod1", width=4, bd=5, state=DISABLED)
    ent45.grid(sticky="E",row=0,column=1)
    fr7=LabelFrame(fr2, text="", bg="grey12", fg="goldenrod1", padx=7, pady=15)
    fr7.grid(row=4,column=0,pady=5)
    fr10=LabelFrame(fr8, bg="grey12", padx=10, pady=10)
    fr10.grid(row=1,column=0, padx=5, pady=5)
    asd=Label(fr7, textvariable=fun, width=14,bg="grey12",fg="green1",font=20, pady=10).grid(row=1,column=0)
    fku=Label(fr7, text="Función:",bg="grey12", fg="goldenrod1").grid(row=0,column=0)
    fr11=LabelFrame(fr8, bg="grey12", padx=10, pady=10)
    fr11.grid(row=2,column=0, padx=5, pady=5 )
    def graficar():
        global val1,val2,val3,factor,y,t,yx,tx,ins,p,sad
        n=int(ent1.get())
        A=float(ent2.get())
        T=float(ent3.get())
        Ti=float(ent44.get())
        Tf=float(ent45.get())
        dt = 1/100
        t = np.arange(Ti,Tf,dt)
        rango = Tf-Ti
        if nm == 1:
            fun.set("Rampa 1")
            y1 = np.piecewise(t, [t>Ti+rango/3], [lambda t: np.exp((t-Ti-rango/3)*10/rango)-1])
            y2 = -np.piecewise(t, [t>Ti+2*rango/3], [lambda t: np.exp((t-Ti-rango/3)*10/rango)-np.exp(((Ti+2*rango/3)-Ti-rango/3)*10/rango)])
            y = y1 + y2
        if nm == 2:
            fun.set("Rampa 2")
            y=np.piecewise(t, [t<Ti+rango/3], [lambda t: t-Ti,rango/3])-np.piecewise(t, [t>Ti+2*rango/3], [lambda t: t-Ti-2*rango/3])
        if nm == 3:
            fun.set("Rampa 3")
            y=np.piecewise(t, [t>Ti+rango/3], [lambda t: t-Ti-rango/3])-np.piecewise(t, [t>Ti+2*rango/3], [lambda t: t-Ti-2*rango/3])
        if nm == 4:
            fun.set("Colmillo 1")
            t2 = np.arange(0,10/3,0.01)
            a = rango
            expon = np.exp(t2)-1
            y1 = np.piecewise(t, [t<Ti+a/3], [lambda t: np.exp(-(t-Ti-a/3)*10/a)-1])
            y2 = -np.piecewise(t, [t>Ti+a/3], [lambda t: np.exp(-(t-Ti-2*a/3)*10/a)-max(expon)-1])
            y3 = np.piecewise(t, [t>Ti+2*a/3], [lambda t: np.exp(-(t-Ti-2*a/3)*10/a)-max(expon)-1])
            y4 = np.piecewise(t, [t>Ti+2*a/3], [lambda t: np.exp(-(t-Ti-a)*10/a)-1])
            y = y1 + y2 + y3 + y4
        if nm == 5:
            fun.set("Colmillo 2")
            t2 = np.arange(0,10/3,0.01)
            a = rango
            expon = np.exp(t2)-1
            y1 = -np.piecewise(t, [t<Ti+a/3], [lambda t: np.exp((t-Ti)*10/a)-max(expon)-1])
            y2 = np.piecewise(t, [t>Ti+a/3], [lambda t: np.exp((t-Ti-a/3)*10/a)-1])
            y3 = -np.piecewise(t, [t>Ti+2*a/3], [lambda t: np.exp((t-Ti-a/3)*10/a)-1])
            y4 = -np.piecewise(t, [t>Ti+2*a/3], [lambda t: np.exp((t-Ti-2*a/3)*10/a)-max(expon)-1])
            y = y1 + y2 + y3 + y4
        x = np.zeros(int(100*T))
        t1 = np.zeros(int(100*T))
        y = (A/max(y))*y
        for i in range(0,int(100*T)):
             x[i] = y[i]
             t1[i] = t[i]


        Wo = 2*np.pi/T
        An = np.zeros((n,1))
        Bn = np.zeros((n,1))
        l = len(t1)
        N = np.arange(1,n+1)
        Cn = np.zeros((n,1))
        Phin = np.zeros((n,1))
        A0 = 0
        plt.figure(1)
        plt.clf()
        plt.title('Señal original')
        plt.plot(t, y,'red')
        plt.gcf().canvas.draw()
        for i in range(1,l):
             A0 = A0 + (1/T)*x[i]*dt
        xf = A0
        Cn[0] = A0
        t2 = np.arange(min(t1),2*max(t1)-min(t1),0.01)
        time.sleep(1)
        for  i in range(1,n):
            for j in range(1,l):
                An[i] = An[i] + ((2/T)*x[j]*np.cos(i*t[j]*Wo))*dt
                Bn[i] = Bn[i] + ((2/T)*x[j]*np.sin(i*t[j]*Wo))*dt
            Cn[i] = np.sqrt((An[i])**2 + (Bn[i])**2)
            Phin[i] = np.arctan(Bn[i]/An[i])
            xf = xf + An[i]*np.cos(i*Wo*t2) + Bn[i]*np.sin(i*Wo*t2)
            plt.figure(2)
            plt.clf()
            plt.title('Señal reconstruida')
            plt.plot(t2, xf,'blue')
            plt.gcf().canvas.draw()
            plt.figure(3)
            plt.clf()
            plt.title('Espectro de amplitud')
            plt.stem(N, Cn,'green')
            plt.gcf().canvas.draw()
            plt.figure(4)
            plt.clf()
            plt.title('Espectro de fase')
            plt.stem(N, Phin,'orange')
            plt.gcf().canvas.draw()
            time.sleep(.1)
            
    btn2=Button(fr3, text="Graficar", borderwidth = 5, bg="lawn green", fg="grey1", state=DISABLED, padx = 20, pady = 10, command=graficar)
    btn2.grid(row=10,column=0, columnspan=2, pady = 10)
    inicio.destroy()
    fig1 = plt.figure(figsize=(5,3),edgecolor="red",facecolor="lightgray")
    canv1 = FigureCanvasTkAgg(fig1, master=fr10)
    canv1.get_tk_widget().grid(row=4, column=1, padx=(1, 1), pady=(10, 10))
    canv1.get_tk_widget().configure(bg="grey20")
    fig2 = plt.figure(figsize=(5,3),edgecolor="red",facecolor="lightgray")
    canv2 = FigureCanvasTkAgg(fig2, master=fr11)
    canv2.get_tk_widget().grid(row=5, column=10, padx=(1, 1), pady=(10, 10))
    canv2.get_tk_widget().configure(bg="grey20")
    fig30 = plt.figure(figsize=(5,3),edgecolor="red",facecolor="lightgray")
    canv30 = FigureCanvasTkAgg(fig30, master=fr9)
    canv30.get_tk_widget().grid(row=4, column=1, padx=(1, 1), pady=(10, 10))
    canv30.get_tk_widget().configure(bg="grey20")
    fig40 = plt.figure(figsize=(5,3),edgecolor="red",facecolor="lightgray")
    canv40 = FigureCanvasTkAgg(fig40, master=fr99)
    canv40.get_tk_widget().grid(row=5, column=1, padx=(1, 1), pady=(10, 10))
    canv40.get_tk_widget().configure(bg="grey20")
    menu.mainloop()
btn=Button(fr, text="Iniciar ", borderwidth = 5, padx=20, pady=20, bg="goldenrod1", fg="grey12", command=cerrar)
btn.grid(row=2,column=0)

blnk = Label(fr, text="", pady=10, bg="grey12").grid(row=1,column=0)


inicio.mainloop()