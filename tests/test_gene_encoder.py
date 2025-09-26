# tests/test_gene_encoder.py


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
Tests unitaires pour le module gene_encoder.

Ce fichier vérifie les fonctionnalités principale:
- Encodage de motifs en ADN
- Construction d'un dictionnaire de gènes
- Encodage de séquences complètes en blocs compressés
- Décodage ADN -> texte


Auteur : Rakotondravelo Tahina Mickaël


EN:
Unit tests for gene_encoder module.

This file validates the following features:
- Encoding of motifs into DNA
- Gene dictionnary construction
- Encoding of full sequences inot compressed blocks
- DNA to text decoding

Author                     : Rakotondravelo Tahina Mickaël
"""

import pytest
from src.gene_encoder import GeneEncoder

def test_encoding_single_motif():

    """
    FR:
    Vérifie qu'un motif texte est correctement encodé en ADN.
    et que le décodage restitue bien le motif original.

    EN:
    Verifies tha a text motif is properly encoded into DNA, and that decoding 
    restores the original motif.
    """
    encoder = GeneEncoder()
    motif = "AC"
    dna = encoder.encode_motif(motif)
    assert isinstance(dna, str)
    assert all(c in "ACGT" for c in dna)
    assert encoder.decode_dna(dna) == motif

def test_build_gene_dict():

    """
    FR:
    Vérifie que le dictionnaire de gènes est bien construit à partir d'un
    ensemble de motifs donnés.

    EN:
    Checks that the gene dictionary is properly built from a given set of motifs.
    """
    encoder = GeneEncoder()
    motifs = {"hello": 3, "world": 2}
    gene_dict = encoder.build_gene_dict(motifs)
    assert "gene1" in gene_dict and "gene2" in gene_dict
    assert all(set(seq).issubset({"A","C","G","T"}) for seq in gene_dict.values())

def test_encode_sequence_with_genes():
    """
    FR:
    Vérifie que les motifs présents dans la séquence sont remplacés par des
    identifiants de gènes, et que les caractères inconnus sont conservés.

    EN:
    Ensure that known motifs in the sequence are replaced with gene IDs and unknown
    caracters are preserved
    """

    encoder = GeneEncoder()
    motifs = {"abc": 5, "def": 4}
    encoder.build_gene_dict(motifs)
    encoded = encoder.encode_sequence("abcxxdefabc", motifs)

    # Devrait reconnaître les motifs et encoder les autres caractères
    assert encoded.count("gene1") + encoded.count("gene2") >= 2
    assert "x" in encoded

def test_decode_dna():
    
    """

    FR:
    Vérife que le décodage d'une séquence ADN reconstruit correctement le motif
    texte d'origine.

    EN:
    Verifies that decoding a DNA sequence correclty restores the original text motif.
    """

    encoder = GeneEncoder()
    motif = "bio"
    dna = encoder.encode_motif(motif)
    decode = encoder.decode_dna(dna)
    assert decode == motif

