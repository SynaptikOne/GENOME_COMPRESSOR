#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# licensed under the MIT License. You may obtain a copy of the Licence at:
# https://opensource.org/licences/MIT
#------------------------------------------------------------------------------



# Benchmark : vitesse de traitement (`benchmark_speed.py`)

## Objectif

Ce script permet de mesurer la **vitesse de compression et de décompression** du projet `GENOME_COMPRESSOR`, en testant tous les fichiers `.txt` du dossier `test_performance/`.

Il fournit :
- Le temps de compression (en secondes)
- Le temps de décompression
- Une remarque d'interprétation sur la rapidité relative des deux  phases

---

## Utilisation

Lancer le script :
```bash
python benchmark/benchmark_speed.py