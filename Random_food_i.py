import tkinter as tk
import random
import csv
from tkinter import messagebox
import datetime

def random_food():
    foods = ['Tom Yum Goong', 'Pad Thai', 'Green Curry', 'Massaman Curry',
             'Som Tam', 'Khao Soi', 'Larb', 'Tom Kha Gai', 'Pad Krapow Moo Saap', 'Moo Ping']
    food = random.choice(foods)
    text = "Menu Today: " + food
    label1.config(text=text)
    with open("Food_Random.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([food, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

def show_history():
    history_listbox.delete(0, tk.END)
    with open("Food_Random.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            history_listbox.insert(tk.END, f"{row[0]} ({row[1]})")
    history_listbox.after(5000, show_history)

def delete_history():
    selected_item = history_listbox.get(history_listbox.curselection())
    food, time = selected_item.split(" (")
    food = food.strip()
    time = time[:-1]

    
    with open("Food_Random.csv", "r") as file:
        data = list(csv.reader(file))
    with open("Food_Random.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for row in data:
            if row[0] != food or row[1] != time:
                writer.writerow(row)
    show_history()

def clear_history():
    with open("Food_Random.csv", "w", newline="") as file:
        writer = csv.writer(file)
        show_history()

GUI = tk.Tk()
GUI.geometry ("500x500" )
GUI.title("Food random")

label0 = tk.Label(GUI, text="วันนี้จะกินอะไรดีละ ?", font=("TkDefaultFont", 20))
label0.place(relx=0.5, rely=0.1, anchor="center")

label1 = tk.Label(GUI, text="สุ่มเมนูอาหาร", font=("TkDefaultFont", 20))
label1.place(relx=0.5, rely=0.15, anchor="center")

button = tk.Button(GUI, text="กดเพื่อสุ่ม", command=random_food)
button.place(relx=0.5, rely=0.22, anchor="center")

history_label = tk.Label(GUI, text="ประวัติเมนู", font=("TkDefaultFont", 20))
history_label.place(relx=0.3, rely=0.3, anchor="center")

history_listbox = tk.Listbox(GUI)
history_listbox.place(relx=0.3, rely=0.54, anchor="center", width=250, height=200)

show_history_button = tk.Button(GUI, text="กดเพื่อดูประวัติ", command=show_history)
show_history_button.place(relx=0.7, rely=0.4, anchor="center")

delete_button = tk.Button(GUI, text="ลบรายการ", command=delete_history)
delete_button.place(relx=0.7, rely=0.52, anchor="center")

clear_button = tk.Button(GUI, text="ล้างประวัติ", command=clear_history)
clear_button.place(relx=0.7, rely=0.58, anchor="center")

GUI.mainloop()