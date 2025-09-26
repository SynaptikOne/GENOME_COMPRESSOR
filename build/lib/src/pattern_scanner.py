# src/pattern_scanner.py
#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licences/MIT
#------------------------------------------------------------------------------

"""
FR:
Détecte les motifs fréquents dans une chaîne selon une longueur minimale/maximale
et une fréquence minimale. Prend en charge deux méthodes :
- 'naive' (défaut, robuste pour toutes longueurs)
- 'rabin-karp' (plus rapide mais nécessite min_length == max_length)

si method=None, sélection automatique basée sur les paramètres.


Auteur                   :  Rakotondravelo Tahina Mickaël


EN:
Detects frequent patterns in a string besed on a minimum/maximum length and a 
minimum frequency. Supports two methods:

- 'naive' (default, robust for all lengths)
- 'rabin-karp' (faster but requires min_length == max_length)

If method=None, automatic method selection is applied.

Author                   : Rakotondravelo Tahina Mickaël
"""




from collections import defaultdict

class PatternScanner:
    def __init__(self, min_length=3, max_length=15, min_frequency=2,method=None):
        self.min_length = min_length
        self.max_length = max_length
        self.min_frequency = min_frequency
        
        if method is None:
            # Sélection automatique
            self.method = "rabin-karp" if min_length == max_length else "naive"

        else:
            method = method.lower()
            assert method in ["naive", "rabin-karp"], "Méthode non prise en charge."

            if method == "rabin-karp" and min_length != max_length:
                raise ValueError("Rabin-karp nécessite min_length == max_length.")
            self.method = method
    
    def scan(self, data):
        """
        FR:Analyse les données d'entrée pour détecter les motifs récurrents.

        :param data: Chaïne de caractères à analyser
        :return: Dictionnaire {motif:fréquence}

        EN: Analyze input data to detect recurring patterns.

        :param data: Input string to be analyzed
        :return    : Dictionary {pattern: frequency}
        """

        if self.method == "rabin-karp":
            try:
                return self._scan_rabin_karp(data)
            except Exception as e:
                print(f"[Alerte] Échec de Rabin-Karp ({type(e).__name__} : {e}), bascule vers 'naive'.")

                return self._scan_naive(data)
        else:
            return self._scan_naive(data)
        
        
        
        
    def _scan_naive(self, data):
        """
        FR: Méthode naïve pour scanner tous les motifs de tailles possibles.
        EN: Naive method to scan all patterns of possible sizes.
        """
        

        patterns = defaultdict(int)

        for size in range(self.min_length, self.max_length +1):
            for i in range(len(data) - size +1):
                chunk = data[i:i + size]
                patterns[chunk] += 1
        # Ne garder que les motifs fréquents
        filtered = {k: v for k, v in patterns.items() if v >= self.min_frequency}
        # Tri par fréquence décroissante
        
        return dict(sorted(filtered.items(), key=lambda x: -x[1]))
    
    def _scan_rabin_karp(self, data):
        """
        FR: Méthode Rabin-Karp optimisée pour une longueur fixe de motifs.
        EN: Optimized Rabin-Karp method for fixed-length pattern scanning.
        """
        base = 256
        prime = 101
        length = self.min_length
        n = len(data)
        patterns = defaultdict(int)

        if n < length:
            return {}
        
        h = pow(base, length - 1, prime)
        current_hash = 0
        hashes = defaultdict(list)

        # Hash initial
        for i in range(length):
            current_hash = (base * current_hash + ord(data[i])) % prime
        hashes[current_hash].append(0)

        for i in range(1, n -length +1):
            current_hash = (base * (current_hash - ord(data[i - 1]) * h) + ord(data[i + length - 1])) % prime
            current_hash = (current_hash + prime) % prime 
            hashes[current_hash].append(i)

        for positions in hashes.values():
            substrs_count = defaultdict(int)
            for pos in positions:
                substrs = data[pos:pos + length]
                substrs_count[substrs] += 1
            for k, v in substrs_count.items():
                if v >= self.min_frequency:
                    patterns[k] += v


        return dict(sorted(patterns.items(), key=lambda x: -x[1]))
    
    def split_into_blocks(self, sequence):
        """
        FR: Découpe la séquence en blocs de taille min_length (ou block_size).
        RN: Splits the sequence into blocks of size min_length.
        """


        blocks = [sequence[i:i + self.min_length] for i in range(0, len(sequence), self.min_length)]

        return blocks
        
    
    def find_frequent_patterns(self,blocks, top_k=5):
        """
        FR: Identifie les motifs les plus fréquents dans les blocs.
        
        :param blocks: Liste de sous-chaïnes
        :param top_k: Nombre maximum de motifs à retourner
        :return: Liste des motifs les plus fréquents

        EN: Identifies the most frequent patterns in the blocks.
        :param blocks: List of string blocks
        :param top_k: Maximum numbre of patterns to return.
        
        :return: List of the most frequent patterns
        """
        concatenated = ''.join(blocks)
        all_patterns = self.scan(concatenated)
        return list(all_patterns.keys())[:top_k]
    

# Exemple d'utilisation
if __name__ == "__main__":
    test_data = "bonjourbonjourbonsoirbonjour"

    # Mode  auto: choisit rabin-karp car min == max
    scanner_auto = PatternScanner(min_length=6, max_length=6, min_frequency=2)
    print("Mode auto :")
    for motif, freq in scanner_auto.scan(test_data).items():
        print(f"{motif}: {freq}")

    # Forçage méthode naïve
    scanner_naive = PatternScanner(min_length=6, max_length=6, min_frequency=2, method="naive")
    print("\nMode force naive :")
    for motif, freq in scanner_naive.scan(test_data).items():
        print(f"{motif}: {freq}")