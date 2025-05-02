import tkinter as tk

window = tk.Tk()
window.title("Temperature Converter")
window.minsize(400, 400)

def convert():
    celsius = float(celsius_input.get())
    fahrenheit = (celsius * 9/5) + 32
    result_label.configure(text=f"{celsius}°C = {fahrenheit:.2f}°F")
    result_label.pack(pady=15)
    

title = tk.Label(master=window, text="Temperature Converter")
title.pack(pady=20)

celsius_input = tk.Entry(master=window, width=20)
celsius_input.pack()

convert_button = tk.Button(master=window, text="convert", command=convert)
convert_button.pack(pady=15)

result_label = tk.Label(master=window, text="")
result_label.pack(pady=15)


window.mainloop()