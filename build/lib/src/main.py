import os
import sys


def start_cli():
    os.system(f"{sys.executable} -m cli/compressor_cli.py")

def start_gui():
    os.system(f"{sys.executable} -m gui/gui_tkinter.py")

def main():
    print("Bienvenu dans GENOME_COMPRESSOR -- (copyright) 2025 --\n")
    print("Choisissez le mode d'utilisation : ")
    print("1 . Interface graphique (Tkinter)")
    print("2 . Interface ligne de commande (CLI)")
    print("0 . Quitter")

    choix  = input("Votre choix : ").strip()

    if choix == "1":
        start_gui()
    elif choix == "2":
        start_cli()
    elif choix == "0":
        print("Au revoire.")
    else:
        print("Choix invalide.")
        main()
if __name__ == "__main__":
    main()