# tests/test_mutation_encoder.py

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
Tests unitaire pour le module mutation_encoder.

Ce fichier vérifie les fonctionnalités suivantes :
- Encodage de mutations entre une sequence et une référence
- Comparaison bloc à bloc de deux sèquence
- Encodage et décodage de mutation à une séquence complète

Auteur             : Rakotondravelo Tahina Mickaël


EN:
Unit tests for the mutation_encoder module

This file verifies the following functionalities:
- Encoding mutations between a sequence and a reference
- Block-by-block comparison of two sequences
- Encoding and decoding mutations on a complete sequence

Author               : Rakotondravelo Tahina Mickaël
"""

import pytest

from src.mutation_encoder import MutationEncoder

@pytest.fixture
def encoder():
    return MutationEncoder()

def test_encode_mutation(encoder):
    ref = "ACGTACGT"
    seq = "ACCTACGA"
    expected = "-|-|Mut_2_C|-|-|-|-|Mut_7_A"
    result = encoder.encode_mutation(seq, ref)
    assert result == expected

def test_compare_blocks(encoder):
    block1 = "GATTACA"
    block2 = "GATCACC"
    expected = "-|-|-|Mut_3_C|-|-|Mut_6_C"
    result = encoder.compare_blocks(block1, block2)
    assert result == expected

def test_apply_mutation(encoder):
    original = "ACGTACGT"
    mutation = "-|-|Mut_2_C|-|-|-|-|Mut_7_A"
    expected = "ACCTACGA"
    result = encoder.apply_mutation(original, mutation)
    assert result == expected

def test_encode_mutations_in_sequence(encoder):
    ref = "TTGGCCAA"
    seq = "TTAGCCAT"
    expected = ['-', '-', 'Mut_2_A', '-', '-', '-' ,'-', 'Mut_7_T']
    result = encoder.encode_mutations_in_sequence(seq, ref)
    assert result == expected

def test_decode_mutation(encoder):
    original = "ACGTACGT"
    encoded_muation = "-|-|Mut_2_C|-|-|-|-|Mut_7_A"
    expected = "ACCTACGA"
    result = encoder.decode_mutation(original, encoded_muation)
    assert result == expected