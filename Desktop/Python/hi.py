import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Title", "Selamat Datang Dihalaman Beranda Saya ")

root = tk.Tk()
root.title("Dialog Ade Muhamad Rivaldi")

root.geometry ("400x200")

button = tk.Button(root, text="Klik Disini", command=show_message)
button.pack(pady=20)

root.mainloop()
