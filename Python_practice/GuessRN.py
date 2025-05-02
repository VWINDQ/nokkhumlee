import tkinter as tk
import random


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#print(random.choice(list1))

def guess():
    num = int(number_input.get())
    if num == 0:
        result_label.config(text="กรุณาใส่ตัวเลขที่ไม่เป็น 0")
        return

    if num == random.choice(list1):
        result_label.configure(text="ถูกต้อง", bg="lightgreen")
        window.configure(bg='lightgreen')
        
    else:
        result_label.configure(text="ผิด", bg="red")
        window.configure(bg='red')
        

window = tk.Tk()
window.title("Guess the number")
window.minsize(400, 400)

title = tk.Label(master=window, text="Guess the number form 1 to 20")
title.pack(pady=20)

number_input = tk.Entry(master=window, width=20)
number_input.pack()

ok_button = tk.Button(master=window, text="Guess", command=guess, bg="green", fg="white")
ok_button.pack(pady=15)

result_label = tk.Label(master=window, text="")
result_label.pack(pady=15)

window.mainloop()