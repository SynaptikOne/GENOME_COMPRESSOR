#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# Licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licenses/MIT
#------------------------------------------------------------------------------

# Module `gene_encoder`

---

## But du module

Le module `gene_encoder` transforme des motifs textuels en séquences ADN compressées à l’aide d’un encodage binaire (2 bits/base).  
Il est utilisé dans le processus de compression génomique pour :

- Convertir des chaînes de caractères (motifs) en ADN synthétique encodé.
- Construire un dictionnaire de gènes à partir des motifs fréquents.
- Encoder des séquences complètes sous forme d’identifiants de gènes pour réduire la redondance.
- Permettre la reconstitution (décodage) des séquences ADN vers le texte initial.

---

## Exemple d’usage

### 1. Encodage d’un motif

```python
from src.gene_encoder import GeneEncoder

encoder = GeneEncoder()
dna = encoder.encode_motif("bio")
print(dna)  # Exemple de sortie : "CAGTC.."


2. Construction du dictionnaire de gènes

motifs = {"hello": 5, "world": 3}
gene_dict = encoder.build_gene_dict(motifs)
print(gene_dict)
# Sortie : {'gene1': '...', 'gene2': '...'}



3. Encodage d’une séquence par les gènes

sequence = "helloworldhello"
encoded = encoder.encode_sequence(sequence, motifs)
print(encoded)
# Sortie : ['gene1', 'gene2', 'gene1']


4. Décodage ADN vers texte

decoded = encoder.decode_dna(dna)
print(decoded)  # "bio"



Structure du dictionnaire

Deux dictionnaires internes sont utilisés dans GeneEncoder :
.gene_dict

{
    "gene1": "ACGTTGCA",  # Séquence ADN associée au motif
    "gene2": "CGGTAACC"
}


.reverse_dict


{
    "hello": "gene1",
    "world": "gene2"
}





