import tkinter as tk
from tkinter import ttk, messagebox


def hesapla():
    try:
        resolution = resolution_var.get()
        duration = int(duration_var.get())

        # Bit hızlarını çözünürlüğe göre ayarlama (kbps)
        bit_rates = {
            "360p": 750,
            "480p": 1500,
            "720p": 3000,
            "1080p": 4500,
        }
        bit_rate = bit_rates[resolution]

        # Dosya boyutunu hesaplama (MB cinsinden)
        file_size_mb = bit_rate * duration * 60 / 8 / 1024
        result_label.config(text=f"Video Boyutu: {file_size_mb:.2f} MB")

    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir süre giriniz!")
    except KeyError:
        messagebox.showerror("Hata", "Geçerli bir çözünürlük seçiniz!")


# Tkinter arayüzü
root = tk.Tk()
root.title("Video Veri Kullanımı Hesaplayıcısı")
root.geometry("400x300")
root.resizable(False, False)  # Boyut değişimini engelle


# Stil ayarları
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TCombobox", font=("Helvetica", 12))
style.map(
    "TButton",
    foreground=[('active', 'black'), ('!disabled', 'blue')],
    background=[('active', 'lightgreen'), ('!disabled', 'green')]
)

# Çözünürlük seçimi
resolution_label = ttk.Label(root, text="Çözünürlük:")
resolution_label.pack(pady=10)

resolution_var = tk.StringVar()
resolution_combobox = ttk.Combobox(
    root, textvariable=resolution_var, state='readonly')
resolution_combobox['values'] = ("360p", "480p", "720p", "1080p")
resolution_combobox.current(0)
resolution_combobox.pack(pady=10)

# Süre girişi
duration_label = ttk.Label(root, text="Video Süresi (Dakika):")
duration_label.pack(pady=10)

duration_var = tk.StringVar()
duration_entry = ttk.Entry(root, textvariable=duration_var)
duration_entry.pack(pady=10)

# Hesapla butonu
calculate_button = ttk.Button(root, text="Hesapla", command=hesapla)
calculate_button.pack(pady=20)

# Sonuç etiketi
result_label = ttk.Label(root, text="Video Boyutu: ")
result_label.pack(pady=20)

# Uygulamayı çalıştır
root.mainloop()
