#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def nmap_hello():
    print("""
    ----------------------
        NMAP
    ----------------------
    0 - Exit
    1 - Açık Port ve Servis Keşfi (-sS)
    2 - Servis ve Versiyon Taraması (-sV -sC)
    3 - Derin Zafiyet Taraması (--script vuln)
    4 - Firewall Tespiti (-sA)
    5 - Web Uygulamaları Tespiti (--script http-enum,http-title)
    6 - Local Ağda ARP Scan (-sP -n)
    7 - Local Ağda ARP Scan Only IP addresses 
    ----------------------
    """)

    ip = input("Enter an IP address: ")

    while True:
        try:
            islem_no = int(input("Select (0-7): "))

            if islem_no == 1:
                print(f"Nmap ile açık port ve servislerin keşfi için tüm portların taraması başlatılıyor... {ip}")
                os.system(f"nmap -sS -p- --min-rate 1000 {ip}")
                break
            elif islem_no == 2:
                print(f"Nmap ile servisler ve versiyonlarının tespiti için tarama başlatılıyor... {ip}")
                os.system(f"nmap -sC -sV -p- --version-all {ip}")
                break
            elif islem_no == 3:
                print(f"NSE zafiyet tarama scriptleri ile derin tarama başlatılıyor... {ip}")
                os.system(f"nmap --script vuln {ip}")
                break
            elif islem_no == 4:
                print(f"Nmap ile firewall IPS IDS tespiti için tarama başlatılıyor... {ip}")
                os.system(f"nmap -sA {ip}")
                break
            elif islem_no == 5:
                print(f"Web sunucusunda çalışan uygulamaların tespiti için tarama başlatılıyor... {ip}")
                os.system(f"nmap --script http-enum,http-title -p 80,443 {ip}")
                break
            elif islem_no == 6:
                print(f"Local ağda ARP taraması yapılıyor... {ip}")
                os.system(f"nmap -sP -n {ip}")
                break
            elif islem_no == 7:
                print(f"Local ağda ARP taraması yapılıyor... (output sadece IP listesinden oluşur!): {ip}")
                os.system(f"nmap -sn {ip} | grep \"Nmap scan report\" | cut -d ' ' -f5")
                break
            elif islem_no == 0:
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçersiz seçim! Lütfen 0-7 arası değer giriniz.")
        except ValueError:
            print("Geçersiz giriş! Lütfen geçerli bir sayı giriniz.")
