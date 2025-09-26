# cli/genome_crypto_cli.py


#------------------------------------------------------------------------------

# Copyright (c) 2025 Rakotondravelo Tahina Mickaël
# All rights reserved.
#
# This file is part of the GENOME_COMPRESSOR project.
#
# licensed under the MIT License. You may obtain a copy of the License at:
# https://opensource.org/licences/MIT
#------------------------------------------------------------------------------


import argparse
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from genome_crypto import genome_crypto


def main():
    parser = argparse.ArgumentParser(
        description="Interface CLI pour le module genome_crypto (encodage, chiffrement ADN),"

        
    )

    subparsers = parser.add_subparsers(dest="command", help="Sous-commandes disponibles")

    # ENCODE
    paresr_encode = subparsers.add_parser("encode", help="Encoder un texte en ADN")
    paresr_encode.add_argument("text", help="Texte à encoder")

    # DECODE
    paresr_decode = subparsers.add_parser("decode", help="Décoder une séquence ADN")
    paresr_decode.add_argument("dna", help="Séquence ADN à décoder")

    # ENCRYPT
    parser_encrypt = subparsers.add_parser("encrypt", help="Chiffrer une séquence ADN")
    parser_encrypt.add_argument("dna", help="Séquence ADN à chiffrer")
    parser_encrypt.add_argument("key", help="Clé de chiffrement")


    # DECRYPT
    parser_decrypt = subparsers.add_parser("decrypt", help="Déchiffre une séquence ADN")
    parser_decrypt.add_argument("dna", help="Séquence ADN chiffrée")
    parser_decrypt.add_argument("key", help="Clé de déchiffrement")


    # VERIFY
    parser_verify = subparsers.add_parser("verify", help="Vérifier l'intégrité entre deux textes")
    parser_verify.add_argument("original", help="Texte original")
    parser_verify.add_argument("decrypted", help="Texte déchiffré à comparer")


    args = parser.parse_args()

    if args.command == "encode":
        print(genome_crypto.test_to_dna(args.text))

    elif args.command == "decode":
        print(genome_crypto.dna_to_text(args.dna))
    
    elif args.command == "encrypt":
        encrypted = genome_crypto.encrypted_dna_sequence(args.dna, args.key)

        print(encrypted)

    elif args.command == "decrypt":
        decrypted = genome_crypto.decrypt_dna_sequence(args.dna, args.key)
        print(decrypted)

    elif args.command == "verify":
        is_valid = genome_crypto.verify_integrity(args.original, args.decrypted)

        print("Intégrité OK" if is_valid else "Intégrité NON VALIDE")

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()