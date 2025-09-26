#src/genome_decoder.py

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
genome_decoder.py

FR:
Module responsable de la reconstitution d'une séquence ADN originale à partir d'un fichier
compressé `.dna` contenant les gènes, les blocs et les mutations.

Auteur               : Rakotondravelo Tahina Mickaël


EN:
Module responsible for reconstructing the original DNA sequence from a compressed `.dna` file
containing genes, blocks, and mutations.

Author               : Rakotondravelo Tahina Mickaël               : 
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from typing import Dict, List
from src.storage_model import StorageModel

SEPARATOR = "|"


class GenomeDecoder:
    """

    FR:
    Classe pour décoder une séquence ADN compressée à partir d'un fichier `.dna`.

    Méthodes :
       decode(data: dict) -> str: Reconstitue la séquence ADN originale.

       decode_from_file(filename: str) -> str : lit un fichier .dna et décode la séquence
    EN:
    Class for decoding a compressed DNA sequence from a `.dna` file.

    Methods:
       decode(data: dict) -> str: Reconstructs the original DNA sequence.
       decode_from_file(filename: str) -> str: Reads a .dna file and decodes the sequence
    """

    @staticmethod
    def decode(data: Dict) -> str:
        """

        FR:
        Reconstitue la séquence ADN originale à partir des blocs, gènes et mutations.

        Args:
           data (dict): Données chargées depuis un fichier .dna
        
        Returns:
           str: Séquence ADN originale reconstituée

        EN:
        Reconstructs the original DNA sequence from blocks, genes, and mutations.

        Args:
          data (dict): Data loaded from a .dna file

        Returns:
          str: Reconstructed original DNA sequence
        """

        genes = data["genes"]
        blocks = data["blocks"]

        sequence_parts : List[str] = []

        for block in blocks:
            gene_seq = genes[block["gene"]]
            mutation = block["mutation"]
            

            if not any(x.strip().startswith(("Mut_", "Ins_", "Del_")) for x in mutation.split(SEPARATOR)):
                sequence_parts.append(gene_seq)

            else:
                # Traitement basique placeholder - à adapter selon ton format réel des mutations

                mutated_seq = GenomeDecoder.apply_mutation(gene_seq, mutation)

                sequence_parts.append(mutated_seq)
        
        return "".join(sequence_parts)
    
    @staticmethod
    def apply_mutation(gene_seq: str, mutation: str) -> str:
        """
        FR:
        Applique une mutation simple à une séquence
        Args:
            gene_seq (str): Séquence d'origine
            mutation (str): Description de la mutation

        Returns:
            str: Séquence mutée

        EN:
        Applies a simple mutation to a sequence.

        Args:
          gene_seq (str): Original sequence
          mutation (str): Mutation description
        
        Returns:
          str: Mutated sequence
        """

        # À adapter selon le format réel de mutation. Exemple fictif:
        # mutation = "sub_2_t" signifie "substituer" la base à l'indice 2 apr T"
        
        bases = list(gene_seq)

        mutations = mutation.split(SEPARATOR)

        offset = 0 # Pour suivre les décalages causés par insertions/suppressions
        
        for m in mutations:
            if m == "-":
                continue
            elif m.startswith("Mut_"):
                parts = m.split("_", maxsplit=2)
                if len(parts) == 3:
                    _, idx_str, new_base = parts
                    try:
                        idx = int(idx_str) + offset
                        if 0 <= idx < len(bases):
                            bases[idx] = new_base
                    except ValueError:
                        continue
            elif m.startswith("Ins_"):
                parts = m.split("_", maxsplit=2)
                if len(parts) == 3:
                    _, idx_str, char = parts
                    try:
                        idx = int(idx_str) + offset
                        if 0 <= idx <= len(bases):
                            bases.insert(idx, char)
                            offset += 1
                    except ValueError:
                        continue
            elif m.startswith("Del_"):
                parts = m.split("_", maxsplit=1)
                if len(parts) == 2:
                    _, idx_str = parts
                    try:
                        idx = int(idx_str) + offset
                        if 0 <= idx < len(bases):
                            bases.pop(idx)
                            offset -= 1
                    except ValueError:
                        continue
        return "".join(bases)
               



        

        
    
    @staticmethod
    def decode_from_file(filename: str) -> str:
        """
        FR:
        Lit un fichier .dna et retourne la séquence ADN reconstituée.

        Args: 
           filename (str): Chemin vers le fichier  .dna

        Returns:
           str: Séquence ADN originale

        EN:
        Reads a .dna file and returns the reconstructed DNA sequence.

        Args:
           filename (str): Path to the .dna file
        Returns:
           str: Original DNA sequence
        """

        data = StorageModel.load(filename)
        return GenomeDecoder.decode(data)
    

if __name__ == "__main__":
    # Démonstration basique

    decode_seq = GenomeDecoder.decode_from_file("test_output.dna")
    print("Séquence reconstruite :", decode_seq)