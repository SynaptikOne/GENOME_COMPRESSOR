# tests/test_genome_decoder.py


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
Tests unitaire pour le module genome_decoder.py.

Ce fichier vérifie la capacité du décodeur à :
- Reconstruire une séquence à partir d'un fichier .dna
- Appliquer correctement différents types de mutations (substitution, insertion, suppression)
- Gérer les cas sans mutation ou avec mutation invalides

Auteur              : Rakotondravelo Tahina Mickaël



EN:
Unit tests for the genome_decoder.py module.

This file verifies the decoder's ability to:
- Reconstruct a sequence from a .dna file
- Correctly apply different types of mutation (substitution, insertion, deletion)
- Handle cases without mutation or with invalid mutation


Author               : Rakotondravelo Tahina Mickaël
"""

import pytest
from src.genome_decoder import GenomeDecoder
from src.storage_model import StorageModel

@pytest.fixture
def sample_dna_data():
    return {
        "genes": {"G0": "ACGTACGT"},
        "blocks": [
            {"gene": "G0", "mutation": None},          # bloc sans mutation
            {"gene": "G0", "mutation": "sub_2_T"}     # bloc avec mutation
        ],

        "metadata": {
            "original_length": 16,
            "block_size": 8,
            "format_version": "1.0"
        }
    }

def test_decode_sequence(sample_dna_data):
    for block in sample_dna_data["blocks"]:
        if block["mutation"] is None:
            block["mutation"] = "-"
    result = GenomeDecoder.decode(sample_dna_data)
    assert result.startswith("ACGTACGT")
    


def test_decode_from_file(tmp_path , sample_dna_data):
    for block in sample_dna_data["blocks"]:
        if block["mutation"] is None:
            block["mutation"] = "-"
    file_path = tmp_path / "test_file.dna"
    StorageModel.save(sample_dna_data, str(file_path))
    decoded = GenomeDecoder.decode_from_file(str(file_path))
    assert isinstance(decoded, str)
    


def test_decode_with_dash_mutation():
    data = {
        "genes": {"G0": "ACGTACGT"},
        "blocks": [{"gene": "G0", "mutation": "-"}],
        "metadata": {}
    }

    result = GenomeDecoder.decode(data)
    assert result == "ACGTACGT"


def test_decode_with_insertion():
    data = {
        "genes": {"G0": "ACGT"},
        "blocks": [{"gene": "G0", "mutation": "Ins_2_T"}],
        "metadata": {}
    }

    result = GenomeDecoder.decode(data)
    assert result == "ACTGT"


def test_decode_with_deletion():
    data = {
        "genes": {"G0": "ACGT"},
        "blocks": [{"gene": "G0", "mutation": "Del_2"}], # ACGT -> AC_T
        "metadata": {}
    }
    result = GenomeDecoder.decode(data)
    assert result == "ACT"


def test_decode_with_combined_mutations():
    data = {
        "genes": {"G0": "ACGTAC"},
        "blocks": [{"gene": "G0", "mutation": "Mut_2_T|Del_4"}], # -> ACTT_C
        "metadata": {}
    }

    result = GenomeDecoder.decode(data)
    assert result == "ACTTC"


def test_decode_with_invalide_mutation():
    data = {
        "genes": {"G0": "ACGT"},
        "blocks": [{"gene": "G0", "mutation": "Mut_X_Y"}], # Invalide, ignorée
        "metadata": {}
    }

    result = GenomeDecoder.decode(data)
    assert result == "ACGT" # L'instruction est ignoree


if __name__ == "__main__":
    pytest.main()
