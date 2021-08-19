from tkinter import Tk
from calc_class import calculadora


root = Tk()
root.title("Calculadora de Throughput do NR")

frame_calc = calculadora(root)
frame_calc.grid()

root.mainloop()
