# benchmark/benchmark_compression_ratio.py

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
Benchmark de ratio de compression pour le projet GENOME_COMPRESSOR.

Ce script exécute l'encodage ADN de tous les fichiers .txt situés dans le dossier test_performance/,
et mesure le ratio de compression, la taille des fichiers et le temps de traitement.

Auteur: Rakotondravelo Tahina Mickaël


EN:
Compression ratio benchmark for the GENOME_COMPRESSOR projetct.

This script performs DNA encoding of all .txt files in the test_performance/ folder,
and measures the compression ratio, file sizes, and processing time.


Author   : Rakotondravelo Tahina Mickaël
"""

import os
import csv
import time
import sys


# Ajout du chemin vers le répertoire parent pour accéder aux modules du projet
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cli import compressor_cli

INPUT_DIR = "test_performance/"
RESULTS_CSV = "benchmark/results_compression_ratio.csv"
RESULTS_TXT = "benchmark/results_compression_ratio.csv"

def get_file_size(filepath):
    """
    FR: Retourne la taille d'un fichier en octets.
    EN: Returns the size of a file in bytes."""
    return os.path.getsize(filepath)

def benchmark_file(filepath):
    """
    FR: Effectue la compression du fichier et mesure les performances.
    Retourne un dictionnaire contenant les résultats du benchmark.

    EN: Compress the file and measures performance.
    Returns a dictionary with the benchmark results.
    """
    dna_path = filepath.replace(".txt", ".dna")

    start = time.time()
    compressor_cli.main(["compress", filepath, "-o", dna_path])
    duration = time.time() - start

    original_size = get_file_size(filepath)
    compressed_size = get_file_size(dna_path)
    compression_ration = compressed_size / original_size

    return {
        "filename": os.path.basename(filepath),
        "original_size": original_size,
        "compressed_size": compressed_size,
        "compression_ratio": round(compression_ration, 4),
        "time_s": round(duration, 4),
    }

def write_csv(results, csv_path):
    """
    FR: Enregistre les résultats dans un fichier CSV.
    EN: Saves the benchmark results to a CSV file.
    """
    

    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        
        writer.writerow([
            "filename",
            "original_size (octets)",
            "compressed_size (octets)",
            "compression_ratio (=compressed/original)",
            "times_s (secondes)"
        ])
        for row in results:
            writer.writerow([
                row["filename"],
                row["original_size"],
                row["compressed_size"],
                row["compression_ratio"],
                row["time_s"]
            ])

def write_txt_summary(results, txt_path):
    """
    FR: Écrit un rapport lisible des benchmarks dans un fichier texte.
    
    EN: Writes a human-readable benchmark report to a text file.
    """
    with open(txt_path, "w") as f:
        f.write("=== RAPPORT DE BENCHMARK - GENOME_COMPRESSOR ===\n\n")
        for row in results:
            f.write(f"Fichier traité             : {row['filename']}\n")
            f.write(f"Taille originale           : {row['original_size']} octets\n")
            f.write(f"Taille compressée          : {row['compressed_size']} octets\n")
            f.write(f"Ratio de compression       : {row['compression_ratio']} (x la taille)\n")
            f.write(f"Durée du traitement        : {row['time_s']} secondes\n")

            if row["compression_ratio"] > 1:
                f.write("Note : Le fichier compressé est plus grand. Ce comportement est normal si le format .dna est structuré et lisible. \n")
            
            elif row["compression_ratio"] < 1:
                f.write("Note : Compression effective (taille réduite)")

            else:
                f.write("Note : Taille identique.\n")
            f.write("-" * 50 + "\n")


def main():
    """
    FR: Point d'entrée du script de benchmark.
    EN: Entry point for the benchmark script
    """
    txt_files = [os.path.join(INPUT_DIR, f) for f in os.listdir(INPUT_DIR) if f.endswith(".txt")]
    results = [benchmark_file(f) for f in txt_files]


    write_csv(results, RESULTS_CSV)
    write_txt_summary(results, RESULTS_TXT)
    print(f"[OK] Résultats enregistrés :\n - CSV : {RESULTS_CSV}\n - Rapport : {RESULTS_TXT}")


if __name__ == "__main__":
    main()