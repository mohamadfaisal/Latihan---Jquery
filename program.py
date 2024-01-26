import os
import subprocess
import pyautogui

def buka_file(nama_file):
    try:
        os.startfile(nama_file)
    except FileNotFoundError:
        print("File tidak ditemukan.")

def buka_browser():
    try:
        subprocess.Popen('C:/Program Files/Internet Explorer/iexplore.exe')
    except FileNotFoundError:
        print("Browser tidak ditemukan.")

def buka_aplikasi(nama_aplikasi):
    try:
        subprocess.Popen(nama_aplikasi)
    except FileNotFoundError:
        print("Aplikasi tidak ditemukan.")

def kirim_pesan_whatsapp(penerima, pesan):
    # Pastikan aplikasi WhatsApp terbuka dan berada pada posisi yang tepat di layar
    posisi_aplikasi = pyautogui.locateOnScreen('whatsapp_icon.png')
    if posisi_aplikasi is None:
        print("Aplikasi WhatsApp tidak ditemukan.")
        return

    pyautogui.click(posisi_aplikasi)
    pyautogui.press('esc')  # Tutup jendela chat sebelumnya (jika ada)
    pyautogui.press('/')
    pyautogui.write(penerima)
    pyautogui.press('enter')

    # Tunggu sampai halaman chat terbuka
    posisi_chat = None
    for _ in range(10):
        posisi_chat = pyautogui.locateOnScreen('chat_window.png')
        if posisi_chat is not None:
            break
        time.sleep(1)

    if posisi_chat is None:
        print("Penerima tidak ditemukan.")
        return

    # Ketik pesan dan kirim
    pyautogui.click(posisi_chat)
    pyautogui.write(pesan)
    pyautogui.press('enter')

# Contoh penggunaan
buka_file("C:/Users/username/Documents/file.txt")
buka_browser()
buka_aplikasi("C:/Program Files/Microsoft Office/Office16/OUTLOOK.EXE")
kirim_pesan_whatsapp("Nama Kontak", "Halo, apa kabar?")
