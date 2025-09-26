#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# Licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licenses/MIT
#------------------------------------------------------------------------------

# `genome_compressor.py`

---

## Présentation

Ce module est le cœur du système **GENOME_COMPRESSOR**.  
Il orchestre l'encodage bio-inspiré d'une séquence ADN en utilisant une approche modulaire basée sur :

- les **blocs** de taille fixe,
- les **motifs fréquents** (gènes),
- et les **mutations** entre séquences.

---

## Fonctionnalités

- Découpe d'une séquence en blocs de taille fixe.
- Détection des motifs les plus fréquents dans ces blocs.
- Encodage de ces motifs comme **gènes de référence**.
- Encodage des blocs sous forme de **mutations** par rapport aux gènes.
- Export du résultat compressé dans un fichier `.dna` au format JSON.

---

## Exemple d’utilisation

```python
from src.genome_compressor import GenomeCompressor

sequence = "AAATTTGTGTCCCAAATTAG"
compressor = GenomeCompressor(block_size=8)
compressed = compressor.compress(sequence)
compressor.save_to_dna(compressed, "output.dna")


Format du fichier .dna

{
    "genes": {
        "G0": "ATGC...",
        ...
    },
    "blocks": [
        {
            "gene": "G1",
            "mutation": "Mut_0_A,Mut_1_C,..."
        },
        ...
    ],
    "metadata": {
        "original_length": 32,
        "block_size": 8
    }
}



Dépendances

    pattern_scanner.py

    gene_encoder.py

    mutation_encoder.py


Tests

Des tests unitaires sont disponibles dans le dossier tests/
Le module de test principal est :

    tests/test_genome_compressor.py

Il peut être exécuté avec la commande suivante :


pytest tests/test_genome_compressor.py



