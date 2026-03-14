#!/data/data/com.termux/files/usr/bin/python3
# XDIZ SPM-CHAT V.1 - WhatsApp Spammer
# Created by dika projects (@_dizofficial)

import os
import sys
import time
import random
import subprocess
from datetime import datetime

PIN_BENAR = "2011"
VERSION = "V.1"
AUTHOR = "dika projects"
TIKTOK = "_dizofficial"

ASCII_ART = '''
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║    ██╗  ██╗██████╗ ██╗███████╗    ███████╗██████╗ ███╗   ███╗
║    ╚██╗██╔╝██╔══██╗██║╚══███╔╝    ██╔════╝██╔══██╗████╗ ████║
║     ╚███╔╝ ██║  ██║██║  ███╔╝     ███████╗██████╔╝██╔████╔██║
║     ██╔██╗ ██║  ██║██║ ███╔╝      ╚════██║██╔═══╝ ██║╚██╔╝██║
║    ██╔╝ ██╗██████╔╝██║███████╗    ███████║██║     ██║ ╚═╝ ██║
║    ╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝    ╚══════╝╚═╝     ╚═╝     ╚═╝
║                                                          ║
║              ┌──────────────────────────┐               ║
║              │   XDIZ SPM-CHAT V.1      │               ║
║              │  Created by dika projects │               ║
║              │    TikTok: @_dizofficial  │               ║
║              └──────────────────────────┘               ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                   [ LOGIN DASHBOARD ]                    ║
╚══════════════════════════════════════════════════════════╝
'''

def clear_screen():
    os.system('clear')

def print_header():
    print("=" * 60)
    print(ASCII_ART)
    print("=" * 60)
    print(f"{'XDIZ SPM-CHAT ' + VERSION:^60}")
    print(f"{'Created by ' + AUTHOR + ' (@' + TIKTOK + ')':^60}")
    print("=" * 60)

def login():
    clear_screen()
    print_header()
    try:
        pin = input("\n[!] Masukkan PIN untuk mengakses tools: ")
        if pin == PIN_BENAR:
            print("\n[✓] PIN benar! Mengakses tools...")
            time.sleep(1)
            return True
        else:
            print("\n[✗] PIN salah! Akses ditolak.")
            time.sleep(2)
            return False
    except KeyboardInterrupt:
        print("\n\n[!] Program dihentikan.")
        sys.exit(0)

def validate_phone(number):
    number = number.strip().replace(" ", "").replace("-", "")
    if number.startswith("+"):
        number = number[1:]
    if len(number) < 10 or len(number) > 15:
        return False, None
    if not number.isdigit():
        return False, None
    if not number.startswith("628"):
        if number.startswith("08"):
            number = "62" + number[1:]
        else:
            return False, None
    return True, number

def spam_whatsapp(phone, message, count, delay):
    print(f"\n[!] Memulai spam ke {phone}")
    print(f"[!] Pesan: {message[:30]}..." if len(message) > 30 else f"[!] Pesan: {message}")
    print(f"[!] Jumlah: {count if count > 0 else '∞ (infinite)'}")
    print(f"[!] Delay: {delay} detik")
    print("-" * 50)
    sent = 0
    try:
        while True:
            if count > 0 and sent >= count:
                break
            cmd = f'am start -a android.intent.action.VIEW -d "https://wa.me/{phone}?text={message}"'
            subprocess.run(cmd, shell=True, capture_output=True, text=True)
            sent += 1
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Pesan ke-{sent} dikirim")
            time.sleep(delay)
    except KeyboardInterrupt:
        print(f"\n\n[!] Spam dihentikan. Total terkirim: {sent}")
    except Exception as e:
        print(f"\n[✗] Error: {e}")
    return sent

def main():
    if not login():
        return
    clear_screen()
    print_header()
    
    default_messages = [
        "Halo, ada yang bisa dibantu?",
        "Test chat dari XDIZ SPM-CHAT",
        "Maaf, ini cuma tes doang",
        "Jangan lupa bahagia hari ini",
        "Semoga harimu menyenangkan",
        "Ini pesan otomatis, gak usah dibales",
        "Cuma mau bilang hai",
        "Testing 1 2 3",
        "Halo, apa kabar?",
        "Gw cuma iseng doang"
    ]
    
    while True:
        print("\n" + "=" * 50)
        print("MENU UTAMA XDIZ SPM-CHAT")
        print("=" * 50)
        print("1. Spam dengan pesan custom")
        print("2. Spam dengan pesan random")
        print("3. Lihat daftar pesan default")
        print("4. Keluar")
        print("-" * 50)
        
        try:
            choice = input("Pilih menu (1-4): ").strip()
            
            if choice == "4":
                print("\n[!] Terima kasih telah menggunakan XDIZ SPM-CHAT")
                print("[!] Created by dika projects (@_dizofficial)")
                break
            
            if choice not in ["1", "2", "3"]:
                print("[✗] Pilihan tidak valid!")
                continue
            
            if choice == "3":
                print("\n" + "=" * 50)
                print("DAFTAR PESAN DEFAULT:")
                print("=" * 50)
                for i, msg in enumerate(default_messages, 1):
                    print(f"{i}. {msg}")
                input("\nTekan Enter untuk kembali...")
                continue
            
            while True:
                phone = input("\nMasukkan nomor target (628xx): ").strip()
                valid, formatted_phone = validate_phone(phone)
                if valid:
                    break
                print("[✗] Format nomor salah! Harus 628xxx")
            
            message = ""
            if choice == "1":
                message = input("Masukkan pesan yang akan dikirim: ").strip()
                if not message:
                    print("[!] Pesan kosong, pakai default")
                    message = random.choice(default_messages)
            elif choice == "2":
                message = random.choice(default_messages)
                print(f"[!] Pesan random: {message}")
            
            while True:
                try:
                    count_input = input("Masukkan jumlah spam (0 untuk infinite): ").strip()
                    count = int(count_input)
                    if count >= 0:
                        break
                    else:
                        print("[✗] Jumlah harus >= 0!")
                except ValueError:
                    print("[✗] Masukkan angka!")
            
            while True:
                try:
                    delay = float(input("Masukkan delay antar chat (detik, contoh: 2): ").strip())
                    if delay > 0:
                        break
                    else:
                        print("[✗] Delay harus > 0!")
                except ValueError:
                    print("[✗] Masukkan angka!")
            
            print("\n" + "=" * 50)
            print("KONFIRMASI SPAM:")
            print("=" * 50)
            print(f"Nomor target: {formatted_phone}")
            print(f"Pesan: {message}")
            print(f"Jumlah: {count if count > 0 else '∞ (infinite)'}")
            print(f"Delay: {delay} detik")
            print("-" * 50)
            
            confirm = input("Lanjutkan spam? (y/n): ").strip().lower()
            if confirm == 'y':
                total = spam_whatsapp(formatted_phone, message, count, delay)
                print(f"\n[✓] Spam selesai! Total terkirim: {total}")
            else:
                print("\n[!] Spam dibatalkan.")
            
        except KeyboardInterrupt:
            print("\n\n[!] Program dihentikan.")
            break
        except Exception as e:
            print(f"\n[✗] Error: {e}")
    
    print("\n" + "=" * 50)
    print("Terima kasih telah menggunakan XDIZ SPM-CHAT")
    print("Follow TikTok: @_dizofficial")
    print("=" * 50)

if __name__ == "__main__":
    main()
