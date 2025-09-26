# gui_tkinter

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
gui_tkinter.py
Interface graphique pour l'outil GENOME_COMPRESSOR utilisant Tkinter.

Auteur                : Rakotondravelo Tahina Mickaël


EN:
Graphical user interface for the GENOME_COMPRESSOR tool using Tkinter.

Author                : Rakotondravelo Tahina Mickaël
"""

import os
import sys
import threading
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from PIL import Image, ImageTk
from gui.splash_screen import show_splash
from src.genome_compressor import GenomeCompressor
from src.genome_decoder import GenomeDecoder
from src.storage_model import StorageModel


# Compatibilite avec touste les version de Pillow
try:
    resample_mode = Image.Resampling.LANCZOS
except AttributeError:
    resample_mode = Image.ANTIALIAS



class GenomeCompressorApp(tk.Tk):
    """
    FR: Fenêtre principale de l'application Tkinter pour la compression et décompression de
    fichiers ADN.

    EN: Main Tkinter application window for DNA file compression and decompression
    """
    def __init__(self):
        """
        FR: Initialise l'application graphique, configure la fenêtre et prépare les composants de 
        l'interface

        EN: Initialize the graphical application, sets up the window, and prepares UI components.
        """
        super().__init__()
        self.title("GENOME_COMPRESSOR - Interface Graphique")
        self.geometry("700x500")
        self.configure(bg="#f0f0f0")
        self.compressor = GenomeCompressor()

        #Chargement et redimensionnement du logo
        image_path = os.path.join("splash", "GENOME_COMPRESSOR.png")
        logo_pil = Image.open(image_path).resize((150, 150), resample_mode)
        self.logo_image = ImageTk.PhotoImage(logo_pil)
        
        logo_label = tk.Label(self, image=self.logo_image, bg="#f0f0f0")
        logo_label.pack(pady=5)


        self.create_widgets()

    def create_widgets(self):

        """
        FR: Crée tous les éléments graphiques (boutons, case à cocher, zone de texte)
        de l'interface
        
        EN: Creates all UI elements (buttons, checkboxes, text area) of the interface
        """
        
        # Initialisation de la variable pour le mode verbeurx
        self.verbose_mode = tk.BooleanVar(value=True)

        # Boutons
        tk.Button(self, text="Compresser un fichier texte", command=self.compress_file, width=40, bg="#cce5ff").pack(pady=5)
        tk.Button(self, text="Décompresser un fichier .dna", command=self.decompress_file, width=40, bg="#d4edda").pack(pady=5)

        # Case à cocher : mode verbeux
        tk.Checkbutton(self, text="Mode verbeux", variable=self.verbose_mode, bg="#f0f0f0").pack(pady=5)

        # Bouton à propos
        tk.Button(self, text="À propos", command=self.show_about, width=40, bg="#fff3cd").pack(pady=5)


        


        # Zone de log
        self.log_text = scrolledtext.ScrolledText(self, wrap=tk.WORD,height=20, bg="white")
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def log(self, message):
        """
        FR: Ajoute un message à la zone de log avec défilement automatique.

        EN: Apends a message to the log area with automatic scrolling
        """
        self.log_text.insert(tk.END, message + '\n')
        self.log_text.see(tk.END)

    def compress_file(self):
        """
        FR: Ouvre un fichier texte, le compresse en utilisant GenomeCompressor, plus
        sauvegarde le fichier compressé.
        
        EN: Opens a text file, compresses it using GenomeCompressor , and saves the compressed file
        """
        input_path = filedialog.askopenfilename(title="Sélectionner un fichier texte",
                                                filetypes=[("Fichiers texte", "*.txt")])
        if not input_path:
            return
        
        try:
            with open(input_path, "r", encoding="utf-8") as f:
                raw_data = f.read()
            self.log(f"Fichier chargé : {os.path.basename(input_path)} ({len(raw_data)} caractère)")
            compressed = self.compressor.compress(raw_data)
            if self.verbose_mode.get():
                self.log("[VERBOSE] Données compressées (extrait) : ")
                self.log(str(compressed)[:200] + "...")

            output_path = filedialog.askopenfilename(title="Enregistrer le fichier compressé",
                                                     defaultextension=".dna",
                                                     filetypes=[("Fichier ADN compressé", "*.dna")])
            if output_path:
                StorageModel.save(compressed, output_path)
                
                self.log(f"Compression réussie ! Fichier sauvegardé : {output_path}")

            else:
                self.log("Compression annulée : aucun fichier de sortie sélectionné.")

        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la compression : {str(e)}")

            self.log(f"[Erreur] {str(e)}")

    def decompress_file(self):
        """
        FR: Ouvre un fichier .dna, la décompresse avec GenomeDecoder, puis sauvegarde le
        fichier texte reonstitué.

        EN: Opens a .dna file, decompresses it using GenomeDecoder, and saves the reconstructed text file.
        """
        input_path = filedialog.askopenfilename(title="Sélectionner un fichier .dna", 
                                                filetypes=[("fichiers ADN compressés", "*.dna")])
        if not input_path:
            return
        
        try:
            reconstructed_seq = GenomeDecoder.decode_from_file(input_path)
            if self.verbose_mode.get():
                self.log("[VERBOSE] Reconstruction partielle :")
                self.log(reconstructed_seq[:200] + "...")

            output_path = filedialog.askopenfilename(title="Enregistrer le fichier reconstitué",
                                                     defaultextension=".txt",
                                                     filetypes=[("Fichiers texte", "*.txt")])
            if output_path:
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(reconstructed_seq)

                self.log(f"Décompression réussie ! Fichier sauvegardé : {output_path}")
            else:
                self.log("Décompression annulée : aucun fichier de sortie sélectionné.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la décompression : {str(e)}")

            self.log(f"[Erreur] {str(e)}")
    
    def show_about(self):
        """
        FR: Affiche une fenêtre "À propos" contenant les informations de l'auteur
        et les modules utilisés.
        
        EN: Displays an "About" window containing author information and used modules
        """

        # Creer une fenetre secondaire
        about_window = tk.Toplevel(self)
        about_window.title("À propos de GENOME_COMPRESSOR")
        about_window.geometry("600x400")
        about_window.configure(bg="#fdfdfd")

        # Logo dans la fenetre " À propos"
        image_path = os.path.join("splash", "GENOME_COMPRESSOR.png")
        logo_pil = Image.open(image_path).resize((120, 120), resample_mode)
        logo_img = ImageTk.PhotoImage(logo_pil)
        
        logo_label = tk.Label(about_window, image=logo_img, bg="#fdfdfd")
        logo_label.image = logo_img # Necessaire pour garder la reference

        logo_label.pack(pady=10)

        # texte principale
        message = (
            "GENOME_COMPRESSOR - Outil de compression ADN bio-inspire\n" \
            "Version       : v1.0\n" \
            "Auteur        : "
        )

        text_widget = tk.Text(about_window, wrap=tk.WORD, bg="#fdfdfd", relief=tk.FLAT, font=("Helvetica", 11))
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Insertion du texte principale
        text_widget.insert(tk.END, message)

        
        text_widget.insert(tk.END, "Rakotondravelo Tahina Mickaël\n", "green_text")

        # Suite du message
        suit = (
            "Pays           : Madagascar\n" \
            "Date           : 8 Août 2025\n\n" \
            "Modules utilisés    :\n" \
            " - pattern_scanner.py\n" \
            " - gene_encoder.py\n" \
            " - mutation_encoder.py\n" \
            " - genome_comressor.py\n" \
            " - genome_decoder.py\n" \
            " - storage_model.py\n\n" \
            "Inspiré de la structure biologique de l'ADN,\n" \
            "cet outil identifie les motifs fréquents,\n" \
            "encode les gènes et modélise les mutations.\n\n" \
            "Développé avec passion pour la bio-informatique."

        )
        text_widget.insert(tk.END, suit)

        # Appliquer le style
        text_widget.tag_config("green_text", foreground="green")

        text_widget.config(state=tk.DISABLED)


        


if __name__ == "__main__":
    # Affiche le splash (bloquant)
    show_splash("splash/GENOME_COMPRESSOR.png", duration=3000)
    

    # Demarre ensuite l'application principale
    app = GenomeCompressorApp()
    app.mainloop()
        