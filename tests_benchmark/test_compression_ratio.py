# tests_benchmark/ test_compression_ratio.py

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
Test du module benckmark_compression_ratio - GENOME_COMPRESSOR

Ce test vefirie que le benchmark de ration de compression fonctionne correctement:
- Génération des fichiers CSV et TXT
- Validité minimale des contenus générés

Auteur               : Rakotondravelo Tahina Mickaël


EN:
Test for the benchmark_compression_ratio module - GENOME_COMPRESSOR

This test checks that the compression ration benchmark works correctly:
- Generation of CSV and TXT files
- Basic validity of generated content

Author               : Rakotondravelo Tahina Mickaël
"""

import os
import pytest
import sys
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from benchmark import benchmark_compression_ratio as bcr

def test_benchmark_on_tiny_file(tmp_path):
    """
    FR:
    Vérifie que le benchmark de compression s'exécute correctement et génè les 
    fichiers CSV et TXT avec des resultats valides.

    EN:
    ensures the compression benchmark:
    - creates a mock .tx file,
    - redirects output paths properly,
    - generates the expected CSV and TXT files,
    - includes the minimal required in each file
    """

    # Creation d'un fichier  .txt factice à compresser
    test_file = tmp_path / "tiny_sample.txt"
    test_file.write_text("ACGT" * 100) # 400 caractères

    # Redirection temporaire des chemins utilisés dans le benchmark
    bcr.INPUT_DIR = str(tmp_path)
    bcr.RESULTS_CSV = str(tmp_path / "results_test.csv")
    bcr.RESULTS_TXT = str(tmp_path / "results_text.txt")

    # Lancement du benchmark
    bcr.main()

    # vérifie que les fichiers de resultats ont bien été créés
    assert os.path.exists(bcr.RESULTS_CSV)
    assert os.path.exists(bcr.RESULTS_TXT)


    # Vérifie que le fichier CSV contient bien des lignes de résultats
    with open(bcr.RESULTS_CSV, "r") as f:
        lines = f.readlines()
        assert len(lines) >= 2 # 1 ligne d'en-tête + 1 ligne de résultat

    
    # Vérifie que le fichier TXT contient les informations du rapport
    with open(bcr.RESULTS_TXT, "r") as f:
        contenu = f.read()
        assert "RAPPORT DE BENCHMARK" in contenu
        assert "Fichier traité" in contenu
        assert "Ratio de compression" in contenu

