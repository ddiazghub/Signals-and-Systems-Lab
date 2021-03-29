import numpy as np
from scipy import signal as sp
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

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
    t = np.arange(-5,5,0.01)
    fr2=Frame(menu, bg="grey12", padx=10, pady=10)
    fr2.grid(row=0,column=0)
    fr8=Frame(menu, bg="grey12", padx=10, pady=10)
    fr8.grid(row=0,column=1)
    fr9=LabelFrame(menu, text="", bg="grey12", padx=10, pady=10)
    fr9.grid(row=0,column=2,padx=5,pady=5)
    fr7=LabelFrame(fr2, text="Seleccione la señal:", bg="grey12", fg="goldenrod1", padx=26, pady=20)
    fr7.grid(row=1,column=0)
    str1 = StringVar(menu)
    str1.set("Parametro 1")
    str2 = StringVar(menu)
    str2.set("Parametro 2")
    str3 = StringVar(menu)
    str3.set("Parametro 3")
    fun = StringVar(menu)
    eee = StringVar(menu)
    ee = StringVar(menu)
    def parametros(num):
        global nm
        nm = int(num)
        if nm == 1:
            str1.set("Amplitud (A)")
            str2.set("Frecuencia (f)")
            str3.set("Fase (φ)")
            ent1.configure(state=NORMAL)
            ent2.configure(state=NORMAL)
            ent3.configure(state=NORMAL)
            fun.set("Asen(2πft+φ)")
            y = np.sin(np.pi*t)
        if nm == 2:
            str1.set("Amplitud (A)")
            str2.set("Ancho (dt)")
            str3.set("Valor inicial (t0)")
            ent1.configure(state=NORMAL)
            ent2.configure(state=NORMAL)
            ent3.configure(state=NORMAL)
            fun.set("A(u(t-t0)-u(t-t0-dt))")
            y = np.piecewise(t,t>=-1,[1,0])-np.piecewise(t,t>=3,[1,0])
        if nm == 3:
            str1.set("a")
            str2.set("b")
            str3.set("c")
            ent1.configure(state=NORMAL)
            ent2.configure(state=NORMAL)
            ent3.configure(state=NORMAL)
            fun.set("ax²+bx+c")
            y = t**2
        if nm == 4:
            str1.set("A")
            str2.set("B")
            str3.set("")
            ent1.configure(state=NORMAL)
            ent2.configure(state=NORMAL)
            ent3.configure(state=DISABLED)
            fun.set("Ae⁻ᴮᵗ")
            y = np.exp(-t)
        if nm == 5:
            str1.set("Pendiente (m)")
            str2.set("Intersecto (b)")
            str3.set("")
            ent1.configure(state=NORMAL)
            ent2.configure(state=NORMAL)
            ent3.configure(state=DISABLED)
            fun.set("mt+b")
            y = t
        if nm == 6:
            str1.set("")
            str2.set("")
            str3.set("")
            ent1.configure(state=DISABLED)
            ent2.configure(state=DISABLED)
            ent3.configure(state=DISABLED)
            fun.set("Triangular")
            y = sp.sawtooth(t, 0.5)
        if nm == 7:
            str1.set("")
            str2.set("")
            str3.set("")
            ent1.configure(state=DISABLED)
            ent2.configure(state=DISABLED)
            ent3.configure(state=DISABLED)
            fun.set("Cuadrada")
            y = sp.square(t)
        if nm == 8:
            str1.set("")
            str2.set("")
            str3.set("")
            ent1.configure(state=DISABLED)
            ent2.configure(state=DISABLED)
            ent3.configure(state=DISABLED)
            fun.set("Impulso Lento")
            y=np.piecewise(t, [t<(10/3)-5], [lambda t: 5+t,10/3])-np.piecewise(t, [t>(20/3)-5], [lambda t: t-1.66])
        rdb1.configure(state=NORMAL)
        rdb2.configure(state=NORMAL)
        rdb3.configure(state=NORMAL)
        plt.figure(1)
        plt.clf()
        plt.title('Señal')
        plt.plot(t, y,'orange')
        plt.gcf().canvas.draw()
    r = IntVar()
    q = IntVar()
    j = IntVar()
    Radiobutton(fr7, text="Senoidal", variable=r, value=1, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(1)).grid(sticky="W",row=1,column=0)
    Radiobutton(fr7, text="Pulso", variable=r, value=2, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(2)).grid(sticky="W",row=2,column=0)
    Radiobutton(fr7, text="Cuadrática", variable=r, value=3, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(3)).grid(sticky="W",row=3,column=0)
    Radiobutton(fr7, text="Exponencial", variable=r, value=4, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(4)).grid(sticky="W",row=4,column=0)
    Radiobutton(fr7, text="Lineal", variable=r, value=5, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(5)).grid(sticky="W",row=5,column=0)
    Radiobutton(fr7, text="Triangular", variable=r, value=6, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(6)).grid(sticky="W",row=6,column=0)
    Radiobutton(fr7, text="Cuadrada", variable=r, value=7, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(7)).grid(sticky="W",row=7,column=0)
    Radiobutton(fr7, text="Impulso lento", variable=r, value=8, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(8)).grid(sticky="W",row=8,column=0)
    fr3=LabelFrame(fr2, text="Digite parámetros:", bg="grey12", fg="goldenrod1", padx=10, pady=20)
    fr3.grid(row=9,column=0,padx=5,pady=5)
    fr4=Frame(fr3,bg="grey12")
    fr4.grid(row=1,column=0, pady=5)
    fr5=Frame(fr3,bg="grey12")
    fr5.grid(row=2,column=0)
    fr6=Frame(fr3,bg="grey12")
    fr6.grid(row=3,column=0, pady=5)
    par1=Label(fr4,textvariable=str1, width=12, anchor="e",bg="grey12",fg="goldenrod1").grid(row=0,column=0)
    par2=Label(fr5,textvariable=str2, width=12, anchor="e",bg="grey12",fg="goldenrod1").grid(row=0,column=0)
    par3=Label(fr6,textvariable=str3, width=12, anchor="e",bg="grey12",fg="goldenrod1").grid(row=0,column=0)
    ent1=Entry(fr4, text="", bg="grey28", fg="goldenrod1", width=4, bd=5, state=DISABLED)
    ent1.grid(sticky="E",row=0,column=1)
    ent2=Entry(fr5, text="", bg="grey28", fg="goldenrod1", width=4, bd=5, state=DISABLED)
    ent2.grid(sticky="E",row=0,column=1)
    ent3=Entry(fr6, text="", bg="grey28", fg="goldenrod1", width=4, bd=5, state=DISABLED)
    ent3.grid(sticky="E",row=0,column=1)
    fr7=LabelFrame(fr8, text="", bg="grey12", fg="goldenrod1", padx=26, pady=20)
    fr7.grid(row=0,column=0)
    fr10=LabelFrame(fr8, text="Operación a realizar:", bg="grey12", fg="goldenrod1", padx=31, pady=20)
    fr10.grid(row=1,column=0)
    asd=Label(fr7, textvariable=fun, width=14,bg="grey12",fg="green1",font=20, pady=10).grid(row=1,column=0)
    fku=Label(fr7, text="Función:",bg="grey12", fg="goldenrod1").grid(row=0,column=0)
    def accion(des):
        global p
        p=int(des)
        if p == 1:
            eee.set("Amplificar")
            ee.set("Atenuar")
        if p == 2:
            eee.set("Expandir")
            ee.set("Comprimir")
        if p == 3:
            eee.set("Adelantar")
            ee.set("Retardar")
        rdb4.configure(state=NORMAL)
        rdb5.configure(state=NORMAL)
    def f123(asd):
        global sad
        sad=int(asd)
        btn2.configure(state=NORMAL)
        ent4.configure(state=NORMAL)
    
    rdb1=Radiobutton(fr10, text="Escalar en amplitud", variable=q, value=1, bg="grey12", fg="goldenrod1", selectcolor="grey38", state=DISABLED, indicatoron=0, width=16, command=lambda: accion(1))
    rdb1.grid(sticky="W",row=1,column=0)
    rdb2=Radiobutton(fr10, text="Escalar en el tiempo", variable=q, value=2, bg="grey12", fg="goldenrod1", selectcolor="grey38", state=DISABLED, indicatoron=0, width=16, command=lambda: accion(2))
    rdb2.grid(sticky="W",row=2,column=0)
    rdb3=Radiobutton(fr10, text="Desplazar en el tiempo", variable=q, value=3, bg="grey12", fg="goldenrod1", selectcolor="grey38", state=DISABLED, indicatoron=0, width=16, command=lambda: accion(3))
    rdb3.grid(sticky="W",row=3,column=0)
    fr11=LabelFrame(fr8, text="", bg="grey12", fg="goldenrod1", padx=30, pady=20)
    fr11.grid(row=2,column=0,pady=8)
    rdb4=Radiobutton(fr11, text="", variable=j, value=1, bg="grey12", fg="goldenrod1", selectcolor="grey38", command=lambda:f123(1), state=DISABLED)
    rdb4.grid(sticky="W",row=0,column=0)
    rdb5=Radiobutton(fr11, text="", variable=j, value=2, bg="grey12", fg="goldenrod1", selectcolor="grey38", command=lambda:f123(2), state=DISABLED)
    rdb5.grid(sticky="W",row=1,column=0)
    lkj=Label(fr11, textvariable=eee, width=13, anchor="w",bg="grey12",fg="goldenrod1").grid(row=0,column=1,columnspan=2)
    lkf=Label(fr11, textvariable=ee, width=13, anchor="w",bg="grey12",fg="goldenrod1").grid(row=1,column=1,columnspan=2)
    ent4=Entry(fr11, bg="grey28", fg="goldenrod1", width=7, bd=5, state=DISABLED)
    ent4.grid(sticky="W",row=3,column=0, columnspan=2)
    def graficar():
        global val1,val2,val3,factor,y,t,yx,tx,ins,p,sad
        v=float(ent4.get())
        grafica=Tk()
        grafica.title("Gráfica")
        grafica.configure(bg="grey12")
        if nm == 1:
            val1=float(ent1.get())
            val2=float(ent2.get())
            val3=float(ent3.get())
            t = np.arange(0,7*(1/val2),1/(100*val2))
            y = val1*np.sin(2*np.pi*val2*t+val3)
            if p == 1:
                tx = t
                if sad == 1:
                    ins=np.arange(1,v+1,(v-1)/100)
                    yx=v*y
                if sad == 2:
                    ins=np.arange(1,v+1,(v-1)/100)
                    yx=(1/v)*y
            if p == 2:
                if sad == 1:
                    ins=np.arange(1,v+1,(v-1)/100)
                    tx = t*v
                    yx=y
                if sad == 2:
                    ins=np.arange(1,v+1,(v-1)/100)
                    tx = t/v
                    yx=y
            if p == 3:
                if sad == 1:
                    ins=np.arange(0,v+1,(v)/100)
                    tx = t-v
                    yx=y
                if sad == 2:
                    ins=np.arange(0,v+1,(v)/100)
                    tx = t+v
                    yx=y
        if nm == 2:
            val1=float(ent1.get())
            val2=float(ent2.get())
            val3=float(ent3.get())
            t = np.arange(val3-1*val2,val3+2*val2,0.0001)
            y = val1*(np.piecewise(t,t>=val3,[1,0])-np.piecewise(t,t>=val3+val2,[1,0]))
            if p == 1:
                tx = t
                if sad == 1:
                    ins=np.arange(1,v+1,(v-1)/100)
                    yx=v*y
                if sad == 2:
                    ins=np.arange(1,v+1,(v-1)/100)
                    yx=(1/v)*y
            if p == 2:
                if sad == 1:
                    ins=np.arange(1,v+1,(v-1)/100)
                    tx = t*v
                    yx=y
                if sad == 2:
                    ins=np.arange(1,v+1,(v-1)/100)
                    tx = t/v
                    yx=y
            if p == 3:
                if sad == 1:
                    ins=np.arange(0,v+1,(v)/100)
                    tx = t-v
                    yx=y
                if sad == 2:
                    ins=np.arange(0,v+1,(v)/100)
                    tx = t+v
                    yx=y
        if nm == 3:
            val1=float(ent1.get())
            val2=float(ent2.get())
            val3=float(ent3.get())
            t = np.arange(-5*np.abs(10/val1)+(-val2/(2*val1)),5*np.abs(10/val1)+(-val2/(2*val1)),0.00001)
            y = (val1*t**2)+(val2*t)+val3
            if p == 1:
                tx = t
                if sad == 1:
                    ins=np.arange(1,v+1,(v-1)/100)
                    yx=v*y
                if sad == 2:
                    ins=np.arange(1,v+1,(v-1)/100)
                    yx=(1/v)*y
            if p == 2:
                if sad == 1:
                    ins=np.arange(1,v+1,(v-1)/100)
                    tx = t*v
                    yx=y
                if sad == 2:
                    ins=np.arange(1,v+1,(v-1)/100)
                    tx = t/v
                    yx=y
            if p == 3:
                if sad == 1:
                    ins=np.arange(0,v+1,(v)/100)
                    tx = t-v
                    yx=y
                if sad == 2:
                    ins=np.arange(0,v+1,(v)/100)
                    tx = t+v
                    yx=y
        if nm == 4:
            val1=float(ent1.get())
            val2=float(ent2.get())
            t = np.arange(0,2*np.abs(5/val2),0.001)
            y = val1*np.exp(-val2*t)
            if p == 1:
                tx = t
                if sad == 1:
                    ins=np.arange(1,v+1,(v-1)/100)
                    yx=v*y
                if sad == 2:
                    ins=np.arange(1,v+1,(v-1)/100)
                    yx=(1/v)*y
            if p == 2:
                if sad == 1:
                    ins=np.arange(1,v+1,(v-1)/100)
                    tx = t*v
                    yx=y
                if sad == 2:
                    ins=np.arange(1,v+1,(v-1)/100)
                    tx = t/v
                    yx=y
            if p == 3:
                if sad == 1:
                    ins=np.arange(0,v+1,(v)/100)
                    tx = t-v
                    yx=y
                if sad == 2:
                    ins=np.arange(0,v+1,(v)/100)
                    tx = t+v
                    yx=y
        if nm == 5:
            val1=float(ent1.get())
            val2=float(ent2.get())
            t = np.arange(-2*np.abs(val1),2*np.abs(val1),0.00001)
            y = val1*t+val2
            if p == 1:
                tx = t
                if sad == 1:
                    ins=np.arange(1,v+1,(v-1)/100)
                    yx=v*y
                if sad == 2:
                    ins=np.arange(1,v+1,(v-1)/100)
                    yx=(1/v)*y
            if p == 2:
                if sad == 1:
                    ins=np.arange(1,v+1,(v-1)/100)
                    tx = t*v
                    yx=y
                if sad == 2:
                    ins=np.arange(1,v+1,(v-1)/100)
                    tx = t/v
                    yx=y
            if p == 3:
                if sad == 1:
                    ins=np.arange(0,v+1,(v)/100)
                    tx = t-v
                    yx=y
                if sad == 2:
                    ins=np.arange(0,v+1,(v)/100)
                    tx = t+v
                    yx=y
        if nm == 6:
            t = np.arange(-10,10,0.001)
            y = sp.sawtooth(t, 0.5)
            if p == 1:
                tx = t
                if sad == 1:
                    ins=np.arange(1,v+1,(v-1)/100)
                    yx=v*y
                if sad == 2:
                    ins=np.arange(1,v+1,(v-1)/100)
                    yx=(1/v)*y
            if p == 2:
                if sad == 1:
                    ins=np.arange(1,v+1,(v-1)/100)
                    tx = t*v
                    yx=y
                if sad == 2:
                    ins=np.arange(1,v+1,(v-1)/100)
                    tx = t/v
                    yx=y
            if p == 3:
                if sad == 1:
                    ins=np.arange(0,v+1,(v)/100)
                    tx = t-v
                    yx=y
                if sad == 2:
                    ins=np.arange(0,v+1,(v)/100)
                    tx = t+v
                    yx=y
        if nm == 7:
            t = np.arange(-10,10,0.001)
            y = sp.square(t)
            if p == 1:
                tx = t
                if sad == 1:
                    ins=np.arange(1,v+1,(v-1)/100)
                    yx=v*y
                if sad == 2:
                    ins=np.arange(1,v+1,(v-1)/100)
                    yx=(1/v)*y
            if p == 2:
                if sad == 1:
                    ins=np.arange(1,v+1,(v-1)/100)
                    tx = t*v
                    yx=y
                if sad == 2:
                    ins=np.arange(1,v+1,(v-1)/100)
                    tx = t/v
                    yx=y
            if p == 3:
                if sad == 1:
                    ins=np.arange(0,v+1,(v)/100)
                    tx = t-v
                    yx=y
                if sad == 2:
                    ins=np.arange(0,v+1,(v)/100)
                    tx = t+v
                    yx=y
        if nm == 8:
            t = np.arange(-5,5,0.01)
            y = np.piecewise(t, [t<(10/3)-5], [lambda t: 5+t,10/3])-np.piecewise(t, [t>(20/3)-5], [lambda t: t-1.66])
            if p == 1:
                tx = t
                if sad == 1:
                    ins=np.arange(1,v+1,(v-1)/100)
                    yx=v*y
                if sad == 2:
                    ins=np.arange(1,v+1,(v-1)/100)
                    yx=(1/v)*y
            if p == 2:
                if sad == 1:
                    ins=np.arange(1,v+1,(v-1)/100)
                    tx = t*v
                    yx=y
                if sad == 2:
                    ins=np.arange(1,v+1,(v-1)/100)
                    tx = t/v
                    yx=y
            if p == 3:
                if sad == 1:
                    ins=np.arange(0,v+1,(v)/100)
                    tx = t-v
                    yx=y
                if sad == 2:
                    ins=np.arange(0,v+1,(v)/100)
                    tx = t+v
                    yx=y
        plt.figure(1)
        plt.clf()
        plt.title('Señal')
        plt.plot(t, y,'orange')
        plt.gcf().canvas.draw()
        qpñqe=Frame(grafica,bg="grey12").grid(row=0,column=3)
        def escala(value=None):
            el=int(sldr.get())
            if p == 1:
                tz = t
                if sad == 1:
                    yz=ins[el]*y
                if sad == 2:
                    yz=(1/ins[el])*y
            if p == 2:
                if sad == 1:
                    tz = t*ins[el]
                    yz=y
                if sad == 2:
                    tz = t/ins[el]
                    yz=y
            if p == 3:
                if sad == 1:
                    tz = t-ins[el]
                    yz=y
                if sad == 2:
                    tz = t+ins[el]
                    yz=y
                    print(np.max)
            plt.figure(3)
            plt.clf()
            plt.title('Comparación')
            plt.plot(tz, yz,t,y,tx,yx,'r','b','k')
            plt.gcf().canvas.draw()
            plt.figure(4)
            plt.clf()
            plt.title('Procedimiento')
            plt.plot(tz, yz, 'b')
            plt.gcf().canvas.draw()
            lrge=Label(qpñqe, text="Procedimiento",fg="blue",bg="grey12").grid(row=1,column=3)
            lrgfge=Label(qpñqe, text="Original",fg="orange",bg="grey12").grid(row=0,column=3)
            lrgeert=Label(qpñqe, text="Nueva señal",fg="red",bg="grey12").grid(row=2,column=3)
        dfe=Frame(grafica,bg="grey12")
        dfe.grid(row=5,column=0,columnspan=3)
        sldr=Scale(dfe,from_=0,to=100,orient=HORIZONTAL,command=escala,sliderlength=30,length=600,showvalue=1,bd=4,bg="grey12",fg="grey30",troughcolor="grey30",relief=GROOVE)
        sldr.grid(row=0,column=0)
        sdfkjbksjd=Label(dfe, text="MUEVEME", bg="grey12",font=20,fg="goldenrod1").grid(row=0,column=1)
        fig2 = plt.figure(figsize=(5,5),facecolor="lightgray")
        canv2 = FigureCanvasTkAgg(fig2, master=grafica)
        canv2.get_tk_widget().grid(row=0, column=0, padx=(1, 1), pady=(10, 10),rowspan=4)
        plt.figure(2)
        plt.clf()
        plt.title('Nueva Señal')
        plt.plot(tx, yx, 'r')
        plt.gcf().canvas.draw()
        fig3 = plt.figure(figsize=(5,5),facecolor="lightgray")
        canv3 = FigureCanvasTkAgg(fig3, master=grafica)
        canv3.get_tk_widget().grid(row=0, column=2, padx=(1, 1), pady=(10, 10),rowspan=4)
        fig4 = plt.figure(figsize=(5,5),facecolor="lightgray")
        canv4 = FigureCanvasTkAgg(fig4, master=grafica)
        canv4.get_tk_widget().grid(row=0, column=1, padx=(1, 1), pady=(10, 10),rowspan=4)
        def salir():
            menu.destroy()
            grafica.destroy()
        btn10=Button(qpñqe, text="Cerrar", borderwidth = 5, bg="red", fg="black", command=salir, padx=20,pady=20)
        btn10.grid(row=3,column=3)
    btn2=Button(fr11, text="Graficar", borderwidth = 5, bg="goldenrod1", fg="grey12", state=DISABLED, command=graficar)
    btn2.grid(row=3,column=2)
    inicio.destroy()
    fig1 = plt.figure(figsize=(5,5),edgecolor="red",facecolor="lightgray")
    canv1 = FigureCanvasTkAgg(fig1, master=fr9)
    canv1.get_tk_widget().grid(row=4, column=1, padx=(1, 1), pady=(10, 10))
    canv1.get_tk_widget().configure(bg="grey20")
    menu.mainloop()
btn=Button(fr, text="Iniciar ", borderwidth = 5, padx=20, pady=20, bg="goldenrod1", fg="grey12", command=cerrar)
btn.grid(row=2,column=0)

blnk = Label(fr, text="", pady=10, bg="grey12").grid(row=1,column=0)


inicio.mainloop()