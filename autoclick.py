import pyautogui
import time

# Daftar koordinat yang ingin diklik
coordinates = [
    (500, 300),
    (600, 400),
    (700, 500),
   c # Tambahkan koordinat lainnya sesuai kebutuhan
]

def auto_click(x, y):
    try:
        pyautogui.click(x, y)
        print(f"Clicked at ({x}, {y})")
    except Exception as e:
        print(f"Error: {str(e)}")

# Auto klik setiap 1 detik untuk setiap koordinat dalam daftar
while True:
    for coord in coordinates:
        auto_click(coord[0], coord[1])
        time.sleep(0.1)  # Jeda setiap klik, sesuaikan jika diperlukan
