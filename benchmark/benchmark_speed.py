

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
Benchmark de vitesse de compression et de séquence - GENOME_COMPRESSOR

Mesure le temps nécessaire pour compresser et décompresser des fichiers .txt du dossier
test_performance/.

Auteur  : Rakotondravelo Tahina Mickaël



EN:
Compression and decompression speed benchmark - GENOME_COMPRESSOR

Measures the time required to compress and decompress .txt files from the test_performance/ folder.

Author   : Rakotondravelo Tahina Mickaël
"""

import os
import sys
import time
import csv

# Ajout du chemin vers le répertoire parent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cli import compressor_cli

INPUT_DIR = "test_performance/"
RESULTS_CSV = "benchmark/results_speed.csv"
RESULTS_TXT = "benchmark/results_speed_report.txt"

def benchmark_speed(filepath):
    """
    FR: Effectue la compression et la décompression d'un fichier, et mesure les temps
    nécessaires.

    EN: Performs compression and decompression of a file, and measures the time taken.
    """
    dna_path = filepath.replace(".txt", ".dna")

    # Mesure du temps de compression
    start_compress = time.time()
    compressor_cli.main(["compress", filepath, "-o", dna_path])
    compress_time = time.time() - start_compress

    # mesure du temps de décompression
    start_decompress = time.time()
    compressor_cli.main(["decompress", dna_path])
    decompress_time = time.time() - start_decompress


    return {
        "filename": os.path.basename(filepath),
        "compress_time": round(compress_time, 4),
        "decompress_time": round(decompress_time, 4)
    }

def write_results(results, csv_path):
    """
    FR: Enregistre les temps de compression et de décompression dans un fichier CSV.

    EN: Saves the compression and decompression time into a CSV file.
    """
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["filename", "compress_time (s)", "decompress_time (s)"])

        for row in results:
            writer.writerow([row["filename"], row["compress_time"], row["decompress_time"]])


def generate_report(results, txt_path):
    """
    FR: Génère un rapport lisible des vitesse de traitement et ajoute un remarque selon les résultats.

    EN: Generates a human-readable report of processing speeds and adds a remark vbased on results.
    """
    with open(txt_path, "w") as f:
        f.write("== RAPPORT DE VITESSE - GENOME_COMPRESSOR ==\n\n")
        for row in results:
            f.write(f"Fichier        : {row['filename']}\n")
            f.write(f"   Temps de compression     :   {row['compress_time']} secondes\n")
            f.write(f"   Temps de décompression   :   {row['decompress_time']} secondes\n")

            if row['decompress_time'] < row['compress_time']:
                f.write("   Remarque : Décompression plus rapide que la compression.\n")
            
            else:
                f.write("   Remarque : Décompression aussi lente ou plus lente (à analyser).\n")

            f.write("-" * 50 + "\n")
    
    print(f"[OK] Rapport généré : {txt_path}")


def main():
    """
    FR: Point d'entrée du script de benchmark de vitesse. Traite tous les fichiers texte et enregistre les résultats.

    EN: Entry point of the speed benchmark script. Processes all text files and saves the results.
    """
    txt_files = [os.path.join(INPUT_DIR, f) for f in os.listdir(INPUT_DIR) if  f.endswith(".txt")]
    results = [benchmark_speed(f) for f in txt_files]
    write_results(results, RESULTS_CSV)
    generate_report(results, RESULTS_TXT)
    print(f"[OK] Resultats enregistrés : {RESULTS_CSV}")


if __name__ == "__main__":
    main()