from tkinter import *
from tkinter import ttk
import pandas as pd

class calculadora(Frame):
    def __init__(self, meumaster):
        super().__init__()
        self.log = StringVar()
        self.text_DD = StringVar()
        self.result = StringVar()
        self.numerology = StringVar()
        self.PRBs = StringVar()
        self.Overhead = StringVar()
        self.text_frame = StringVar()
        self.text_bw = StringVar()
        self.text_carries = StringVar()
        self.text_modulation = StringVar()
        self.text_scaling_factor = StringVar()
        self.text_SC = StringVar()
        self.text_layers = StringVar()


        #input parameters
        label_bw = Label(self, text="Bandwidht (MHz):")
        self.text_bw = ttk.Combobox(self, values=[5,10,15,20,25,30,40,50,60,70,80,90,100,200,400])
        label_bw.grid(row=1, column=2)
        self.text_bw.grid(row=1, column=3)

        label_SC = Label(self, text="Spacing carries µ(kHz):")
        self.text_SC = ttk.Combobox(self, values=[15,30,60,120])
        label_SC.grid(row=1, column=7)
        self.text_SC.grid(row=1, column=8)

        label_layers = Label(self, text="Max MIMO Layers: ")
        self.text_layers = ttk.Combobox(self, values=["2x2", "4x4", "8x8"])
        label_layers.grid(row=1, column=5)
        self.text_layers.grid(row=1, column=6)

        label_modulation = Label(self, text="Q(j) modulation order:")
        self.text_modulation = ttk.Combobox(self, values=[2,4,6,8])
        label_modulation.grid(row=3, column=0)
        self.text_modulation.grid(row=3, column=1)

        label_Frame = Label(self, text="Frequency Range:")
        self.text_frame = ttk.Combobox(self, values=[1,2])
        label_Frame.grid(row=3, column=5)
        self.text_frame.grid(row=3, column=6)

        label_scaling_factor = Label(self, text="Scaling Factor:")
        self.text_scaling_factor = ttk.Combobox(self, values=[1, 0.8, 0.75, 0.4])
        label_scaling_factor.grid(row=3, column=7)
        self.text_scaling_factor.grid(row=3, column=8)

        label_carries = Label(self, text="aggregated carriers: ")
        self.text_carries = Spinbox(self, values=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16))
        label_carries.grid(row=3, column=2)
        self.text_carries.grid(row=3, column=3)

        label_DD = Label(self, text="Direction data:")
        self.text_DD = ttk.Combobox(self, values=["Downlink", "Uplink"])
        label_DD.grid(row=1, column=0)
        self.text_DD.grid(row=1, column=1)


        label_input = Label(self, text="INPUT DATA", font="Arial 16")
        label_input.grid(row=0, column=4)

        label_ = Label(self, text="")
        label_.grid(row=2, column=4)

        label_output = Label(self, text="OUTPUT DATA", font="Arial 16")
        label_output2 = Label(self, text="INPUT DATA", font="Arial 16")
        label_output.grid(row=4, column=4)
        label_output2.grid(row=0, column=4)


        #output labels
        label_throughput = Label(self, 
            textvariable = self.result,
            font="Arial 12")

        label_numerology = Label(self, 
            textvariable =  self.numerology,
            font="Arial 12")

        label_PRB = Label(self, 
            textvariable = self.PRBs,
            font="Arial 12")

        label_OH = Label(self, 
            textvariable = self.Overhead,
            font="Arial 12")

        label_Log = Label(self, 
            textvariable = self.log,
            font="Arial 12")

        cmd_calculate = Button(self,text="calculate", command=self.calc)
        
        #layout output
        label_throughput.grid(row=5, column=4)
        label_numerology.grid(row=6, column=4)
        label_PRB.grid(row=7, column=4)
        label_OH.grid(row=8, column=4)
        label_Log.grid(row=9, column=4)

        cmd_calculate.grid(row=10, column=4)

    def calc(self):
        DD = self.text_DD.get()
        FR = int(self.text_frame.get())
        BW = int(self.text_bw.get())
        J = int(self.text_carries.get())
        Q = int(self.text_modulation.get())
        f = float(self.text_scaling_factor.get())
        SC = int(self.text_SC.get())
        v = (self.text_layers.get())
        v = int(v[0])

        #condicoes para os logs de saida
        if DD == "Uplink" and v==8: self.log.set("Warning: Numer of maximum MIMO layers for uplink is 4x4!!!")
        elif FR==2 and BW<50:self.log.set("Bandwidht value d'ont correspond to FR2")
        elif FR==1 and BW>100:self.log.set("Bandwidht value d'ont correspond to FR1")
        elif BW>50 and SC==15: self.log.set("Nrb was set to N/A!!!")
        else: self.log.set("")

        column = str(BW) + 'MHz'
        #condicoes para definir a numerologia
        #condicoes para definir o numero de prbs
        if FR == 1: 
            T = pd.read_table('table.txt', delimiter=',')
            if SC ==60: row = 2
            else: row = int((SC/15) - 1)
            RB = T.iloc[row][column]
            mi = row
        else: 
            T = pd.read_table('table2.txt', delimiter=',')
            row = int((SC/60)-1)
            RB = T.iloc[row][column]
            mi = row + 3

        #condicoes para definir o overhead
        if FR == 1 and DD=='Downlink':   OH = 0.14
        elif FR == 2 and DD=='Downlink': OH = 0.18
        elif FR == 1 and DD=='Uplink': OH = 0.08
        elif FR == 2 and DD=='Uplink': OH = 0.1

        i = 0
        Th = 0
        while(i < J):
            Th += v * Q * f * (948/1024) * ((RB * 12)*(14*(2**mi)/(10**-3)))*(1-OH) #equacao geral do throughput
            i+=1
        Th = round(Th * 10**-6,2)
        
        #MHz to GHz
        if Th > 1024: Th = str((round(Th/1024,2))) + "Gbps"
        else: Th = str(Th) + "Mbps"

        #variaveis de saida
        self.numerology.set("Numerology: " + str(mi))
        self.PRBs.set("Num of PRBs: " + str(RB))
        self.Overhead.set("Overhead: " + str(OH))
        self.result.set("Troughput: " + Th )
