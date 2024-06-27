from tkinter import *

my_window = Tk()
my_window.title("Vücut Kitle İndeksi Hesaplayıcı")
my_window.minsize(width=300, height=300)

my_label = Label(text="Ağırlığınızı giriniz (kg)")
my_label.config(padx=20, pady=20)
my_label.pack()

my_window.mainloop()