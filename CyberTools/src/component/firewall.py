import os

def firewall_hello():
    print("""
    1 - UFW Durumunu Görüntüle
    2 - UFW'u Etkinleştir
    3 - UFW'u Devre Dışı Bırak
    4 - Yeni Kural Ekle
    """)
    secim = input("Seçiminizi yapınız: ")

    if secim == "1":
        os.system("ufw status")
    elif secim == "2":
        os.system("ufw enable")
    elif secim == "3":
        os.system("ufw disable")
    elif secim == "4":
        kural = input("Eklemek istediğiniz kuralı giriniz (örnek: allow 22): ")
        os.system(f"ufw {kural}")
    else:
        print("Geçersiz seçim! Ana menüye dönülüyor...")
