import socket
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from concurrent.futures import ThreadPoolExecutor


# Lista de puertos comunes
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 3389, 8080, 8443]

# Función para validar una IP
def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

# Función para escanear un puerto específico
def scan_port(ip, port, output_box, progress_var, total_ports):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Desconocido"
            output_box.insert(tk.END, f"[+] Puerto {port} ABIERTO - Servicio: {service}\n", "open")
            output_box.see(tk.END)
        sock.close()
    except Exception as e:
        pass

    # Actualizar progreso
    progress_var.set(progress_var.get() + 1)

# Función para realizar el escaneo
def perform_scan(ip, ports, output_box, progress_bar, status_label):
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, f"Escaneando {ip}...\n", "info")
    output_box.tag_config("open", foreground="green")
    output_box.tag_config("info", foreground="blue")

    status_label.config(text="Escaneando...", foreground="orange")
    progress_bar["value"] = 0
    total_ports = len(ports)
    progress_var = tk.IntVar(value=0)

    # Función que se ejecutará en segundo plano
    def threaded_scan():
        with ThreadPoolExecutor(max_workers=100) as executor:
            for port in ports:
                executor.submit(scan_port, ip, port, output_box, progress_var, total_ports)
        status_label.config(text="Escaneo completado.", foreground="green")
        output_box.insert(tk.END, "\n[+] Escaneo completado.\n", "info")

    # Lanzar el escaneo en un hilo separado
    threading.Thread(target=threaded_scan, daemon=True).start()

# Función principal para iniciar el escaneo con rango de puertos
def start_scan(ip_entry, start_port_entry, end_port_entry, output_box, progress_bar, status_label):
    ip = ip_entry.get()
    if not is_valid_ip(ip):
        messagebox.showerror("Error", "Introduce una dirección IP válida.")
        return

    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError
        ports = range(start_port, end_port + 1)
        perform_scan(ip, ports, output_box, progress_bar, status_label)
    except ValueError:
        messagebox.showerror("Error", "Introduce un rango de puertos válido (1-65535).")

# Función para escanear puertos comunes
def scan_common_ports(ip_entry, output_box, progress_bar, status_label):
    ip = ip_entry.get()
    if not is_valid_ip(ip):
        messagebox.showerror("Error", "Introduce una dirección IP válida.")
        return
    perform_scan(ip, COMMON_PORTS, output_box, progress_bar, status_label)

# Función para crear la interfaz gráfica
def create_gui():
    window = tk.Tk()
    window.title("Port Scanner by vFo")
    window.geometry("600x500")
    window.configure(bg="black")

    # Etiquetas y entradas
    tk.Label(window, text="Dirección IP:", fg="green", bg="black").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    ip_entry = tk.Entry(window, width=30, bg="black", fg="green", insertbackground="green")
    ip_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    tk.Label(window, text="Puerto inicial:", fg="green", bg="black").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    start_port_entry = tk.Entry(window, width=10, bg="black", fg="green", insertbackground="green")
    start_port_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    tk.Label(window, text="Puerto final:", fg="green", bg="black").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    end_port_entry = tk.Entry(window, width=10, bg="black", fg="green", insertbackground="green")
    end_port_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Botones
    start_button = tk.Button(window, text="Escanear Rango", bg="red", fg="white", 
                             command=lambda: start_scan(ip_entry, start_port_entry, end_port_entry, output_box, progress_bar, status_label))
    start_button.grid(row=3, column=0, padx=10, pady=10)

    common_button = tk.Button(window, text="Escanear Puertos Comunes", bg="red", fg="white", 
                              command=lambda: scan_common_ports(ip_entry, output_box, progress_bar, status_label))
    common_button.grid(row=3, column=1, padx=10, pady=10)

    # Área de salida
    output_box = scrolledtext.ScrolledText(window, width=80, height=20, bg="white", fg="green", insertbackground="green",setgrid="0")
    output_box.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    
    # Cambiar el color de la barra de progreso
    style = ttk.Style()
    style.theme_use('default')
    style.configure("red.Horizontal.TProgressbar", troughcolor='white', background='red')


   

    # Barra de progreso
    progress_bar = ttk.Progressbar(window, orient="horizontal", length=600, mode="determinate", style="red.Horizontal.TProgressbar")
    progress_bar.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    # Etiqueta de estado
    status_label = tk.Label(window, text="Listo", font=("Arial", 10, "bold"), fg="green", bg="black")
    status_label.grid(row=6, column=0, columnspan=2, pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
