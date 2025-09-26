#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# Licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licenses/MIT
#------------------------------------------------------------------------------

# MODULE `pattern_scanner.py`

---

## Description

Ce module fournit une classe `PatternScanner` permettant d’identifier les **motifs fréquents** dans une chaîne de caractères.  
Il est conçu pour être utile dans des systèmes de compression bio-inspirée ou d’analyse de données textuelles.

---

## Fonctionnalités

- Recherche de motifs de longueur variable (`min_length`, `max_length`)  
- Filtrage par fréquence minimale (`min_frequency`)  
- Deux algorithmes disponibles :
  - `naive` : méthode exhaustive, fiable pour toutes longueurs  
  - `rabin-karp` : méthode plus rapide, mais limitée à des longueurs fixes  
- Repli automatique vers `naive` si `rabin-karp` échoue  

---

## Exemple d’utilisation

```python
from pattern_scanner import PatternScanner

data = "bonjourbonjourbonsoirbonjour"

scanner = PatternScanner(min_length=6, max_length=6, min_frequency=2)
result = scanner.scan(data)
print(result)
# Sortie : {'bonjour': 3, 'onjour': 3, ...}



Structure interne

    PatternScanner : classe principale

    _scan_naive : implémentation exhaustive (brute force)

    _scan_rabin_karp : version optimisée par hachage

    Gestion automatique du fallback en cas d’échec d’une méthode

Tests

Le module est testé avec pytest dans tests/test_pattern_scanner.py

Commande d’exécution :

pytest tests/test_pattern_scanner.py


Améliorations à venir

    Optimisation mémoire pour les très grands fichiers

    Intégration directe dans le pipeline de compression


