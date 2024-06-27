from tkinter import *

my_window = Tk()
my_window.title("Vücut Kitle İndeksi Hesaplayıcı")
my_window.minsize(width=300, height=300)

my_weight_label = Label(text="Ağırlığınızı giriniz (kg)")
my_weight_label.config(padx=10, pady=10)
my_weight_label.pack()

my_weight_entry = Entry(width=20)
my_weight_entry.pack()

my_height_label = Label(text="Boyunuzu giriniz (cm)")
my_height_label.config(padx=10, pady=10)
my_height_label.pack()

my_height_entry = Entry(width=20)
my_height_entry.pack()

my_calculate_button = Button(text="Hesapla")
my_calculate_button.pack(pady=20)

my_window.mainloop()