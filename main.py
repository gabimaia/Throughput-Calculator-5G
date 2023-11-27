from tkinter import Tk
from calc_class import calculadora


root = Tk()
root.title("NR Throughput Calculator")

frame_calc = calculadora(root)
frame_calc.grid()

root.mainloop()
