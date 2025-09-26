# scr/gene_encoder.py


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
Module GeneEncoder

FR:
Transforme des motifs textuels en séquences ADN encodées (2 bits/base) et génère un dictionnaire de 
gènes optimisé pour la compression génomique

Fonctionnalités :
- Encodage texte -> ADN
- Construction de dictionnaire de gènes
- Encodage de séquences par référence aux gènes
- Décodage ADN -> texte

Auteur : Rakotondravelo Tahina Mickaël


EN:
Transforms textual patterns into encoded DNA sequences (2 bits/base) and builds a
gene dictionnary
optimized for genomic compression.

Features:
- Text to DNA encoding
- Gene dictionary construction
- Sequence encoding using gene references
- DNA to text decoding

Author                 : Rakotondravelo tahina Mickaël
"""

from typing import Dict, List


class GeneEncoder:
    """
    FR : Encodeur de motifs en séquences ADN (2 bits/base).
    EN : Encoder for converting text patterns into DNA sequence (2 bits par base)
    """

    def __init__(self):
        """
        FR : Initialise les tables de correspondance binaiare <-> ADN et les dictionnaires de gènes.

        EN : Initializes binary <-> DNA conversion tables and gene dictionaries.
        """
        

        self.binary_to_dna = {
            "00":"A",
            "01":"C",
            "10":"G",
            "11":"T"
        }
        self.dna_to_binary = {v: k for k, v in self.binary_to_dna.items()}
        self.gene_dict = {} # {gene_id: dna_sequence}
        self.reverse_dict = {} # {motif: gene_id}

    def _char_to_binary(self, char:str) -> str:
        """

        FR : Convertit un caractère en binaire 8 bits.
        
        EN : Converts a character to an 8-bits binary string.
        
        :param char: Caractére à encoder / Character to encode
        :return: Chaîne binaire / Binary / string"""
        return format(ord(char), "08b")
    
    def _binary_to_dna(self, binary_str: str) -> str:
        """
        FR : Convertit une chaîne binaire en séquence ADN (2 bits/base).

        EN : Converts a binary string into a DNA sequence (2 bits per base)

        :param binary_str: Chaîne binaire / Binary string
        :return: séquence ADN / DNA sequence
        """
        return ''.join(self.binary_to_dna[binary_str[i:i+2]] for i in range(0, len(binary_str),2))
    
    def encode_motif(self, motif: str) -> str:
        """
        
        FR : Encode un motif en une séquence ADN.
        
        EN : Encodes a textual motif into a DNA sequence.
        
        :param motif: Motif à encoder / Motif to encode
        :return: Séquence ADN encodée / Encoded DNA sequence
        """
        binary = ''.join(self._char_to_binary(c) for c in motif)
        return self._binary_to_dna(binary)
    
    def build_gene_dict(self, motifs: Dict[str, int]) -> Dict[str, str]:
        """

        FR : Construit un dictionnaire de gènes a partir de motifs fréquents.

        EN : Builds a gene dictionnary from frequent motifs.

        :param motifs: Dictionnaire {motis: fréquence} / Dictionary {motif: frequency}
        :return: Dictionnaire {gene_id: séquence ADN}  / Dictionary {gene_id: DNA sequence}
        """
        self.gene_dict = {}
        self.reverse_dict = {}

        for i, motif in enumerate(motifs):
            gene_id = f"gene{i+1}"
            dna_seq = self.encode_motif(motif)
            self.gene_dict[gene_id] = dna_seq
            self.reverse_dict[motif] = gene_id

        return self.gene_dict
    def encode_sequence(self, sequence: str, motifs: Dict[str, int]) -> List[str]:
        """

        FR : Encode une séquence complète en blocs  de gènes et texte brut.

        EN : Encodes a full sequence using gene references and raw text blocks.

        :param sequence: Séquence à encoder / Sequence to encode
        :param motifs: Dictionnaire des motifs / Motifs dictionary


        :return: Liste des blocs encodés (gènes ou texte) / List of encoded blocks (genes or raw text)
        """

        blocks = []
        i = 0
        motif_lengths = sorted({len(m) for m in motifs}, reverse=True)

        while i < len(sequence):
            matched = False
            for length in motif_lengths:
                chunk = sequence[i:i + length]
                if chunk in self.reverse_dict:
                    blocks.append(self.reverse_dict[chunk])
                    i += length
                    matched = True
                    break 
            if not matched:
                blocks.append(sequence[i])
                i += 1
        return blocks
    
    def decode_dna(self, dna_seq: str) -> str:
        """
        
        FR : Reconvertit une séquence ADN en texte brut.
        
        EN : Decodes a DNA sequence back into plain text.
        
        :param dna_seq: Séquence AND à décoder / DNA sequence to decode
        :return: Chaîne de texte / Text string"""
        binary_str = ''.join(self.dna_to_binary[base] for base in dna_seq)

        chars = [chr(int(binary_str[i:i+8], 2)) for i in range(0,len(binary_str),8)]

        return ''.join(chars)
    
if __name__ == "__main__":
    encoder = GeneEncoder()
    motif = "bio"
    dna = encoder.encode_motif(motif)
    print("Motif :", motif)
    print("ADN encodé :", dna)
    print("Décodé :", encoder.decode_dna(dna))