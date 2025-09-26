# tests/test_storage_model.py

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
Test unitaires pour le module storage_model.py

Ce fichier vérifie le capacité à :
- Sauvegarder et recharger un fichier .dna valide
- Gérer les erreurs de JSON invalide
- Détecter l'abscence de clés obligatoires
- Enregistrer le nom du fichier source dans les métadonnées


Auteur                   : Rakotondravelo Tahina Mickaël


EN:
Unit tests for the storage_model.py module

This file verifies the ability to:
- Save and reload a valid .dna file
- Handle errors from invalid JSON
- Detect missign required keys
- Record the source filename in metadata

Author                   : Rakotondravelo Tahina Mickaël
"""

import os
import json
import pytest
from src.storage_model import StorageModel

@pytest.fixture
def sample_data():
    """
    FR: Fixture retournant un jeu de données compressées valide.
    EN: Fixture returning a valid compressed data sample.
    """
    return {
        "genes": {"G0": "ACGTACGT"},
        "blocks": [{"gene":"G0", "mutation": "Mut_0_A"}],
        "metadata": {
            "original_length": 8,
            "block_size": 4,
            "format_version": "1.0"
        }
    }

def test_save_and_load_dna_file(tmp_path, sample_data):
    """
    FR: Teste la capacité à sauvegarder et recharger un fichier .dna
    EN: Tests the ability to save and reload a .dna file
    """
    file_path = tmp_path / "test_output.dna"

    # Test sauvegarde
    StorageModel.save(sample_data, str(file_path))
    assert file_path.exists(), "Le fichier .dna n'a pas été créé."

    # Test lecture
    loaded_data = StorageModel.load(str(file_path))
    assert isinstance(loaded_data, dict), "Les données lues ne sont pas un dictionnaire."
    assert loaded_data == sample_data, "Les données lues ne correspondent pas aux donnes initiales."


def test_invalid_json(tmp_path):
    """
    FR: Vérifie qu'un JSOn invalide génère une exception.
    EN: Checks that invalid JSON raises an exception
    """
    file_path = tmp_path / "invalid.dna"
    file_path.write_text("{invalid_json: true,}") # contenu JSON invalide / invalid JSON

    with pytest.raises(json.JSONDecodeError):
        StorageModel.load(str(file_path))


def test_save_with_missing_keys(tmp_path):
    """
    FR: Vérifie que la sauvegarde échoue si des clés obligatoires manquent.
    EN: Checks that saving fails if required keys are missing.
    """
    # Donnees incomplète (manque 'blocks')
    bad_data = {
        "genes": {"G0": "ACGT"},
        "metadata": {"original_length": 4}
    }
    file_path = tmp_path / "bad_output.dna"
    with pytest.raises(ValueError, match="doit contenir les clés"):
        StorageModel.save(bad_data, str(file_path))


def test_load_with_missing_keys(tmp_path):
    """
    FR: Vérifie que le chargement échiue si les clés attendues sont absentes.
    EN: Checks that loading fails if required keys are missing
    """
    file_path = tmp_path / "incomplete.dna"
    # JSON valide mais sans les clés requises
    file_path.write_text(json.dumps({"genes": {}, "blocks": []}))
    with pytest.raises(ValueError, match="invalide ou corrompu"):
        StorageModel.load(str(file_path))


def test_save_with_source_filename(tmp_path, sample_data):
    """
    FR: Vérifie que le nom du fichier source est bien enregistré dans les métadonnées
    EN: Checks that the source filename is correctly saved in metadata
    """
    file_path = tmp_path / "with_source.dna"
    StorageModel.save(sample_data, str(file_path), source_filename= "input.txt")
    loaded = StorageModel.load(str(file_path))
    assert "source_filename" in loaded["metadata"]
    assert loaded["metadata"]["source_filename"] == "input.txt"