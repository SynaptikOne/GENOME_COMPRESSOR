

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
Test de benchmark de mémoire - GENOME_COMPRESSOR

Tests unitares pour vérifier la validité des mesures mémoire et fichiers générés
lors de la compression/décompression.

Auteur  : Rakotondravelo Tahina Mickaël



EN:
Memory benchmark tests - GENOME_COMPRESSOR

unit tests to validate memory measurements and generated files during compression/decompression

Author               : Rakotondravelo Tahina Mickaël
"""


import os
import csv
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from benchmark.benchmark_memory import benchmark_memory, write_results, generate_report

# Exemple de fichier test (doit exister dans test_performance/)
TEST_FILE = "test_performance/bel_ami_extrait.txt"
CSV_PATH = "benchmark/test_results_memory.csv"
TXT_PATH = "benchmark/test_results_memory_report.txt"

def test_benchmark_memory_output_structure():
    """
    FR:Vérifie que benchmark_memory retourn bine les bonnes clés
    EN: Checks that benchmark_memory returns the expected keys
    """
    result = benchmark_memory(TEST_FILE)
    expected_keys = {"filename", "compress_mem", "decompress_mem", "compress_time", "decompress_time"}

    assert set(result.keys()) == expected_keys
    assert result["compress_mem"] >= 0
    assert result["decompress_mem"] >= 0
    assert result["compress_time"] >= 0
    assert result["decompress_time"] >= 0


def test_write_results_creates_csv():
    """
    FR: Vérifie que le fichier CSV est bien généré et contient les bonnes colonnes
    EN: Verifies that the CSV file is correctly created and contains expected columns
    """

    results = [benchmark_memory(TEST_FILE)]
    write_results(results, CSV_PATH)

    assert os.path.exists(CSV_PATH)
    with open(CSV_PATH, newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        assert header == [
            "filename", "compress_mem (MB)", "decompress_mem (MB)",
            "compress_time (s)", "decompress_time (s)"
        ]

def test_generate_report_crates_txt():
    """
    FR: Vérifie que le fichier TXT de rapport contient les ligne attendues
    EN: Verifies that the TXT report file contains the expected lines
    """

    results = [benchmark_memory(TEST_FILE)]
    generate_report(results, TXT_PATH)

    assert os.path.exists(TXT_PATH)
    with open(TXT_PATH) as f:
        content = f.read()
        assert "== RAPPORT DE MEMOIRE & TEMPS" in content
        assert "Mémoire compression" in content
        assert "Temps compression" in content

@pytest.fixture(scope="session", autouse=True)
def cleanup_files():
    """
    FR: supprime les fichiers de test après les tests
    EN: Deletes test files after tests run
    """
    yield
    for path in [CSV_PATH, TXT_PATH]:
        if os.path.exists(path):
            os.remove(path)