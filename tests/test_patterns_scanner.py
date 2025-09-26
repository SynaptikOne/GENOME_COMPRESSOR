# tests/test_patterns_scanner.py

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
Tests unitaires pour le module pattern_scanner.

FR:
Ce fichier couvre les fonctionnalités suivantes :
- Détection naïve de motifs fréquents
- Détection par l'algorithme Rabin-Karp
- Choix automatique de la méthode selon les paramètres 
- Mécanisme de repli en cas d'échec de Rabin-Karp


FR:
Auteur                 : Rakotondravelo Tahina Mickaël


EN:
unit tests for the pattern_scanner module

This file covers the following features:
- Naive frequent pattern detection
- Detection using the Rabin-Karp algorithm
- Automatic method selection based on parameters
- Fallback mechanism in case of Rabin-Karp failure
- Utility functions (block splitting, frequent pattern extraction)





EN:
Author                 : Rakotondravelo Tahina Mickaël     
"""


import pytest
from src.pattern_scanner import PatternScanner

def test_naive_detection():

    """
    FR : Vérifie que la méthode naîve détecte correctement un motif récurrent
    EN : Check that the naive method correctyly detects arecurring pattern
    """
    scanner = PatternScanner(min_length=3, max_length=5, min_frequency=2, method="naive")

    result = scanner.scan("abcabcabcde")
    assert "abc" in result
    assert result["abc"] == 3

def test_rabin_karp_detection():
    
    """
    FR : Vérifie que Rabin-Karp détecte correctement un motif récurrent de longueur fixe.
    EN : Check that Rabin-Karp detects afixed-length recurring pattern
    """
    scanner = PatternScanner(min_length=3, max_length=3, min_frequency=2, method="rabin-karp")

    result = scanner.scan("abcabcabcde")
    assert "abc" in result
    assert result["abc"] == 3

def test_auto_mode_naive():

    """
    FR : Vérifie que le mode automatique choisit l'approche naîve quand min_length != max_length.
    EN : Check that auto chooses the naive method when min_length != max_length.
    """
    scanner = PatternScanner(min_length=3, max_length=4, min_frequency=2)
# min != max =>naîve

    result = scanner.scan("abababcabab")
    assert "aba" in result

def test_auto_mode_rabin_karp():

    """
    FR : Vérifie que le mode automatique utilise Rabin-Karp lorsque min_length == max_lenght.
    EN : Check that auto mode uses Rabin-Karp when min_length == max_length.
    """
    scanner = PatternScanner(min_length=4, max_length=4, min_frequency=2)
# min == max => rabin-karp
    result = scanner.scan("testtestoktest")
    assert "test" in result
    assert result["test"] == 3

def test_rabin_karp_fallback(monkeypatch):

    """
    FR : Simule un échec de Rabin-karp pour tester le repli vers l'approche naîve.
    EN : Simulate Rabin-Karp failure to test fallback to naive method.
    """
    # Force _scan_rabin_karp to fail
    scanner = PatternScanner(min_length=4, max_length=4, min_frequency=2)
    def fail(*args, **kwargs):
        raise RuntimeError("Fail Rabin-karp")
    monkeypatch.setattr(scanner, "_scan_rabin_karp", fail)

    # Ensure fallback works
    result = scanner.scan("abcdabcdabcd")
    assert "abcd" in result
    assert result["abcd"] == 3

def test_split_into_blocks():
    """
    FR : Vérife que split_into_blocks découpe correctemment une séquence en blocs de taille
    min_length
    EN : Check that split_into_blocks correctly splits the sequence into blocks of min_length.
    """
    scanner = PatternScanner(min_length=4)
    result = scanner.split_into_blocks("ACGTACGTAC")
    assert result == ["ACGT", "ACGT", "AC"]

def test_find_frequent_patterns():
    """
    FR : Vérifie que find_frequent_patterns retourne les motifs les plus 
    fréquentes dans les blocs.
    EN : Check that find_frequent_patterns returns the most frequent patterns in the blocks.
    """

    scanner = PatternScanner(min_length=3, max_length=3, min_frequency=2)
    blocks = ["abc", "abc", "abc", "def"]
    top = scanner.find_frequent_patterns(blocks, top_k=2)
    assert "abc" in top