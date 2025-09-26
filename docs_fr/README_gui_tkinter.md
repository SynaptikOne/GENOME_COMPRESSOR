#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# Licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licenses/MIT
#------------------------------------------------------------------------------

# Interface Graphique - `gui_tkinter.py`

---

## Description

`gui_tkinter.py` fournit une interface graphique simple et intuitive pour le projet **GENOME_COMPRESSOR**, développée avec Tkinter.  
Cette interface permet de :

- Compresser un fichier texte au format `.dna`  
- Décompresser un fichier `.dna` en fichier texte original  
- Visualiser les logs de traitement en temps réel  
- Activer/désactiver le mode verbeux  
- Consulter les informations sur l’auteur et les modules  

---

## Fonctionnalités

- **Compression** : Lecture d’un fichier `.txt`, encodage ADN, puis sauvegarde sous format `.dna`  
- **Décompression** : Lecture d’un fichier `.dna`, reconstruction de la séquence texte, puis export en `.txt`  
- **Mode verbeux** : Affiche les détails intermédiaires dans le journal d’exécution  
- **Zone de log** : Affichage des messages avec défilement automatique  
- **Fenêtre "À propos"** : Détails du projet, modules utilisés et informations sur l’auteur  

---

## Modules utilisés

- `genome_compressor.py`  
- `genome_decoder.py`  
- `storage_model.py`  
- `pattern_scanner.py`  
- `gene_encoder.py`  
- `mutation_encoder.py`  

---

## Dépendances

- Python ≥ 3.7  
- Tkinter (inclus dans l’installation standard de Python)

---

## Lancer l’application

```bash
python gui/gui_tkinter.py
