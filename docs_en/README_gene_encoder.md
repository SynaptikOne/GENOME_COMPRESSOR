#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# Licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licenses/MIT
#------------------------------------------------------------------------------

# Module `gene_encoder`

---

## Purpose of the module

The `gene_encoder` module transforms textual patterns into compressed DNA sequences using a binary encoding (2 bits/base).  
It is used in the genomic compression process to:

- Convert character strings (patterns) into encoded synthetic DNA.  
- Build a gene dictionary from frequent patterns.  
- Encode full sequences as gene identifiers to reduce redundancy.  
- Allow reconstruction (decoding) of DNA sequences back to the original text.

---

## Usage example

### 1. Encoding a pattern

```python
from src.gene_encoder import GeneEncoder

encoder = GeneEncoder()
dna = encoder.encode_motif("bio")
print(dna)  # Example output: "CAGTC.."



2. Building the gene dictionary


motifs = {"hello": 5, "world": 3}
gene_dict = encoder.build_gene_dict(motifs)
print(gene_dict)
# Output: {'gene1': '...', 'gene2': '...'}



3. Encoding a sequence using the genes


sequence = "helloworldhello"
encoded = encoder.encode_sequence(sequence, motifs)
print(encoded)
# Output: ['gene1', 'gene2', 'gene1']



4. Decoding DNA back to text


decoded = encoder.decode_dna(dna)
print(decoded)  # "bio"


Dictionary structure

Two internal dictionaries are used within GeneEncoder:

    .gene_dict


{
    "gene1": "ACGTTGCA",  # DNA sequence associated with the pattern
    "gene2": "CGGTAACC"
}


.reverse_dict


{
    "hello": "gene1",
    "world": "gene2"
}



