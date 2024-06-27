from tkinter import *

my_window = Tk()
my_window.title("Vücut Kitle İndeksi Hesaplayıcı")
my_window.minsize(width=300, height=250)

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

def calculate_bmi():
    try:
        weight = float(my_weight_entry.get())
        height = float(my_height_entry.get()) / 100
        if 500 > weight > 0 and 500 > height > 0:
            bmi = weight / (height ** 2)
            if bmi < 18.5:
                my_result_label.config(text=f"Vücut kitle indeksiniz {bmi:.2f} olup zayıfsınız." )
            elif 25 > bmi >= 18.5:
                my_result_label.config(text=f"Vücut kitle indeksiniz {bmi:.2f} olup normal kilodasınız.")
            elif 30 > bmi >= 25:
                my_result_label.config(text=f"Vücut kitle indeksiniz {bmi:.2f} olup fazla kilolusunuz.")
            elif bmi >= 30:
                my_result_label.config(text=f"Vücut kitle indeksiniz {bmi:.2f} olup obezsiniz.")
        else:
            my_result_label.config(text="Lütfen geçerli bir değer giriniz")
    except ValueError:
        my_result_label.config(text="Lütfen geçerli bir değer giriniz")

my_calculate_button = Button(text="Hesapla", command=calculate_bmi)
my_calculate_button.pack(pady=20)

my_result_label = Label(text="")
my_result_label.pack()

my_window.mainloop()