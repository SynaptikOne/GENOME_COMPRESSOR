#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# Licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licenses/MIT
#------------------------------------------------------------------------------

# `compressor_cli.py` - Interface CLI pour GENOME_COMPRESSOR

## Présentation

**GENOME_COMPRESSOR** est un outil de compression de séquences ADN inspiré des mécanismes biologiques.  
Le module `compressor_cli.py` fournit une interface en ligne de commande conviviale pour compresser et décompresser des fichiers.

---

## Commandes disponibles

```bash
python3 cli/compressor_cli.py <commande> [arguments] [options]


1. compress

Description : Compresse un fichier texte contenant une séquence ADN vers un fichier .dna.

Syntaxe :
python3 cli/compressor_cli.py compress <input_file> -o <output_file> [--verbose]



Arguments :

    <input_file> : chemin du fichier texte contenant l’ADN brut.

    -o, --output : fichier .dna de sortie (par défaut : output.dna).

    --verbose : affiche des informations supplémentaires (blocs, mutations, références, etc.)

python3 cli/compressor_cli.py compress data/adn.txt -o result.dna



2. decompress

Description : Décompresse un fichier .dna vers une séquence ADN brute.

Syntaxe :


python3 cli/compressor_cli.py decompress <input_file> -o <output_file> [--verbose]




Arguments :

    <input_file> : chemin du fichier .dna à décompresser.

    -o, --output : fichier texte contenant la séquence reconstruite (par défaut : reconstructed.txt).

    --verbose : affiche la taille, les premières données JSON, etc.



Exemple :

python3 cli/compressor_cli.py decompress result.dna -o reconstruction.txt --verbose



3. about

Description : Affiche les informations générales sur le projet, les modules et l’auteur.

Commande :


python3 cli/compressor_cli.py about


Autres options

    --version : affiche la version de l’outil et le nom de l’auteur.



python3 cli/compressor_cli.py --version


Lancement sans argument : ouvre une interface interactive (menu navigable via les flèches/clavier).


python3 cli/compressor_cli.py



Dépendances

    tqdm

    inquirer

    colorama


pip install tqdm inquirer colorama



Exemple de sortie (--verbose)


[INFO] Lecture du fichier test.txt...
[INFO] Nombre de blocs : 127
[DEBUG] Premier bloc : ATGCGT...
[DEBUG] Référence utilisée : ATGCGT...
[DEBUG] Nombre de gènes uniques : 12
[INFO] Encodage des mutations...
Encodage mutation : 100%|████████| 127/127 [00:00<00:00, 130000.00 bloc/s]
[INFO] Compression finale...
[SUCCÈS] Compression réussie : 'test.txt' -> 'output.dna'
[FIN] Durée totale de compression : 0.03 secondes


