#src/storage_model.py

#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licences/MIT
#------------------------------------------------------------------------------

"""

FR:
Module responsable de la sérialisation et désérialisation des fichier .dna
dans un format JSON versionné et portable.

Auteur                : Rakotondravelo Tahina Mickaël


EN:
Module respnsible for serialization and deserialization of .dna files using a versioned,
structured, and portable JSON format.

Author                : Rakotondravelo Tahina Mickaël
"""

import json
from typing import Any
from datetime import datetime

class StorageModel:
    """
    FR:
    Classe pour la gestion des fichier .dna (sauvegarde et lecture).

    Attributs:
       version (str): Version actuelle du format de fichier .dna

    EN:
    Class for managing .dna files (saving and loading)
    Attributes:
       version (str): Current version of the .dna file format
    """

    version = "1.0"
    generator_name = "GENOME_COMPRESSOR"
    generator_version = "1.0.0"
    author = "Rakotondravelo Tahina Mickael"

    @staticmethod
    def save(data: dict, filename: str, source_filename: str = "") -> None:
        """
        FR:
        Enregistre les données compressées dans un fichier .dna au format JSON.

        Args:
           data (dict): Données compressées contenant 'genes', 'blocks' et 'metadata'.

           filename (str): Nom du fichier de sortie (avec extension .dna)

        Raises:
           ValueError: Si les données ne contiennent pas les clés attendues.

        EN:
        Saves the compressed data into a .dna file in JSON format.
        Args:
          data (dict): Compressed data containing 'genes', 'blocks', and 'metadata'.

          filename (str):Output file name (with .dna extension)
        
        Raises:
           ValueError : If data does not contain the required keys.
        """

        required_keys = {"genes", "blocks", "metadata"}
        if not required_keys.issubset(data.keys()):
            raise ValueError("Le fichier .dna doit contenir les clés : 'genes', 'blocks', 'metadata'.")
        

        metadata = data["metadata"]
        metadata["format_version"] = StorageModel.version
        metadata["created_at"] = datetime.now().isoformat()
        metadata["author"] = StorageModel.author
        metadata["generator"] = StorageModel.generator_name
        metadata["generator_version"] = StorageModel.generator_version

        if source_filename:
            metadata["source_filename"] = source_filename
        
        

        with open(filename, "w") as f:
            json.dump(data, f, indent=3)

    @staticmethod
    def load(filename: str) -> dict:
        """
        FR:
        Charge un fichier .dna et retourne les données compressées.

        Args:
           filename (str): Nom du fichier à lire.
        
        Returns:
           dict: Données compresssées chargées.

        Raises:
          ValueError: Si le fichier ne contient pas les champs requis.

        EN:
        Loads a .dna file and returns the compressed data.
        Args:
           filename (str): Name of the file to read.
        
        Returns:
          dict: Loaded compressed data.

        Raises:
          ValueError: If the file is invalid or corrupted      
        """

        with open(filename, "r") as f:
            data = json.load(f)

        required_keys = {"genes", "blocks", "metadata"}
        if not required_keys.issubset(data.keys()):
            raise ValueError("Le fichier .dna est invalide ou corrompu.")
        
        return data
    

if __name__ == "__main__":
    # Données de test unitaire
    dummy_data = {
        "genes": {"G0": "ACGTACGT"},
        "blocks": [{"gene": "G0", "mutation": "Mut_0_A"}],
        "metadata": {"original_length": 8, "block_size": 4}
    }

    # Sauvegarde test
    filename = "test_output.dna"
    StorageModel.save(dummy_data, filename)
    print(f"Fichier suavegarde sous : {filename}")

    # Chargement test
    loaded = StorageModel.load(filename)
    print("contenu charge :", loaded)