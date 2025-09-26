#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# licensed under the MIT License. You may obtain a copy of the Licence at:
# https://opensource.org/licences/MIT
#------------------------------------------------------------------------------

# Benchmark : Consommation mémoire (`benchmark_memory.py`)

## Objectif

Ce script mesure la **consommation mémoire** et le **temps d'exécution** du projet `GENOME_COMPRESSOR` lors de la **compression** et de la **décompression** de fichiers texte.

Il fournit des résultats chiffrés sur:
- Le pic mémoire utilisé (en Mo)
- La durée du traitement (en secondes)
- La comparaison entre compression et décompression

---

## Utilisation

Lancer le script :
```bash
python benchmark/benchmark_memory.py