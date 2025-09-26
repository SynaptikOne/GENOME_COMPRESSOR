#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# Licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licenses/MIT
#------------------------------------------------------------------------------

# MODULE `pattern_scanner.py`

---

## Description

This module provides a `PatternScanner` class for identifying **frequent patterns** within a character string.  
It is designed to be useful in bio-inspired compression systems or textual data analysis tasks.

---

## Features

- Pattern search with variable lengths (`min_length`, `max_length`)  
- Filtering by minimum frequency (`min_frequency`)  
- Two available algorithms:
  - `naive`: exhaustive method, reliable for all lengths  
  - `rabin-karp`: faster method, but limited to fixed lengths  
- Automatic fallback to `naive` if `rabin-karp` fails  

---

## Example Usage

```python
from pattern_scanner import PatternScanner

data = "bonjourbonjourbonsoirbonjour"

scanner = PatternScanner(min_length=6, max_length=6, min_frequency=2)
result = scanner.scan(data)
print(result)
# Output: {'bonjour': 3, 'onjour': 3, ...}


Internal Structure

    PatternScanner: main class

    _scan_naive: brute-force implementation

    _scan_rabin_karp: optimized version using hashing

    Automatic fallback management if one method fails


Tests

The module is tested using pytest in tests/test_pattern_scanner.py.

Command to run tests:


pytest tests/test_pattern_scanner.py



Future Improvements

    Memory optimization for very large files

    Direct integration into the compression pipeline