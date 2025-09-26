# cli/compressor_cli.py


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
GENOME_COMPRESSOR - Interface en ligne de commande pour compresser et décompresser 
des fichiers ADN.

Auteur               : Rakotondravelo Tahina Mickaël


EN:
GENOME_COMPRESSOR - Command-line interface for compressing and decompressing
DNA sequence files.

Author               : Rakotondravelo Tahina Mickaël
"""
import inquirer
import argparse
import sys
import os
import time

from tqdm import tqdm

from colorama import Fore, Style, init

init()

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.pattern_scanner import PatternScanner
from src.gene_encoder import GeneEncoder
from src.mutation_encoder import MutationEncoder
from src.genome_compressor import GenomeCompressor
from src.genome_decoder import GenomeDecoder
from src.storage_model import StorageModel

def compress(input_path: str, output_path: str, verbose: bool = False):
    """
    FR: Compresse un fichier texte contenant une séquence ADN vers un fichier .dna.

    EN: Compresses a text file containing a DNA sequence into a .dna file.
    """
    start_time = time.time()

    if not os.path.exists(input_path):
        print(Fore.RED + f"[ERREUR] Fichier introuvable : {input_path}" + Style.RESET_ALL)
        sys.exit(1)

    print(Fore.BLUE + f"[INFO] Lécture du fichier {input_path}..." + Style.RESET_ALL)

    with open(input_path, "r", encoding="utf-8") as f:
        raw_data = f.read().strip()

    if not raw_data:
        print(Fore.RED + "[ERREUR] Le fichier est vide." + Style.RESET_ALL)
        sys.exit(1)

    block_size = 6
    compressor = GenomeCompressor(block_size=block_size)
    total_blocks = len(raw_data) // block_size + (1 if len(raw_data) % block_size else 0)

    
    print(Fore.BLUE + "[INFO] Compression finale..." + Style.RESET_ALL)
    compressed_chunks = []
    with tqdm(total=total_blocks, desc="Compression", unit="bloc", colour="green", dynamic_ncols=True) as pbar:
        for i in range(0, len(raw_data), block_size):
            block = raw_data[i:i + block_size]
            compressed = compressor.compress(block)
            compressed_chunks.append(compressed)
            pbar.update(1)
    
    compressed_data = compressor.compress(raw_data)
            

    

    if verbose:
        print(Fore.BLUE + f"[DEBUG] Aperçu compression: {str(compressed_data)[100]}..." + Style.RESET_ALL)
    
    StorageModel.save(compressed_data, output_path)

    print(Fore.GREEN + f"[SUCCES] Compression réussie : '{input_path}' -> '{output_path}'" + Style.RESET_ALL)


    elapsed = time.time() - start_time
    print(Fore.YELLOW + f"[FIN] Durée totale de compression : {elapsed:.2f} secondes" + Style.RESET_ALL)
    
 
    

def decompress(input_path: str, output_path: str, verbose: bool = False):
    """
    FR: Décompresse un fichier .dna vers un fichier texte brute.
    EN: Decompresses a .dna file inot a plain text file.
    """
    start_time = time.time()

    if not os.path.exists(input_path):
        print(Fore.RED + f"[ERREUR] Fichier .dna introuvable : {input_path}" + Style.RESET_ALL)
        sys.exit(1)
    

    if not input_path.endswith(".dna"):
        print(Fore.RED + "[ERREUR] Le fichier d'entrée doit avoir l'éxtension .dna" + Style.RESET_ALL)
        sys.exit(1)
    
    print(Fore.BLUE + f"[INFO] Décompréssion du fichier {input_path}..." + Style.RESET_ALL)
    

    # Lecture progressive pour montrer la barre de chargement
    file_size = os.path.getsize(input_path)
    with open(input_path, "r", encoding="utf-8") as f:
        buffer = []
        with tqdm(total=file_size, desc="Lecture .dna", unit="o", dynamic_ncols=True, leave=True, colour="magenta") as pbar:
            while True:
                chunk = f.read(1024)
                if not chunk:
                    break
                buffer.append(chunk)
                pbar.update(len(chunk))
    
    json_data = ''.join(buffer)
    if verbose:
        print(Fore.BLUE + f"[DEBUG] Taille .dna: {file_size} octets"+ Style.RESET_ALL)
        print(Fore.BLUE + "[DEBUG] Données JSON début:", json_data[:100],"...", Style.RESET_ALL)
    
    


    print(Fore.BLUE + "[INFO] Reconstruction de la séquence..." + Style.RESET_ALL)
    reconstructed = GenomeDecoder.decode_from_file(input_path)


    with open(output_path, "w", encoding="utf-8") as f:
        f.write(reconstructed)

    print(Fore.GREEN + f"[SUCCES] Décompréssion réussie : '{input_path}' -> '{output_path}'" + Style.RESET_ALL)
    
    elapsed = time.time() - start_time
    print(Fore.YELLOW + f"[FIN] Durée totale de décompréssion : {elapsed:.2f} secondes" + Style.RESET_ALL)


def show_about():
    """
    FR: Affiche les informations à propos du projet.
    EN: Displays information about the projetct.
    """
    print(Fore.CYAN + Style.BRIGHT + "[GENOME_COMPRESSOR] - Outil de compression ADN bio-inspiré" + Style.RESET_ALL)

    print("Vérsion       :", Fore.YELLOW + "v1.0" + Style.RESET_ALL)
    print("Auteur        :", Fore.GREEN + "Rakotondravelo Tahina Mickaël" + Style.RESET_ALL)
    print("Pays          :", "Madagascar")
    print("Date          :", "Mai 2025")

    print(Style.BRIGHT + "Description :" + Style.RESET_ALL)
    print("GENOME_COMPRESSOR est un outil de compression de séquence ADN basé sur:\n")
    print("- l'identification de motifs fréquents\n")
    print("- l'encodage génétique\n")
    print("- la modélisation des mutations\n")

    print(Style.BRIGHT + "Modules principaux :" + Style.RESET_ALL)
    print("- pattern_scanner.py\n")
    print("- gene_encoder.py\n")
    print("- mutation_encoder.py\n")
    print("- genome_compressor.py\n")
    print("- genome_decoder.py\n")
    print("- storage_model.py\n")

    print(Style.BRIGHT + "Utilisation rapide :" + Style.RESET_ALL)
    print("  puthon3 cli/compressor_cli.py compress fichier.txt -o fichier.dna\n")
    print("  python3 cli/compressor-cli.py decompress fichier.dna -o reconstruction.txt\n")
    print("  python3 cli/compressor_cli.py about\n")
    print(Fore.MAGENTA + "Projet développé avec passion pour la bio-informatique." + Style.RESET_ALL)



def interactive_menu():
    questions = [
        inquirer.List('action',
                      message="Que voulez-vous faire ?",
                      choices=['Compresser', 'Décompresser', 'Voir informations', 'Quitter']
                      ),

    ]
    answers = inquirer.prompt(questions)

    if answers['action'] == 'Compresser':
        input_path = input("Entrez le chemin du fichier à compresser : ")
        output_path = input("Entrez le chemin de sortie pour le fichier compressé (.dna) : ")
        verbose = input("Activer le mode verbeux ? (y/n) : ").lower().strip() == "y"
        compress(input_path, output_path, verbose=verbose)
    
    elif answers['action'] == 'Décompresser':
        input_path = input("Entrez le chemin du fichier .dna à décomprésser : ")
        output_path = input("Entrez le chemin de sortie pour la reconstruction (.txt) : ")
        verbose = input("Activer le mode verbeux ? (y/n) : ").lower().strip() == "y"
        decompress(input_path, output_path, verbose=verbose)

   

    elif answers['action'] == 'Voir informations':
        show_about()
    elif answers['action'] == 'Quitter':
        print("Merci d'avoir utilisé GENOME_COMPRESSOR ! ")
        sys.exit(0)



def main(args=None):
    if args is None:
        args = sys.argv[1:]
    

    parser = argparse.ArgumentParser(
        prog="GENOME_COMPRESSOR",
        description=(
            "GENOME_COMPRESSOR - Outil de compression et décompression ADN\n" \
            "" \
            "Auteur : Rakotondravelo Tahina Mickaël\n" \
            "Pays   : Madagascar\n" \
            "Usage  : \n" \
            "    python3 compressor_cli.py compress fichier.txt -o fichier.dna\n" \
            "    python3 compressor_cli.py  decompress fichier.dna -o reconstruction.txt\n" \
            "    python3 cli/compressor_cli.py about"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )

    
   
    subparsers = parser.add_subparsers(dest="command")

    # Sous-commande : compress
    compress_parser = subparsers.add_parser("compress", help="Compresser un fichier text ADN en format .dna")

    compress_parser.add_argument("input", help="Chemin du fichier texte à compresser")

    compress_parser.add_argument("-o", "--output", default="output.dna", help="Fichier de sortie .dna")
    compress_parser.add_argument("--verbose", action="store_true",help="Afficher plus de détails pendant l'exécution")

    # Sous-commnande : decompress
    decompress_parser = subparsers.add_parser("decompress", help="Décompresser un fichier .dna en text brut")

    decompress_parser.add_argument("input", help="Fichier .dna à décompresser")

    decompress_parser.add_argument("-o", "--output", default="reconstructed.txt",help="Fichier texte de sortie")
    decompress_parser.add_argument("--verbose", action="store_true", help="Afficher plus de details pendant l'éxécution")

    # Sous-commande : about
    subparsers.add_parser("about", help="Afficher les inforamtions sur le projet")

    # Option --version
    if "--version" in args:
        print(f"GENOME_COMPRESSOR v1.0 - {Fore.GREEN}Rakotondravelo Tahina Mickaël{Style.RESET_ALL}")
        sys.exit(0)


    if not args:
        print("[GENOME_COMPRESSOR] Bienvenue dans l'outil de compression ADN !")
        print(f"Auteur : {Fore.GREEN}Rakotondravelo Tahina Mickaël{Style.RESET_ALL}")
        print("Utilisez l'option '--help' pour voire les commandes disponibles.")
        interactive_menu()
        return
        

    
  

    args = parser.parse_args(args)

    if args.command == "compress":
        compress(args.input, args.output, verbose=args.verbose)
    elif args.command == "decompress":
        decompress(args.input, args.output, verbose=args.verbose)
    elif args.command == "about":
        show_about()



if __name__ == "__main__":
    main()
