# src/genome_compressor.py

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
Module principal pour la compression d'une séquence génomique en utilisant des motifs
fréquents, un encodage ADN, et une stratégie de mutations minimales


Auteur             : Rakotondravelo Tahina Mickaël


EN:
Main module for compressing a genomic sequence

Uses a block-based approach, frequent pattern detection
DNA-like encoding, and a minimal-mutation strategy.

Author               : Rakotondravelo Tahina Mickaël
"""

import json
from src.pattern_scanner import PatternScanner
from src.gene_encoder import GeneEncoder
from src.mutation_encoder import MutationEncoder



class GenomeCompressor:
    """
    FR:
    Compresseur de séquences génomiques utilisant des motifs féquents et des mutations.

    EN:
    Genomic sequence compressor using frequent motifs and mutation encoding
    """
    def __init__(self, block_size: int = 8):
        """
        FR:Initialise le compresseur avec une taille de bloc donnée.
        
        EN: Initialize the compressor with a given block size.
        """
        self.block_size = block_size
        self.pattern_scanner = PatternScanner(min_length=block_size, max_length=block_size)
        self.gene_encoder = GeneEncoder()
        self.mutation_encoder = MutationEncoder()

    def compress(self, raw_sequence: str) -> dict:
        """
        FR:
        Compresse une séquence brute d'ADN.

        Paramètres:
        - raw_sequence (str): La séquence ADN originale 
        Retour:
        - dict: Données compressées incluant les gènes, mutations, et métadonnées.


        EN: Compress a raw DNA sequence.
        Parameters:
        - raw_sequence (str): Original DNA sequence.
        Returns:
        - dict: Compressed data including genes, mutations, and metadata.
        """
        # Etape 1 : découper en blocs
        blocks = self.pattern_scanner.split_into_blocks(raw_sequence)

        # Etape 2 : détecter motifs fréquents (ici, on choisit top 5 motifs les plus fréquents)
        top_patterns = self.pattern_scanner.find_frequent_patterns(blocks, top_k=5)

        # Fallback : si aucun motif fréquent n'est trouvé, prendre les premiers blocs comme motifs
        if not top_patterns:
            top_patterns = blocks[:min(5, len(blocks))]

        # Etape 3 : encoder les motifs en ADN (base des gènes)
        genes = {
            f"G{i}": self.gene_encoder.encode_motif(pattern)
            for i, pattern in enumerate(top_patterns)
        }

        # Etape 4 : encoder chaque bloc par mutation par rapport au gène le plus proche
        compressed_blocks = []
        max_allowed_mutations = self.block_size // 2

        for block in blocks:
            # Cherche un gène existant proche avec peu de mutations
            gene_id, mutation_str = self.mutation_encoder.find_closest_gene(
                block, genes, max_mutations=max_allowed_mutations
            )
            if gene_id is not None:
                compressed_blocks.append({
                    "gene": gene_id,
                    "mutation": mutation_str
                })
            else:
                # Aucun gène proche : ajouter comme nouveau gène dynamique
                gene_id = f"G_dyn_{len(genes)}"
                genes[gene_id] = block
                compressed_blocks.append({
                    "gene": gene_id,
                    "mutation": "-"
                })
    
        # Etape 5 : retourner les données compressées
        return {
            "genes": genes,
            "blocks": compressed_blocks,
            "metadata": {
                "original_length": len(raw_sequence),
                "block_size": self.block_size,
                "format_version": "1.0"
            }
        }

    def save_to_dna(self, compressed_data: dict, filename: str) -> None:

        """
        FR:
        sauvegarde les données compressées dans un fichier au format .dna (JSON).

        Paramètres:
        - compressed_data (dict): Données compressées à sauvegarder
        - filename (str): Nom du fichier de sortie

        EN:
        Saves compressed data tp a .dna (JSON) file.
        Parameters:
        - compressed_data (dict): Data to save.
        - filename (str): Output filename
        """
        with open(filename, "w") as f:
            json.dump(compressed_data, f, indent=2)


if __name__ == "__main__":
    # Exemple rapide d'utilisation
    seq = "ACGTACGTACGTACGTACGTACGTACGTACGT"
    compressor = GenomeCompressor(block_size=8)
    compressed = compressor.compress(seq)
    compressor.save_to_dna(compressed, "output.dna")
    print(json.dumps(compressed, indent=2))