import tkinter as tk
from tkinter import messagebox
import requests
import json

options = ["bypasser.online", "bypasser.link", "thebypasser.com"]

def dark_mode(root):
    root.config(bg='#303030')

def on_select(value):
    if value == "bypasser.online":
        url = input_url.get()
        url = "https://bypass.pm/bypass2?url=" + url
        response = requests.get(url)
        json_response = json.loads(response.text)
        destination = json_response["destination"]
        output_label.config(text=destination)
    elif value == "bypasser.link":
        url = input_url.get()
        url = "https://bypass.bot.nu/bypass2?url=" + url
        response = requests.get(url)
        json_response = json.loads(response.text)
        destination = json_response["destination"]
        output_label.config(text=destination)
    elif value == "thebypasser.com":
        url = input_url.get()
        url = "https://bypass.pm/bypass2?url=" + url
        response = requests.get(url)
        json_response = json.loads(response.text)
        destination = json_response["destination"]
        output_label.config(text=destination)
    else:
        messagebox.showerror("Error", "Geçersiz Seçim. Lütfen tekrar deneyiniz.")

def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_label.cget("text"))
    messagebox.showinfo("Success", "Yazı kopyalandı!")

root = tk.Tk()
root.geometry("450x200+450+250")
root.title("Twix URL Bypasser")

dark_mode(root)

label = tk.Label(root, text="Bypass Methodunu Seçiniz:", font=("Helvetica", 12), bg='#303030', fg='white')
label.pack()

var = tk.StringVar(value=options[0])
dropdown = tk.OptionMenu(root, var, *options, command=lambda value: on_select(value))
dropdown.config(bg='#303030', fg='white', activebackground='#303030', activeforeground='white')
dropdown.pack()

input_url = tk.Entry(root, bg='#404040', fg='white')
input_url.pack()

output_label = tk.Label(root, text="", font=("Helvetica", 12), bg='#303030', fg='white')
output_label.pack()

copy_button = tk.Button(root, text="Kopyala", font=("Helvetica", 12), bg='#404040', fg='white', command=copy_text)
copy_button.pack()

label2 = tk.Label(root, text="linki yapıştırdıktan sonra bypass yöntemini seçiniz", font=("ArialBold", 7), bg='#303030', fg='white')
label2.pack()

root.mainloop()