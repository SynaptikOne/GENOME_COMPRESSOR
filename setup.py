


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
FR : Script de configuration pour le packaging et l'installation du projet 
GENOME_COMPRESSOR.
Utilise setuptools pour créer un paquet installable via pip.

Auteur             : Rakotondravelo Tahina Mickaël


EN : Setup script for packaging and installing the GENOME_COMPRESSOR project.
Uses setuptools to crate a pip-installable package.

Author               : Rakotondravelo Tahina Mickaël
"""

# pip install setuptools wheel



from setuptools import setup, find_packages

# FR : Inforamtions générqles sur le paquet
# EN : General package information

setup(
    name="genome_compressor",
    version="1.0.0",
    description="Outil de compression ADN bio-inspire",
    author="Rakotondravelo Tahina Mickaël",
    author_email="darkphex@example.com",
    url="https://github.com/ton-github/genome_compressor",

    # FR : Inclut tous les sous-modules dans les répertoires spécifiés
    # EN : Includes all submodules in specified directories
    packages=find_packages(include=["src*","cli*", "gui*"]),
    py_modules=["run"],
    package_dir={"": "."},

    # FR : Dépendances nécessaires à l'installation
    # EN : Required dependencies for installation
    install_requires=[
        "colorama",
        "tqdm",
        "inquirer",
        "setuptools",
        "wheel",
        "Pytest",
        "Pillow",
    ],

    # FR : Point d'entrée pour la commande 'genome_compressor'
    # En : Entry point for the 'genome_compressor' command
    entry_points={
        "console_scripts": [
            "genome_compressor=run:main", # permet a l'utilisateur de taper `genome_compressor`
        ],
    },
    include_package_data=True,

    # FR : Informations supplémentaires pour les outils de distribution
    # EN : Additional metadata for distribution tools
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS independent",
    ],
    python_requires=">=3.7",
)