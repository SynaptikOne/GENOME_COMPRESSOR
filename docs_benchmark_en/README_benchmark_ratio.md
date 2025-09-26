#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# licensed under the MIT License. You may obtain a copy of the Licence at:
# https://opensource.org/licences/MIT
#------------------------------------------------------------------------------





# Benchmark: Compression Ratio (`benchmark_compression_ratio.py`)

## Objective

This script measures the **compression ratio** achieved by the `GENOME_COMPRESSOR` project. It applies DNA encoding to all text files (`.txt`) found in the `test_performance` directory and records the following results:

- Original file size
- Compressed file size (`.dna`)
- Compression ratio (`compressed_size / original_size`)
- Processing time (in seconds)

---

## Usage

Run the script:
```bash
python benchmark/benchmark_compression_ratio.py