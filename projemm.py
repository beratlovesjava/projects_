import tkinter as tk
import psutil

window = tk.Tk()
window.geometry("200x200")
window.title("Computer Statistics board")
window.configure(background='Green')


ram1 = psutil.virtual_memory()
cpu1 = psutil.cpu_percent()



ram = tk.Label(
    window,
    fg="Black",
    bg="Green",
    text=f"RAM: {ram1.percent}%",
)
ram.pack()

def update():
    ram1 = psutil.virtual_memory()
    ram.config(text=f"Ram usage: {ram1.percent}%")
    window.after(1000, update)

cpu = tk.Label(
    window,
    fg="Black",
    bg="Green",
    text=f"CPU: {cpu1}%",
)
cpu.pack()
def cpu_update():
    cpu1 = psutil.virtual_memory()
    ram.config(text=f"CPU usage: {cpu1.percent}%")
    window.after(1000,cpu_update)


update()


window.mainloop()
