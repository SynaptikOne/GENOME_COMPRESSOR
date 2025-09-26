#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# Licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licenses/MIT
#------------------------------------------------------------------------------

# `compressor_cli.py` - CLI Interface for GENOME_COMPRESSOR

## Overview

**GENOME_COMPRESSOR** is a DNA sequence compression tool inspired by biological mechanisms.  
The module `compressor_cli.py` provides a user-friendly command-line interface to compress and decompress files.

---

## Available Commands

```bash
python3 cli/compressor_cli.py <command> [arguments] [options]


 1.   compress

Description: Compresses a text file containing a DNA sequence into a .dna file.

Syntax:


python3 cli/compressor_cli.py compress <input_file> -o <output_file> [--verbose]


Arguments:

    <input_file>: path to the text file containing raw DNA.

    -o, --output: output .dna file (default: output.dna).

    --verbose: displays additional information (blocks, mutations, references, etc.)

Example:


python3 cli/compressor_cli.py compress data/adn.txt -o result.dna


 2.   decompress

Description: Decompresses a .dna file into a raw DNA sequence.

Syntax:

python3 cli/compressor_cli.py decompress <input_file> -o <output_file> [--verbose]



Arguments:

    <input_file>: path to the .dna file to decompress.

    -o, --output: text file containing the reconstructed sequence (default: reconstructed.txt).

    --verbose: displays size, initial JSON data, etc.

Example:


python3 cli/compressor_cli.py decompress result.dna -o reconstruction.txt --verbose



 3.   about

Description: Displays general information about the project, modules, and author.

Command:

python3 cli/compressor_cli.py about



Other options

    --version: displays the tool version and author name.


python3 cli/compressor_cli.py --version



Running without arguments opens an interactive interface (menu navigable via arrow keys/keyboard).


python3 cli/compressor_cli.py


Dependencies

    tqdm

    inquirer

    colorama

Install them via pip:


pip install tqdm inquirer colorama


Example output (--verbose)

[INFO] Reading file test.txt...
[INFO] Number of blocks: 127
[DEBUG] First block: ATGCGT...
[DEBUG] Reference used: ATGCGT...
[DEBUG] Number of unique genes: 12
[INFO] Encoding mutations...
Mutation encoding: 100%|████████| 127/127 [00:00<00:00, 130000.00 blocks/s]
[INFO] Final compression...
[SUCCESS] Compression succeeded: 'test.txt' -> 'output.dna'
[END] Total compression time: 0.03 seconds







