# PatternScanner

**PatternScanner** est un module Python destine a detecter les motifs frequents dans une sequence de caracteres. Il prend en charge deux methodes d'analyse:
-**Naive** : robuste pour toutes les longuers de motifs.
-**Rabin-Karp**: plus rapide, mais necessite une longueur fixe de motif.

Un mecanisme de **repli automatique** est integre : si l'alogrithme Rabin-Kapr echoue, l'analyse bascule automatiquement vers la methode naive.


---
## Fonctionnalites
- Detection de motifs de longueur variable ou fixe
- Detection uniquement des motifs apparaissant  a une frequence minimale
- Methode de recherche optimisee (Rabin-Karp)
- Methode robuste par defaut (Naive)
- Selection automatique de l'algorithme en fonction des parametres
- Repli automatique en cas d'erreur


---

## Installation
```bash
git clone https://github.com/votre-utilisateur/GENOME_COMPRESSOR.git cd GENOME_COMPRESSOR
# Optionnel : creation d'un environnement virtuel
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt # Aucun package externe requis pour ce module