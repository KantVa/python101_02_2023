import tkinter as tk
import random
from tkinter import messagebox

def random_food():
    foods = ["สุกี้น้ำหมู","สุกี้น้ำทะเล","ผัดไทกุ้งสด","ผัดไทกุ้งสดห่อไข่","ข้าวผัดกระเพราหมูกรอบ","ข้าวผัดกระเพราหมูสับ","ข้าวผัดกระเพราไก่สับ","ข้าวผัดน้ำพริกลงเรือ","ข้าวราดผัดพริกแกงกุ้ง","ข้าวหมูกระเทียม","สปาเก็ตตี้ผัดพริกแห้ง",
    "ข้าวกะเพราหมูชิ้นไข่ดาว","ข้าวผัดต้มยำทะเล","ข้าวผัดหมู","ยำมาม่า ทะเล","มาม่าผัดต้มยำ กุ้งสับ","สุกี้แห้ง","ข้าวต้มหมูสับ","ข้าวต้มกุ้งสับ","ข้าวผัดแกงเขียวหวาน"]
    food = random.choice(foods)
    text = "เมนูที่สุ่มได้คือ " + food
    label1.config(text=text)

GUI = tk.Tk()
GUI.geometry ("500x500" )
GUI.title("สุ่มเมนูอาหาร")

label0 = tk.Label(GUI, text="กินอะไรกันดี", font=("TkDefaultFont", 20))
label0.place(relx=0.5, rely=0.3,anchor="center")

label1 = tk.Label(GUI, text="สุ่มเมนูอาหาร", font=("TkDefaultFont", 20))
label1.place(relx=0.5, rely=0.4,anchor="center")

button = tk.Button(GUI, text="Generate", command=random_food)
button.place(relx=0.5, rely=0.5, anchor="center")

GUI.mainloop()