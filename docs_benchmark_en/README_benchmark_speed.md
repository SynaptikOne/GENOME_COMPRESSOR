#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# licensed under the MIT License. You may obtain a copy of the Licence at:
# https://opensource.org/licences/MIT
#------------------------------------------------------------------------------




# Benchmark: Processing Speed (`benchmark_speed.py`)

## Objective

This script measures the **compression and decompression speed** of the `GENOME_COMPRESSOR` project by testing all `.txt` files in the `test_performance/` folder.

It provides:
- Compression time (in seconds)
- Decompression time 
- An interpretation comment on the relative speed of both phases

---

## Usage

Run the script:
```bash
python benchmark/benchmark_speed.py