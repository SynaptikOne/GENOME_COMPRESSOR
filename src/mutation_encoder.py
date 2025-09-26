# src/mutation_encoder.py

#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licences/MIT
#------------------------------------------------------------------------------


SEPARATOR = "|" # Séparateur plus sûr que la virgule pour les mutations

class MutationEncoder:
    """
    FR:
    Class responsable de l'encodage des mutations entre les blocs similaires d'ADN
    Elle compare deux séquences (originale et modifiée) et encode les différences:
    - Substitution : Mut_i_X
    - Insertion    : Ins_i_X
    - Suppression  : Del_i

    Auteur            : Rakotondravelo Tahina Mickaël


    EN:
    Class responsible for encoding mutations between similar DNA blocks.
    It compares two sequence (original and modified) and encodes the differences:

    - Substitution : Mut_i_X
    - Insertion    : Ins_i_X
    - Deletion     : Del_i

    Author               : Rakotondravelo Tahina Mickaël
    """ 
    def __init__(self):
        """
        
        FR : Initialise un objet MutationEncoder.
        EN : Initializes a MutationEncoder object.
        """
        # Variables à définir selon la logique du projet
        # Aucune donnée specifique à initialiser pour l'instant
        pass

    def encode_mutation(self, gene_sequence, reference_gene_sequence):
        """
        FR:
        Encode les mutations entre la séquence génétique donnée et une séquence  de référence
        
        Paramètres:
        - gene_sequence (str): La séquence d'ADN à encoder.
        - reference_gene_sequence (str): La séquence d'ADN de référence à comparer.

        Retour:
        -str: La séquence codée représentant les mutations.(ex: les indices des différences)

        EN:
        Encodes the mutations between a given DNA sequence and a reference sequence.

        Parameters:
        - gene_sequence (str): DNA sequence to encode.
        - reference_gene_sequence (str) : Reference DNA sequence.

        Returns:
        - str: Encoded muation string (e.g., mutation indices)
        """
        mutations = []
        len_ref = len(reference_gene_sequence)
        len_seq = len(gene_sequence)
        i = j = 0

        while i < len_ref or j < len_seq:
            if i < len_ref and j < len_seq:
                if reference_gene_sequence[i] != gene_sequence[j]:
                    mutations.append(f"Mut_{i}_{gene_sequence[j]}")

                else:
                    mutations.append("-")

                i += 1
                j += 1
            
            elif i < len_ref:
                mutations.append(f"Del_{i}")
                i +=1
            elif j < len_seq:
                mutations.append(f"Ins_{i}_{gene_sequence[j]}")
                j += 1
                i += 1    # Pour garder une cohérence d'index croissant
        
        return SEPARATOR.join(mutations)
        
        
               
          

    def compare_blocks(self, block1, block2):
        """
        FR:
        Compare deux blocs génétiques et retourne les mutations nécessaire pour transformer block1 en block2

        Paramètres:
        - block1 (str): Bloc source (original).
        - block2 (str): Bloc cible (modifié)

        Retour:
        - str: Mutations nécessaires (au format encode-mutation)

        EN:
        Comapres two genetic blocks and returns the mutations required to transform 
        block1 into block2

        Parameters:
        - block1 (str): Source block.
        - block2 (str): Target block.

        Returns:
        - str: Required mutations in encoded format.
        """
        return self.encode_mutation(block2, block1)  # Inversé exprès: transforme block1 -> block2

    def apply_mutation(self, original_sequence, mutation_sequence):
        """
        FR:
        Applique une mutation à une séquence d'ADN.

        Paramètres:
        - original_sequence (str): La séquence de base (référence).
        - mutation_sequence (str): La séquence de  mutations (ex: "Mut_2_a,Ins_3_,).
        pour remplacer le 1er caractere par 'c').

        Retour:
        - str: La séquence modifiée après  mutation.

        EN:
        Applies a mutation to a DNA sequence

        Parameters:
        - original_sequence (str): Reference DNA sequence.
        - mutation_sequence (str): Mutation sequence (e.g./ "Mut_2_a", "Ins_3_c").

        Returns:
        - str: Modified DNA sequence
        """

        sequence = list(original_sequence)
        mutations = mutation_sequence.split(SEPARATOR)
        

        offset = 0  # Pour suivre le déplacement causé par insertions/suppressions

        for m in mutations:
            if m == "-":
                continue
            elif m.startswith("Mut_"):
                try:
                    _, idx_str, new_char = m.split("_", maxsplit=2)
                    idx = int(idx_str) + offset
                    if 0 <= idx < len(sequence):
                        sequence[idx] = new_char
                except ValueError:
                    continue # Mutation mal formée, on ignore
            elif m.startswith("Ins_"):
                try:
                    _, idx_str, char = m.split("_", maxsplit=2)
                    idx = int(idx_str) + offset
                    sequence.insert(idx, char)
                    offset += 1
                except ValueError:
                    continue
            elif m.startswith("Del_"):
                try:
                    _, idx_str = m.split("_", maxsplit=1)
                    idx = int(idx_str) + offset
                    if 0 <= idx < len(sequence):
                        sequence.pop(idx)
                        offset -= 1
                except ValueError:
                    continue
        return "".join(sequence)
                
            

    def find_closest_gene(self, new_sequence, known_genes, max_mutations=3):
        """
        FR:
        Cherche dans les gènes connus celui qui est le plus proche (par mutation)
        du bloc cible.

        Parametres:
        - new_sequence (str): la bloc à encoder.
        - known_genes (dict): dictionnaire {gene_id: séquence}
        - max_mutation (int): seuil minimum de mutations autorisé.

        Retour:
        - Tuple (gene_id, encoded_mutation) si un gène proche est trouvé, sinon (None,None)


        EN:
        Searches for the closest known gene to the target block, based on mutation count.

        Parameters:
        - new_sequence (str): Block to encode
        - known_genes (dict): Dictionary {gene_id: sequence}
        - max_mutations (int): Maximum allowed mutations.
        

        Returns:
        - Tuple (gene_id, encoded_muation) or (None, None)
        """
        for gene_id, gene_seq in known_genes.items():
            mutation_str = self.encode_mutation(new_sequence, gene_seq)
            mutations = mutation_str.split(SEPARATOR)
            num_real_mutations = sum(1 for m in mutations if m != "-")
            if num_real_mutations <= max_mutations:
                return gene_id, mutation_str
        return None, None
          
    def encode_mutations_in_sequence(self, sequence, reference_sequence):
        """
        FR:
        Encode toutes les mutations dans une séquence ADN complète par rapport à une séquence de référence
        

        Paramètres:
        - sequence (str): La séquence cible.
        - reference_sequence (str): La séquence de référence.

        Retour:
        - List[str]: Liste des mutations encodées pour chaque position.


        EN:
        Encodes all mutations between a DNA sequence and a reference.

        Parameters:
        - sequence (str): Target DNA sequence.
        - reference_sequence (str): Reference DNA sequence

        Rerurns:
        - List[str]: List of encoded mutations
        """

        return self.encode_mutation(sequence, reference_sequence).split(SEPARATOR)
        

    def decode_mutation(self, original_sequence, encoded_mutation):
        """
        FR:
        Décode une séquence mutée à partir d'une séquence originale et d'une mutation encodée.

        EN:
        Decode a mutated sequence from an original sequence and and encoded muation.

        Alias of apply_mutation for compatibility
        """
        return self.apply_mutation(original_sequence, encoded_mutation)
