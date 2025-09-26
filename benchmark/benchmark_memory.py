

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
Benchmark de consomation mémoire - GENOME_COMPRESSOR

Mesure la mémoire utilisée pendant la compression et la décompression de fichiers texte.
Les résultats sont enregistrés dans un fichier CSV et un rapport lisible.

Auteur   : Rakotondravelo Tahina Mickaël



EN:
Memory consumption benchmark - GENOME_COMPRESSOR

Measures memory usage during the compression and decompression of text files.
Results are saved in a CSV file and a human-readable report.

Author   : Rakotondravelo Tahina Mickaël
"""


import os
import sys
import time
import csv

import tracemalloc

# Ajout du chemin vers le dossier parent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cli import compressor_cli

INPUT_DIR = "test_performance/"
RESULTS_CSV = "benchmark/results_memory.csv"
RESULTS_TXT = "benchmark/results_memory_report.txt"


def run_with_memory_tracking(target_func, args):
    """
    FR:
    Exécute une fonction en suivant la mémoire avec tracemalloc.
    Retourne le pic de mémoire (en Mo) et le temps d'exécution (en s).

    EN:
    Runs a function with tracemalloc to track memory usage.
    Returns peak memory (in MB) and execution time (in seconds)
    """
    tracemalloc.start()
    start_time = time.time()

    target_func(*args)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Conversion en Mo
    peak_memory_mb = peak / (1024*1024)
    return peak_memory_mb, round(end_time - start_time, 2)
    

     

    




def benchmark_memory(filepath):
    """
    FR:
    Effectue un benchmark de consommation pour un fichier :
    compression puis décompression, avec mesure du pic mémoire et du temps.

    EN:
    Performs a memory usage benchmark for a file:
    compression then decompression, measuring peak memory and time.
    """
    dna_path = filepath.replace(".txt", ".dna")

    compress_mem, compress_time = run_with_memory_tracking(
        compressor_cli.main, (["compress", filepath, "-o", dna_path],)
    )

    decompress_mem, decompress_time = run_with_memory_tracking(
        compressor_cli.main, (["decompress", dna_path],)
    )

    return {
        "filename": os.path.basename(filepath),
        "compress_mem": round(compress_mem, 2),
        "decompress_mem": round(decompress_mem, 2),
        "compress_time": compress_time,
        "decompress_time": decompress_time
    }

def write_results(results, csv_path):
    """
    FR:
    Écrit les résultats du bechnmark dans un fichier CSV, incluant mémoire et temps.

    EN:
    Writes benchmark results toa a CSV file, including memory and time.
    """
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "filename", "compress_mem (MB)", "decompress_mem (MB)",
            "compress_time (s)", "decompress_time (s)"
        ])
        for row in results:
            writer.writerow([
                row["filename"], row["compress_mem"], row["decompress_mem"],
                row["compress_time"], row["decompress_time"]
            ])


def generate_report(results, txt_path):
    """
    FR:
    Génère un rapport texte lisible avec détails sur mémoire et temps pour chaque fichier traité

    EN:
    Generates a readable text report with memory and time details for each proccessd file.
    """
    with open(txt_path, "w")  as f:
        f.write("== RAPPORT DE MEMOIRE & TEMPS - GENOME_COMPRESSOR ==\n\n")

        for row in results:
            f.write(f"Fichier         : {row['filename']}\n")
            f.write(f"            Mémoire compression      : {row['compress_mem']}   Mo\n")
            f.write(f"            Mémoire décompression    : {row['decompress_mem']} Mo\n")
            f.write(f"            Temps compression        : {row['compress_time']}  s\n")
            f.write(f"            Temps décompression      : {row['decompress_time']}s\n")

            if row["decompress_mem"] < row["compress_mem"]:
                f.write("         Remarque  : Décompression plus légère en memoire.\n")

            else:
                f.write("         Remarque  : Décompression aussi gourmande ou plus lourde.\n")

            f.write("-" * 50 + "\n\n")
    print(f"[OK] Rapport généré : {txt_path}")


def main():
    """
    FR: Point d'entrée du script: exécute les benchmarks mémoire pour tous les fichiers texte.

    EN: Script entry point: runs memory benchmarks on all text files.
    """
    txt_files = [
        os.path.join(INPUT_DIR, f) for f in os.listdir(INPUT_DIR)
        if f.endswith(".txt")
    ]

    results = [benchmark_memory(f) for f in txt_files]

    write_results(results, RESULTS_CSV)
    generate_report(results, RESULTS_TXT)

    print(f"[OK] Resultats enregistrés : {RESULTS_CSV}")


if __name__ == "__main__":
    main()


    