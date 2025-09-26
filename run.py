
#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licences/MIT
#------------------------------------------------------------------------------


"""
FR:
Point d'entrée principale de l'application GENOME_COMPRESSOR.
Permet à l'utilisateur de choisir entre une interface graphique (GUI) ou interface en ligne de commande (CLI)

Auteur             : Rakotondravelo Tahina Mickaël


EN:
Main entry point of the GENOME_COMPRESSOR application.
Allows the user to choose between a graphical interface (GUI) or a command-line interface (CLI)

Author               : Rakotondravelo Tahina Mickaël
"""
import subprocess 
import os
import sys


def start_cli():
    """
    FR: Lance l'interface en ligne de commande exn exécutant le script compressor_cli.py

    EN: Launches the command-line interface by executing the compressor_cli.py script.
    """
    
    subprocess.run([sys.executable, "cli/compressor_cli.py"])


def start_gui():
    """
    FR: Lance l'interface graphique Tkinter en exécutant le script gui_tkinter.py

    EN: Launches the Tkinter graphical interface by executing the gui_tkinter.py script.
    """
    subprocess.run([sys.executable, "gui/gui_tkinter.py"])

def main():
    """
    FR: Affiche un menu pour permettre à l'utilisateur de choisir entre GUI, CLI ou quitter l'application

    EN: Displays a menu to let the user choose between GUI, CLI, or exiting the application
    """
    print("Bienvenu dans GENOME_COMPRESSOR")
    print("---------------------------------------------------------------")
    print("(c) 2025 Rakotondravelo Tahina Mickaël")
    print("licensed under the MIT License")
    print("https://opensource.org/licences/MIT")
    print("---------------------------------------------------------------\n\n")
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