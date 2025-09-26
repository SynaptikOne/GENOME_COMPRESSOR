## License

This project is licensed under the MIT License - see the [`LICENSE_EN`] (LICENSE_EN) fole for details.

Note : This project includes an unofficial French translation of the MIT License (file `LICENSE_FR`). The english version (`LICENSE_EN`) remains the legally binding one.


# GENOME_COMPRESSOR
[![License : MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**A bio-inspired DNA compression system written in Python.**

## Description
`GENOME_COMPRESSOR` is a modular Python tool for compressing and decompressing DNA sequences using pattern repetition, gene encoding, and mutation modeling.

It transforms raw DNA strings into structured, minimized `.dna` files with reversible encoding.

## Features

- Pattern detection via sliding window scanning
- Gene reference selection and block matching
- Lightweight mutation encoding (substitution, insertion, deletion)
- Full decompression to original sequence
- JSON `.dna` format with metadata
- MIT License, bilingual comments (FR/EN)


## Modules
- `PatternScanner`  : identifies repeated DNA motifs
- `GeneEncoder`     : builds a gene dictionary
- `MutationEncoder` : detects differences between blocks and references
- `GenomeCompressor`: orchestrates compression
- `GenomeDecoder`   : reconstructs the original sequence
- `StorageModel`    : handles .dna serialization

## Installation

```bash
git clone https://github.com/DARKPHEX/GENOME_COMPRESSOR.git 
cd GENOME_COMPRESSOR
python3 main.py # GENOME_COMPRESSOR
"# GENOME_COMPRESSOR" 
