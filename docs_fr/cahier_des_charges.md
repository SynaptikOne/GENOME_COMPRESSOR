#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# Licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licenses/MIT
#------------------------------------------------------------------------------

# Cahier des charges - Projet GENOME_COMPRESSOR

---

## Objectif du projet
Créer un compresseur de fichiers bio-inspiré reposant sur l'encodage ADN, capable de compresser et décompresser efficacement de grandes séquences textuelles (par exemple des œuvres littéraires) en exploitant des motifs récurrents, la substitution de gènes et la réduction redondante de mutations.

---

## Modules principaux

### 1. `pattern_scanner.py`
- **Rôle :** Détecte les motifs répétitifs dans une séquence de texte.
- **Exigences :**
  - Détection rapide et robuste, y compris sur données bruitées.
  - Algorithme optimisé (Rabin-Karp).
  - Résistance aux longues séquences.
- **Tests :**
  - Couverture exhaustive via `test_pattern_scanner.py`.

---

### 2. `gene_encoder.py`
- **Rôle :** Encode les motifs trouvés en "gènes" ADN.
- **Exigences :**
  - Utilisation d'un alphabet ADN (A, T, C, G).
  - Encodage stable et déchiffrable.
  - Compatibilité avec l'algorithme de compression.
- **Tests :**
  - Validité des gènes, collisions, unicité.

---

### 3. `mutation_encoder.py`
- **Rôle :** Encode les différences ou mutations entre motifs similaires.
- **Exigences :**
  - Réduction de redondance entre motifs proches.
  - Encodage sous forme de mutation ADN (insertion, suppression, substitution).
- **Tests :**
  - Précision des mutations, robustesse face au bruit.

---

### 4. `genome_compressor.py`
- **Rôle :** Orchestration de la compression (motif → gène → mutation).
- **Entrée :** Fichier texte brut.
- **Sortie :** Fichier `.dna` compressé.
- **Format `.dna` :**
  - JSON structuré et versionné.
  - Contient :
    - Métadonnées (auteur, date, version),
    - Table des motifs,
    - Encodage ADN.

---

### 5. `storage_model.py`
- **Rôle :** Gestion des opérations de lecture/écriture des fichiers `.dna`.
- **Format :** JSON compressé et structuré.
- **Exigences :**
  - Support multi-version.
  - Portabilité.
  - Validation du format.

---

### 6. `genome_decoder.py`
- **Rôle :** Décompression du fichier `.dna` vers texte brut.
- **Exigences :**
  - Fidélité à l’original.
  - Validation du fichier `.dna`.
  - Traitement des erreurs.

---

### 7. `utils.py`
- **Rôle :** Fonctions utilitaires communes :
  - Encodage ADN.
  - Générateurs de motifs.
  - Validation de gènes.

---

## Autres composants

### `benchmark/`
- **Fichiers :**
  - `benchmark_compression_ratio.py`
  - `benchmark_speed.py`
  - `benchmark_memory.py`
- **But :** Évaluer les performances en :
  - Temps,
  - Mémoire,
  - Taux de compression.

### `tests_benchmark/`
- **Tests automatisés des benchmarks.**
- Vérifient la cohérence des mesures et fichiers générés (`.csv`, `.txt`).

---

## Interface utilisateur

### `cli/compressor_cli.py`
- **Interface en ligne de commande** avec options :
  - Compression d’un fichier,
  - Décompression,
  - Affichage des métadonnées.
- **Ergonomie :**
  - Aide intégrée,
  - Messages clairs.

---

## Contraintes techniques
- **Langage :** Python 3.12+
- **Structure projet :** Respect des standards de packaging Python (`setup.py`, `pyproject.toml`).
- **Tests :** Couverture ≥ 90 % avec `pytest`.
- **Environnement :** Développé dans un venv : `~/python_library/venv`.
- **Compatibilité :** Linux (Ubuntu), exportable sur d'autres plateformes.

---

## Documentation

- Stockée dans le dossier `/docs/`
- Contient :
  - Cahier des charges,
  - Diagrammes d’architecture,
  - Schémas du format `.dna`.

---

## Livrables
- Code source complet dans `src/`,
- Tests unitaires (`tests/`) et benchmarks (`tests_benchmark/`),
- CLI fonctionnelle,
- Rapport de performance,
- Documentation complète,
- Exemple d'utilisation.

---

## Évolutions possibles
- Interface web pour encodage/décodage en ligne,
- Compression parallèle,
- Support de plusieurs formats d’entrée (JSON, CSV).
