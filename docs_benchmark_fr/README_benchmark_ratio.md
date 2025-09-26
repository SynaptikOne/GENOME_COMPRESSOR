#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# licensed under the MIT License. You may obtain a copy of the Licence at:
# https://opensource.org/licences/MIT
#------------------------------------------------------------------------------



# Benchmark : Taux de compression (`benchmark_compression_ratio.p`)

## Objectif

Ce script mesure le **taux de compression** obtenu par le projet `GENOME_COMPRESSOR`. Il applique l'encodage ADN à tous les fichiers texte (`.txt`) présents dans le dossier `test_performance`, et enregistre les resultats suivants :

- Taille originale du fichier 
- Taille du fichier compressée (`.dna`)
- Ration de compression (`compressed_size / original_size`)
- Temps de traitement (en secondes)

---

## Utilisation
Lancer le script :
```bash
python benchmark/benchmark_compression_ratio.py