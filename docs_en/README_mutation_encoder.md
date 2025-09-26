#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# Licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licenses/MIT
#------------------------------------------------------------------------------

# `mutation_encoder.py` - Mutation Encoder for DNA Sequences

---

## Description

The `mutation_encoder` module provides a set of functions to detect, encode, decode, and apply mutations in DNA sequences.  
It facilitates compression, comparison, and transformation of genomic data.

---

## Main Features

- Encoding differences between a sequence and a reference.
- Decoding mutations to reconstruct a mutated sequence.
- Comparing blocks of sequences to detect mutations.
- Generating a list of mutations position by position.

---

### Mutation Representation

Mutations are represented in the following format:

`Mut_<position>_<new_base>`

Identical positions are represented as `"-"`.

---

## Available Functions

### `encode_mutation(seq: str, ref: str) -> str`

Encodes the differences between `seq` and `ref` as a mutation string.

**Example:**

```python
encode_mutation("ACCTACGA", "ACGTACGT")
# Result: "-,-,Mut_2_C,-,-,-,-,Mut_7_A"


compare_blocks(block1: str, block2: str) -> str

Compares two DNA blocks and returns the mutation string between them.

Example:

compare_blocks("GATTACA", "GATCACC")
# Result: "-,-,-,Mut_3_C,-,-,Mut_6_C"


apply_mutation(original: str, mutation_code: str) -> str

Applies encoded mutations to the original sequence.

Example:


apply_mutation("ACGTACGT", "-,-,Mut_2_C,-,-,-,-,Mut_7_A")
# Result: "ACCTACGA"



encode_mutations_in_sequence(seq: str, ref: str) -> List[str]

Returns a list of mutations between two sequences.

Example:


encode_mutations_in_sequence("TTAGCCAT", "TTGGCCAA")
# Result: ['-', '-', 'Mut_2_A', '-', '-', '-', 'Mut_6_A', 'Mut_7_T']


decode_mutation(original: str, mutation_code: str) -> str

Reconstructs a mutated sequence from a mutation string.

Example:


decode_mutation("ACGTACGT", "-,-,Mut_2_C,-,-,-,-,Mut_7_A")
# Result: "ACCTACGA"



Mutation Format Summary

    Mutation: Mut_<index>_<base>

    No change: "-"

    Indexing: zero-based (starts from 0)


Requirements

    Python 3.6 or higher

    No external libraries required

License

This project is licensed under the MIT License.
See the LICENSE file for more information.


