import tkinter as tk

def sum():
    num = int(number_input.get())
    if num == 0:
        result_label.config(text="กรุณาใส่ตัวเลขที่ไม่เป็น 0")
        return

    result = ""
    for i in range(1, 13):
        result += f"{num} x {i} = {num * i}\n"
    result_label.configure(text=result)
        

window = tk.Tk()
window.title("สูตรคูณ")
window.minsize(400, 400)

result_label = tk.Label(master=window, text="")
result_label.pack(pady=15)

title = tk.Label(master=window, text="สูตรคูณแม่")
title.pack(pady=20)

number_input = tk.Entry(master=window, width=20)
number_input.pack()

ok_button = tk.Button(master=window, text="ได้แก่", command=sum, bg="green", fg="white"
                      , width=15)
ok_button.pack()


window.mainloop()