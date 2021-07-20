from tkinter import *
from tkinter import ttk
import pandas as pd

def calcTputNR():

    DD = text_DD.get()
    FR = int(text_frame.get())
    BW = int(text_bw.get())
    J = int(text_carries.get())
    Q = int(text_modulation.get())
    f = float(text_scaling_factor.get())
    SC = int(text_SC.get())
    v = (text_layers.get())
    v = int(v[0])

    #condicoes para os logs de saida
    if DD == "Uplink" and v==8: Log.set("Warning: Numer of maximum MIMO layers for uplink is 4x4!!!")
    elif FR==2 and BW<50:Log.set("Bandwidht value d'ont correspond to FR2")
    elif FR==1 and BW>100:Log.set("Bandwidht value d'ont correspond to FR1")
    elif BW>50 and SC==15: Log.set("Nrb was set to N/A!!!")
    else: Log.set("")

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
    numerology.set("Numerology: " + str(mi))
    PRBs.set("Num of PRBs: " + str(RB))
    Overhead.set("Overhead: " + str(OH))
    result.set("Troughput: " + Th )

#Atribuicao das variaveis
root = Tk()
root.title("Calculadora de Throughput do NR")
frame_calcNR = Frame(root)
result = StringVar()
numerology = StringVar()
PRBs = StringVar()
Log = StringVar()
Overhead = StringVar()
text_DD = StringVar()
text_DD.set("Downlink")
teste = text_DD.get()

#definicao dos labels
label_bw = Label(frame_calcNR, text="Bandwidht (MHz):")
label_SC = Label(frame_calcNR, text="Spacing carries µ(kHz):")
label_layers = Label(frame_calcNR, text="Max MIMO Layers: ")
label_modulation = Label(frame_calcNR, text="Q(j) modulation order:")
label_Frame = Label(frame_calcNR, text="Frequency Range:")
label_scaling_factor = Label(frame_calcNR, text="Scaling Factor:")
label_carries = Label(frame_calcNR, text="aggregated carriers: ")
label_DD = Label(frame_calcNR, text="Direction data:")
label_input = Label(frame_calcNR, text="INPUT DATA", font="Arial 16")
label_ = Label(frame_calcNR, text="")
label_output = Label(frame_calcNR, text="OUTPUT DATA", font="Arial 16")


#output labels
label_throughput = Label(root, 
    textvariable = result,
    font="Arial 12")

label_numerology = Label(root, 
    textvariable =  numerology,
    font="Arial 12")

label_PRB = Label(root, 
    textvariable = PRBs,
    font="Arial 12")

label_OH = Label(root, 
    textvariable = Overhead,
    font="Arial 12")

label_Log = Label(root, 
    textvariable = Log,
    font="Arial 12")

#input parameters
text_bw = ttk.Combobox(frame_calcNR, values=[5,10,15,20,25,30,40,50,60,70,80,90,100,200,400])
text_SC = ttk.Combobox(frame_calcNR, values=[15,30,60,120])
text_layers = ttk.Combobox(frame_calcNR, values=["2x2", "4x4", "8x8"])
text_modulation = ttk.Combobox(frame_calcNR, values=[2,4,6,8])
text_scaling_factor = ttk.Combobox(frame_calcNR, values=[1, 0.8, 0.75, 0.4])
text_carries = Spinbox(frame_calcNR, values=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16))
text_DD = ttk.Combobox(frame_calcNR, values=["Downlink", "Uplink"])
text_frame = ttk.Combobox(frame_calcNR, values=[1,2])

# ------------------------------------------------------------------------------------------
# layout
label_input.grid(row=0, column=4)
label_DD.grid(row=1, column=0)
text_DD.grid(row=1, column=1)
label_modulation.grid(row=3, column=0)
text_modulation.grid(row=3, column=1)
label_bw.grid(row=1, column=2)
text_bw.grid(row=1, column=3)
label_carries.grid(row=3, column=2)
text_carries.grid(row=3, column=3)
label_.grid(row=2, column=4)
label_layers.grid(row=1, column=5)
text_layers.grid(row=1, column=6)
label_Frame.grid(row=3, column=5)
text_frame.grid(row=3, column=6)
label_SC.grid(row=1, column=7)
text_SC.grid(row=1, column=8)
label_scaling_factor.grid(row=3, column=7)
text_scaling_factor.grid(row=3, column=8)
label_output.grid(row=4, column=4)

frame_calcNR.grid()

cmd_calculate = Button(root, text="Calculate", command=calcTputNR)

#layout output
label_throughput.grid()
label_numerology.grid()
label_PRB.grid()
label_OH.grid()
label_Log.grid()

cmd_calculate.grid()

root.mainloop()