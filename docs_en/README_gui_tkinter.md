#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licences/MIT
#------------------------------------------------------------------------------



### `docs_en/README_gui_tkinter.md`

```markdown
# Graphical Interface - `gui_tkinter.py`

## Description

`gui_tkinter.py` provides a simple and intuitive graphical interface for the **GENOME_COMPRESSOR** project using Tkinter. It allows users to:

- Compress a `.txt` file into a `.dna` format
- Decompress a `.dna` file back to its original `.txt`
- View processing logs in real-time
- Enable/disable verbose mode
- View author and module information

## Features

- **Compression**: Reads a `.txt` file, encodes it in a DNA-inspired format, and saves it as `.dna`
- **Decompression**: Reads a `.dna` file, reconstructs the original text, and saves it as `.txt`
- **Verbose mode**: Displays internal process details in the log area
- **Log area**:  Real-time feedback with auto-scrolling
- **About window** : Information about the author and used modules

## Used Modules 
- `genome_compressor.py`
- `genome_decoder.py`
- `storage_model,py`
- `pattern_scanner.py`
- `gene_encoder.py`
- `mutation_encoder.py`


## Reqquirements

- Python >= 3.7
- Tkinter (bundled with Python)

## Run the application

```bash
python gui/gui_tkinter.py