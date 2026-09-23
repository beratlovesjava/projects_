import tkinter as tk
import socket

window = tk.Tk()
window.title("port_checker")
window.geometry("400x300")
window.config(bg="Green")


ip_get = tk.Entry(
    window,
    bg='black',
    fg='white',
    font=("Arial", 12),
    width=20,
)
ip_get.pack(pady=(60, 5))


port_get = tk.Entry(
    window,
    bg='black',
    fg='white',
    font=("Arial", 12),
    width=20,
)
port_get.pack(pady=(5, 30))


def check_port():
    ip = ip_get.get()
    ports = port_get.get().split(",")

    results = []

    for port in ports:
        port = int(port.strip())

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result_code = sock.connect_ex((ip, port))

        if result_code == 0:
            results.append(f"Port {port} OPEN")
        else:
            results.append(f"Port {port} CLOSED")

        sock.close()

    result.config(text="\n".join(results))

button = tk.Button(
    window,
    text="Check Port",
    command=check_port
)
button.pack()


result = tk.Label(
    window,
    text="",
    bg="Green",
    fg="white",
    font=("Arial", 12)
)
result.pack(pady=30)


window.mainloop()