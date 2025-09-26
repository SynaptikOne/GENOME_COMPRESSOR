# tests/test_genome_compressor


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
Tests unitaires pour le module genome_compressor.py.

Ce fichier vérifie que la compression fonctionne correctement :
- Structure du résultat
- Cohérence des blocs
- Génération des gènes
- Sauvegarde dans un fichier .dna

Auteur                  : Rakotondravelo Tahina Mickaël


EN:
Unit tests for the genome_compressor.py module.

This file checks that compression works correctly:
- Result structure
- Block consistency
- Gene generation
- saving to .dna file

Author                  : Rakotondravelo Tahina Mickaël
"""


import pytest
from src.genome_compressor import GenomeCompressor

def test_compress_structure():
    """
    FR:
    Vérifie que la structure retournée par `compress()` contient les bonnes clés.
    EN:
    Checks that the structure returned by 'compress()' contains the correct keys.
    """
    seq = "ACGTACGTACGTACGTACGTACGTACGTACGT"
    compressor = GenomeCompressor(block_size=4)
    result = compressor.compress(seq)

    assert "genes" in result
    assert "blocks" in result
    assert "metadata" in result

    assert isinstance(result["genes"], dict)
    assert isinstance(result["blocks"], list)
    assert isinstance(result["metadata"], dict)
    assert "original_length" in result["metadata"]
    assert "block_size" in result["metadata"]

def test_compress_block_size():
    """
    FR:
    Vérifie que chaque bloc compressé contient un clé 'gene' et une mutation valide.

    EN:
    Checks that each compressed block containts a 'gene' key and a valid mutation string.
    """
    seq = "ACGTACGTACGTACGTACGTACGTACGTACGT"
    block_size = 8
    compressor = GenomeCompressor(block_size=block_size)
    result = compressor.compress(seq)

    for block in result["blocks"]:
        assert "gene" in block 
        assert "mutation" in block
        assert isinstance(block["mutation"], str) or block["mutation"] is None

def test_compress_non_empty_genes():
    """
    FR:
    Vérifie que des gènes sont bien générés et que leur nom suit le format 'Gx'.

    EN:
    Checks that genes are generated and that their names follow the format 'Gx'.
    """
    seq = "ACGTACGTACGTACGTACGTACGTACGTACGT"
    compressor  = GenomeCompressor(block_size=4)
    result = compressor.compress(seq)

    assert len(result["genes"]) > 0
    for name, seq in result["genes"].items():
        assert name.startswith("G")
        assert isinstance(seq, str)

def test_save_to_dna(tmp_path):
    """
    FR:
    Vérifie que le fichier .dna est bien créé et contient les bonnes sections.

    EN:
    Checks that the .dna file is properly created and contains the expected sections.
    """
    seq = "ACGTACGTACGTACGTACGTACGTACGTACGT"
    compressor = GenomeCompressor(block_size=8)
    result = compressor.compress(seq)

    output_file = tmp_path / "output.dna"
    compressor.save_to_dna(result, str(output_file))


    assert output_file.exists()
    content = output_file.read_text()
    assert '"genes":' in content
    assert '"blocks":' in content
    assert '"metadata":' in content
    