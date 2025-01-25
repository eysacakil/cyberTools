import os

def mac_degis():
    interface = input("Hedef ağ arayüzünü giriniz (örnek: wlan0): ")

    print("""
    1 - Rastgele bir MAC adresi ata
    2 - Varsayılan MAC adresine dön
    """)
    secim = input("Seçiminizi yapınız: ")

    if secim == "1":
        os.system(f"macchanger -r {interface}")
    elif secim == "2":
        os.system(f"macchanger -p {interface}")
    else:
        print("Geçersiz seçim! Ana menüye dönülüyor...")
