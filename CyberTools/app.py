#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import src.component.nmap as nmap
import src.component.gobuster as gobuster
import src.component.hydra as hydra
import src.component.file as files
import src.component.kriptoloji as kripto
import src.component.macchanger as macch
import src.component.firewall as firewall

def figlet():
    os.system("apt-get install figlet")
    os.system("clear")
    os.system("figlet -f slant -c '\033[ eysA \033['")

def anaekran():
    print("""
        ----------------------
            List Of Tools
        ----------------------

        1 - NMAP
        2 - Gobuster
        3 - Macchanger
        4 - Binwalk
        5 - Hydra
        6 - Kriptoloji
        7 - Firewall
        0 - Quit
    """)

def main():
    figlet()
    anaekran()

    while True:
        islem_no = input("Select an option from menu: ")

        if islem_no == "1":
            nmap.nmap_hello()
        elif islem_no == "2":
            gobuster.gobuster_hello()
        elif islem_no == "3":
            macch.mac_degis()
        elif islem_no == "4":
            files.file_information()
        elif islem_no == "5":
            hydra.hydra_hello()
        elif islem_no == "6":
            kripto.kriptoloji_hello()
        elif islem_no == "7":
            firewall.firewall_hello()
        elif islem_no == "0":
            print("Exiting...")
            break
        else:
            print("Invalid menu option was chosen ")

if __name__ == "__main__":
    main()
