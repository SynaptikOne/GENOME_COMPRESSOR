

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
Test de benchmark de vitesse - GENOME_COMPRESSOR

Teste la créqtion des fichiers CSV et TXT générés lors du benchmark de vitesse:



Auteur  : Rakotondravelo Tahina Mickaël


EN:
Speed benchmark test - GENOME_COMPRESSOR

Tests the creation of CSV and TXT files generated during speed benchmarking.

Author               : Rakotondravelo Tahina Mickaël
"""

import os
import pytest
import sys

# Ajout du chemin vers le dossier parent pour importer le module benchmark_speed
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from benchmark import benchmark_speed as bs

def test_speed_benchmarK_execution(tmp_path):
    """
    FR:
    Vérifie l'exécution complète du benchmark de vitesse :
    - création d'un fichier temporaire,
    - exécution de la fonction main(),
    - génération des fichiers de résultats CSV et TXT,
    - présence des lignes/clés attendues.

    EN:
    Validates full speed benchmark execution:
    - creates a temporaty text file,
    - runs the main() function,
    - ensures output files (CSV and TXT) are generated,
    - checks for expected lines/keywords in reports.
    """
    # Création d'un fichier texte factice à compresser
    test_file = tmp_path / "tiny_sample.txt"
    test_file.write_text("ACGT" * 100)  # 400 caractere

    # Rédéfinir les chemins pour ne pas poluer les vrais dossier
    bs.INPUT_DIR = str(tmp_path)
    bs.RESULTS_CSV = str(tmp_path / "results_speed.csv")
    bs.RESULTS_TXT = str(tmp_path / "results_speed_report.txt")


    # Exécuter le benchmark
    bs.main()

    # Vérifier que les fichiers de résultats sont créés
    assert os.path.exists(bs.RESULTS_CSV)
    assert os.path.exists(bs.RESULTS_TXT)


    # Vérifier que le fichier CSV contient une ligne de résultats
    with open(bs.RESULTS_CSV, "r") as f:
        lines = f.readlines()
        assert len(lines) >= 2 # En-tête + au moins une ligne de résultat


    
    # Vérifier que le fichier TXT contient les mots-clés attendus
    with open(bs.RESULTS_TXT, "r") as f:
        content = f.read()
        assert "RAPPORT DE VITESSE" in content
        assert "Fichier" in content
        assert "Temps de compression" in content
        assert "Temps de décompression" in content
