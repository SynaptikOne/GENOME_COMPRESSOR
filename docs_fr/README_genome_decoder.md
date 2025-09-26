#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# Licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licenses/MIT
#------------------------------------------------------------------------------

# Module `genome_decoder.py`

**Fichier :** `src/genome_decoder.py`

---

## Description

Le module `genome_decoder.py` permet de décoder un fichier `.dna` généré par le compresseur **GENOME_COMPRESSOR**.  
Il s’appuie sur les blocs, les gènes et les mutations pour reconstruire fidèlement la séquence ADN d’origine.

Ce module est crucial pour valider la **réversibilité** de la compression.

---

## Fonctionnalités principales

- `GenomeDecoder.decode(data: dict) -> str`  
  Reconstruit la séquence ADN à partir des données chargées (`genes`, `blocks`, `metadata`).

- `GenomeDecoder.decode_from_file(filename: str) -> str`  
  Charge un fichier `.dna` et retourne la séquence ADN reconstruite.

- `GenomeDecoder.apply_mutation(gene_seq: str, mutation: str) -> str`  
  Applique une mutation simple (par défaut : **substitution de base**) à une séquence.

---

## Format attendu du fichier `.dna`

```json
{
  "genes": {
    "G0": "ACGTACGT"
  },
  "blocks": [
    {
      "gene": "G0",
      "mutation": "sub_2_T"
    }
  ],
  "metadata": {
    "original_length": 8,
    "block_size": 4,
    "format_version": "1.0"
  }
}


Résultat attendu :
ACTTACGT (remplacement de la base à l’indice 2 par "T")


Exécution de démonstration


python3 -m src.genome_decoder



Cela utilise un fichier .dna présent dans le dossier courant (ex. : test_output.dna) et affiche la séquence reconstruite.


Améliorations futures

    Support de mutations complexes (insertions, suppressions, inversions).

    Validation de l’intégrité via checksum.

    Tests unitaires avec des fichiers .dna pour cas limites.


Licence

Ce module fait partie du projet open source GENOME_COMPRESSOR.
Réutilisation libre avec mention de l’auteur.