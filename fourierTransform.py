import numpy as np
from scipy import signal as sp
import scipy.io.wavfile as wav
from tkinter import *
import winsound
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from tkinter import messagebox
from scipy import stats
import time

inicio = Tk()
inicio.title("Inicio")
inicio.configure(bg="grey12")

fr = LabelFrame(inicio, font= 41, text="TALLER 2: TRANSFORMADA DE\nFOURIER", fg="goldenrod1", bg="grey12", padx=50, pady=60)
fr.pack(padx=5, pady=5) 

nom = Label(fr, text="Señales y sistemas\nDavid Eduardo Díaz de Moya\nProfesor:\nPedro Juan Narvaez Rosado", fg="goldenrod1", bg="grey12").grid(row=0,column=0)


def cerrar():
    menu=Tk()
    menu.title("Menu")
    menu.configure(bg="grey12")
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
    fr7=LabelFrame(fr2, text="Seleccione el audio:", bg="grey12", fg="goldenrod1", padx=43, pady=33)
    fr7.grid(row=1,column=0,pady=10)
    fun = StringVar(menu)
    eee = StringVar(menu)
    ee = StringVar(menu)
    (tasa1, ECG_1)=wav.read("./soundFiles/ECG_1.wav")
    (tasa2, ECG_2)=wav.read("./soundFiles/ECG_2.wav")
    (tasa3, EEG_1)=wav.read("./soundFiles/EEG_1.wav")
    (tasa4, EEG_2)=wav.read("./soundFiles/EEG_2.wav")
    (tasa5, EMG_1)=wav.read("./soundFiles/EMG_1.wav")
    (tasa6, EMG_2)=wav.read("./soundFiles/EMG_2.wav")


    def parametros(num):
        global nm, y, adver, t, f
        nm = int(num)
        if nm == 1:
            fun.set("./soundFiles/ECG_1.wav")
            (f, y) = wav.read("./soundFiles/ECG_1.wav")
            t = np.arange(0,len(y)/f,1/f)
            winsound.PlaySound('./soundFiles/ECG_1.wav', winsound.SND_ASYNC)
        if nm == 2:
            fun.set("./soundFiles/ECG_2.wav")
            (f, y) = wav.read("./soundFiles/ECG_2.wav")
            t = np.arange(0,len(y)/f,1/f)
            winsound.PlaySound('./soundFiles/ECG_2.wav', winsound.SND_ASYNC)
        if nm == 3:
            fun.set("./soundFiles/EEG_1.wav")
            (f, y)=wav.read("./soundFiles/EEG_1.wav")
            t = np.arange(0,len(y)/f,1/f)
            winsound.PlaySound('./soundFiles/EEG_1.wav', winsound.SND_ASYNC)
        if nm == 4:
            fun.set("./soundFiles/EEG_2.wav")
            (f, y)=wav.read("./soundFiles/EEG_2.wav")
            t = np.arange(0,len(y)/f,1/f)
            winsound.PlaySound('./soundFiles/EEG_2.wav', winsound.SND_ASYNC)
        if nm == 5:
            fun.set("./soundFiles/EMG_1.wav")
            (f, y)=wav.read("./soundFiles/EMG_1.wav")
            t = np.arange(0,len(y)/f,1/f)
            winsound.PlaySound('./soundFiles/EMG_1.wav', winsound.SND_ASYNC)
        if nm == 6:
            fun.set("./soundFiles/EMG_2.wav")
            (f, y)=wav.read("./soundFiles/EMG_2.wav")
            t = np.arange(0,len(y)/f,1/f) 
            winsound.PlaySound('./soundFiles/EMG_2.wav', winsound.SND_ASYNC)
        y = y/max(y)
        btn2.configure(state=NORMAL)
    r = IntVar()
    q = IntVar()
    j = IntVar()
    Radiobutton(fr7, text="1", variable=r, value=1, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(1)).grid(sticky="W",row=1,column=0)
    Radiobutton(fr7, text="2", variable=r, value=2, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(2)).grid(sticky="W",row=2,column=0)
    Radiobutton(fr7, text="3", variable=r, value=3, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(3)).grid(sticky="W",row=3,column=0)
    Radiobutton(fr7, text="4", variable=r, value=4, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(4)).grid(sticky="W",row=4,column=0)
    Radiobutton(fr7, text="5", variable=r, value=5, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(5)).grid(sticky="W",row=5,column=0)
    Radiobutton(fr7, text="6", variable=r, value=6, bg="grey12", fg="goldenrod1", selectcolor="grey38", indicatoron=0, width=12,command=lambda: parametros(6)).grid(sticky="W",row=6,column=0)
    fr3=LabelFrame(fr2, text="", bg="grey12", fg="goldenrod1", padx=25, pady=35)
    fr3.grid(row=9,column=0,padx=5,pady=5)
    
    fr7=LabelFrame(fr2, text="", bg="grey12", fg="goldenrod1", padx=24, pady=30)
    fr7.grid(row=4,column=0,pady=5)
    fr10=LabelFrame(fr8, bg="grey12", padx=10, pady=10)
    fr10.grid(row=1,column=0, padx=5, pady=5)
    asd=Label(fr7, textvariable=fun, width=14,bg="grey12",fg="green1",font=20, pady=10).grid(row=1,column=0)
    fku=Label(fr7, text="Audio:",bg="grey12", fg="goldenrod1").grid(row=0,column=0)
    fr11=LabelFrame(fr8, bg="grey12", padx=10, pady=10)
    fr11.grid(row=2,column=0, padx=5, pady=5 )
    def graficar():
        global y, t, f
        yfi = np.fft.fft(y)
        ff = np.fft.fftfreq(len(t))*f
        N = len(y)
        Pow = (np.abs(yfi)**2)/N
        #Caracterización en el tiempo
        u = 0
        for i in range(0,N):
            u = u+(1/N)*y[i]
        asc = np.sort(y)
        i = (N+1)/2
        if i.is_integer() == True:
            Me = asc[int(i)]
        else:
            Me = (asc[int(np.floor(i))]+asc[int(np.ceil(i))])/2
        i = N/4
        if i.is_integer() == True:
            Q1 = asc[int(i)]
        else:
            Q1 = (asc[int(np.floor(i))]+asc[int(np.ceil(i))])/2
        i2 = 3*N/4
        if i2.is_integer() == True:
            Q3 = asc[int(i2)]
        else:
            Q3 = (asc[int(np.floor(i2))]+asc[int(np.ceil(i2))])/2
        IQR = Q3-Q1
        sigma = 0
        sigmaabs = 0
        for i in range(0,N):
            sigma = sigma+(1/N)*((y[i]-u)**2)
            sigmaabs = sigmaabs+(1/N)*abs(y[i]-u)
        sigma = np.sqrt(sigma)
        ca = 0
        cr = 0
        cv = 0
        P = 0
        for i in range(0,N):
            ca = ca + ((1/N)*((y[i]-u)**3))/(sigma**3)
            cr = cr + (y[i]-u)**4
            P = P + (1/(2*N+1))*(abs(y[i])**2)
        cr = cr*(1/(N*(sigma**4)))
        cv = sigma/u
        
        result = np.where(ff == 0)
        #Caracterización en la frecuencia
        Nf = int(len(yfi)/2)
        yf = np.zeros(Nf, np.complex64)
        for i in range(0,Nf):
            yf[i] = yfi[i+Nf-1] 
        yf = np.abs(yf)
        uf = 0
        for i in range(0,Nf):
            uf = uf+(1/Nf)*yf[i]

        ascf = np.sort(yf)
        i = (Nf+1)/2
        if i.is_integer() == True:
            Mef = ascf[int(i)]
        else:
            Mef = (ascf[int(np.floor(i))]+ascf[int(np.ceil(i))])/2
        i = Nf/4
        if i.is_integer() == True:
            Q1f = ascf[int(i)]
        else:
            Q1f = (ascf[int(np.floor(i))]+ascf[int(np.ceil(i))])/2
        i2 = 3*Nf/4
        if i2.is_integer() == True:
            Q3f = ascf[int(i2)]
        else:
            Q3f = (ascf[int(np.floor(i2))]+ascf[int(np.ceil(i2))])/2
        IQRf = Q3f-Q1f
        print(Q1f)
        print(Q3f)
        sigmaf = 0
        sigmaabsf = 0
        for i in range(0,Nf):
            sigmaf = sigmaf+(1/Nf)*((yf[i]-uf)**2)
            sigmaabsf = sigmaabsf+(1/Nf)*abs(yf[i]-uf)
        sigmaf = np.sqrt(sigmaf)
        caf = 0
        crf = 0
        cvf = 0
        Pf = 0
        for i in range(0,Nf):
            caf = caf + ((1/Nf)*((yf[i]-uf)**3))/(sigmaf**3)
            crf = crf + ((1/Nf)*((yf[i]-uf)**4))/(sigmaf**4)
            cvf = sigmaf/uf
            Pf = Pf + (1/(Nf+1))*(abs(yf[i])**2)

        carac=Tk()
        carac.title("Características del audio")
        carac.configure(bg="grey12")
        dat = Entry(carac, width=40, fg='goldenrod1', bg="grey12", justify=CENTER, font=('Times New Roman',16,'bold')) 
        dat.grid(row=0, column=0, columnspan=2)
        dat.insert(END, 'Dominio del Tiempo')
        dat2 = Entry(carac, width=40, fg='goldenrod1', bg="grey12", justify=CENTER, font=('Times New Roman',16,'bold')) 
        dat2.grid(row=0, column=2, columnspan=2) 
        dat2.insert(END, 'Dominio de la Frecuencia')
        lst = [('Promedio de la señal',u,'Promedio de la señal',uf),
               ('Mediana de la señal',Me,'Mediana de la señal',Mef),
               ('Desviación estandar',sigma,'Desviación estandar',sigmaf),
               ('Desviación media absoluta',sigmaabs,'Desviación media absoluta',sigmaabsf),
               ('Primer cuartil',Q1,'Primer cuartil',Q1f),
               ('Tercer cuartil',Q3,'Tercer cuartil',Q3f),
               ('IQR',IQR,'IQR',IQRf),
               ('Asimetría de la señal',ca,'Asimetría de la señal',caf),
               ('Curtosis de la señal',cr,'Curtosis de la señal',crf),
               ('Coeficiente de variación',cv,'Coeficiente de variación',cvf),
               ('Potencia de la señal',P,'Potencia de la señal',Pf),]
        for i in range(1,12): 
            for j in range(0,4): 
                  
                e = Entry(carac, width=27, fg='lawn green', bg="grey12", font=('Times New Roman',12,'bold')) 
                e.grid(row=i, column=j) 
                e.insert(END, lst[i-1][j]) 
        
        plt.figure(1)
        plt.clf()
        plt.title('Representación del audio en el tiempo')
        plt.plot(t, y,'green')
        plt.gcf().canvas.draw()
        plt.figure(2)
        plt.clf()
        plt.title('Representación del audio en la frecuencia')
        plt.plot(ff, np.abs(yfi),'red')
        plt.gcf().canvas.draw()
        plt.figure(3)
        plt.clf()
        plt.title('Potencia')
        plt.plot(ff, Pow, 'blue')
        plt.gcf().canvas.draw()
        plt.figure(4)
        plt.clf()
        plt.title('Espectrograma')
        plt.specgram(y, Fs = f, cmap=plt.get_cmap('jet'))
        plt.gcf().canvas.draw()

 
            
    btn2=Button(fr3, text="Analizar audio", borderwidth = 5, bg="lawn green", fg="grey1", state=DISABLED, padx = 20, pady = 10, command=graficar)
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