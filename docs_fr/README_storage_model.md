#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# Licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licenses/MIT
#------------------------------------------------------------------------------

# Module `storage_model.py`

---

## Description

Ce module centralise les opérations d’entrées/sorties pour les fichiers `.dna` générés par le projet **GENOME_COMPRESSOR**.  
Il garantit que les données compressées (gènes, blocs, métadonnées) soient sauvegardées dans un format structuré, lisible et compatible avec les futures versions du compresseur.

---

## Fonctions principales

- `StorageModel.save(data: dict, filename: str)`  
  Sauvegarde les données compressées dans un fichier `.dna` au format JSON avec indentation.

- `StorageModel.load(filename: str) -> dict`  
  Charge un fichier `.dna` existant et retourne son contenu sous forme de dictionnaire Python.

---

## Spécifications du format `.dna`

Les fichiers `.dna` doivent contenir les trois clés suivantes :

- `"genes"` : un dictionnaire de séquences ADN référencées (`G0`, `G1`, etc.)  
- `"blocks"` : une liste de blocs compressés contenant les noms de gènes et les mutations associées  
- `"metadata"` : informations générales, incluant `original_length`, `block_size`, et `format_version`

### Exemple :

```json
{
  "genes": {
    "G0": "ACGTACGT"
  },
  "blocks": [
    {
      "gene": "G0",
      "mutation": "Mut_0_A"
    }
  ],
  "metadata": {
    "original_length": 8,
    "block_size": 4,
    "format_version": "1.0"
  }
}



Tests unitaires

Les tests associés sont définis dans tests/test_storage_model.py et vérifient :

    la création correcte d’un fichier .dna

    la fidélité de la lecture (les données lues sont identiques aux données enregistrées)

    la détection des erreurs JSON mal formées


Exécution en ligne de commande (mode démonstration)

python3 src/storage_model.py



Ce mode teste la sauvegarde et la lecture sur des données factices dans un fichier test_output.dna.


Version actuelle du format

"format_version": "1.0"


Licence

Ce module fait partie du projet open source GENOME_COMPRESSOR


