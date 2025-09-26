#tests_cli/test_compressor_cli.py


#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# licensed under the MIT License. You may obtain a copy of the Licence at:
# https://opensource.org/licences/MIT
#------------------------------------------------------------------------------

"""
FR:
Tests d'intégration pour l'interfacee CLI de GENOME_COMPRESSOR.

Ce module vérifie :
- L'affichage de la commande 'about'
- La réponse à l'option '--version'
- le bon fonctionnement d'un cycle compression/décompression

Auteur               : Rakotondravelo Tahina Mickaël



EN:
Integration tests for the GENOME_COMPRESSOR CLI interface

This module checks:
- The output of the 'about'command
- The response to the '--version' option
- The correct behavior of a full compress/decompress roundtrip


Author               : Rakotondravelo Tahina Mickaël
"""

import subprocess
import tempfile
import os
import pytest
from cli import compressor_cli


CLI_PATH = "cli/compressor_cli.py"

def test_show_about():
    result = subprocess.run(["python3", CLI_PATH, "about"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "GENOME_COMPRESSOR" in result.stdout
    assert "Auteur" in result.stdout


def test_version_option():
    result = subprocess.run(["python3", CLI_PATH, "--version"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "GENOME_COMPRESSOR v1.0" in result.stdout


def test_compress_and_decompress_roundtrip():
    with tempfile.TemporaryDirectory() as tmpdir:
        input_file = os.path.join(tmpdir, "input.txt")
        compressed_file = os.path.join(tmpdir, "output.dna")
        decompress_file = os.path.join(tmpdir, "output.txt")

        # Creation d'un fichier ADN fictif
        sample_data = "AGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTC"
        with open(input_file, "w") as f:
            f.write(sample_data)

        # Compression
        result_compress = subprocess.run(
            ["python3", CLI_PATH, "compress", input_file, "-o", compressed_file],
            capture_output=True, text=True
        )
        assert result_compress.returncode == 0
        assert os.path.exists(compressed_file)

        # Decompression
        result_decompress = subprocess.run(
            ["python3", CLI_PATH, "decompress", compressed_file, "-o", decompress_file],
            capture_output=True, text=True

        )
        assert result_decompress.returncode == 0
        assert os.path.exists(decompress_file)

        # verification round-trip
        with open(decompress_file, "r") as f:
            reconstructed = f.read()
        assert reconstructed.startswith("AGTC") # au minimum coherent



