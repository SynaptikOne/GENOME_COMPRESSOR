#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# Licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licenses/MIT
#------------------------------------------------------------------------------

# `mutation_encoder.py` - Encodeur de mutations pour séquences ADN

---

## Description

Le module `mutation_encoder` fournit un ensemble de fonctionnalités permettant de détecter, encoder, décoder et appliquer des mutations dans des séquences ADN.  
Il facilite la compression, la comparaison et la transformation de données génomiques.

---

## Fonctionnalités principales

- Encodage des différences entre une séquence et une référence.
- Décodage de mutations pour reconstituer une séquence mutée.
- Comparaison de blocs de séquences pour détecter les mutations.
- Génération d'une liste de mutations position par position.

---

### Représentation des mutations

Les mutations sont représentées sous la forme :

Mut_<position>_<nouvelle_base>


Les positions identiques sont notées `"-"`.

---

## Fonctions disponibles

### `encode_mutation(seq: str, ref: str) -> str`

Encode les différences entre `seq` et `ref` sous forme d’une chaîne de mutations.

**Exemple :**

```python
encode_mutation("ACCTACGA", "ACGTACGT")
# Résultat : "-,-,Mut_2_C,-,-,-,-,Mut_7_A"


compare_blocks(block1: str, block2: str) -> str

Compare deux blocs ADN et retourne les mutations entre eux.

Exemple :

compare_blocks("GATTACA", "GATCACC")
# Résultat : "-,-,-,Mut_3_C,-,-,Mut_6_C"



apply_mutation(original: str, mutation_code: str) -> str

Applique des mutations codées à une séquence d’origine.

Exemple :


apply_mutation("ACGTACGT", "-,-,Mut_2_C,-,-,-,-,Mut_7_A")
# Résultat : "ACCTACGA"



encode_mutations_in_sequence(seq: str, ref: str) -> List[str]

Retourne une liste de mutations entre deux séquences.

Exemple :


encode_mutations_in_sequence("TTAGCCAT", "TTGGCCAA")
# Résultat : ['-', '-', 'Mut_2_A', '-', '-', '-', 'Mut_6_A', 'Mut_7_T']



decode_mutation(original: str, mutation_code: str) -> str

Reconstitue une séquence mutée à partir d’une chaîne de mutations.

Exemple :


decode_mutation("ACGTACGT", "-,-,Mut_2_C,-,-,-,-,Mut_7_A")
# Résultat : "ACCTACGA"



Format des mutations

    Mutation : Mut_<indice>_<base>

    Identique : "-"

    Indexation : base 0


Prérequis

    Python 3.6 ou supérieur

    Aucune bibliothèque externe nécessaire


Licence

Ce projet est sous licence MIT.
Voir le fichier LICENSE pour plus d’informations.