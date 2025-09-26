#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# Licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licenses/MIT
#------------------------------------------------------------------------------

# `genome_compressor.py`

---

## Overview

This module is the core of the **GENOME_COMPRESSOR** system.  
It orchestrates the bio-inspired encoding of a DNA sequence using a modular approach based on:

- fixed-size **blocks**,  
- frequent **patterns** (genes),  
- and **mutations** between sequences.

---

## Features

- Splits a sequence into fixed-size blocks.  
- Detects the most frequent patterns within these blocks.  
- Encodes these patterns as **reference genes**.  
- Encodes blocks as **mutations** relative to the genes.  
- Exports the compressed result to a `.dna` file in JSON format.

---

## Usage example

```python
from src.genome_compressor import GenomeCompressor

sequence = "AAATTTGTGTCCCAAATTAG"
compressor = GenomeCompressor(block_size=8)
compressed = compressor.compress(sequence)
compressor.save_to_dna(compressed, "output.dna")


Format of the .dna file


{
    "genes": {
        "G0": "ATGC...",
        ...
    },
    "blocks": [
        {
            "gene": "G1",
            "mutation": "Mut_0_A,Mut_1_C,..."
        },
        ...
    ],
    "metadata": {
        "original_length": 32,
        "block_size": 8
    }
}



Dependencies

    pattern_scanner.py

    gene_encoder.py

    mutation_encoder.py


Tests

Unit tests are available in the tests/ folder.
The main test module is:



tests/test_genome_compressor.py


It can be run with the following command:

pytest tests/test_genome_compressor.py


