# GENOME_COMPRESSOR - Roadmap

## Phase 1 - Mise en palce du nouay fonctionnel
> Objectif : Creer une version minimale viable (MVP)

- [x] Initialiser le depot Github avec '.gitignore' , 'README.md', 'LICENCE'
- [] Implementer 'pattern_scanner.py'
- [] Implementer 'gene_encoder.py'
- [] Implementer 'mutation_encoder.py'
- [] Implementer 'genome_compressor.py'
- [] Implementer 'storage-model.py'
- [] Implementer 'genome_decoder.py'
- [] Implementer 'utils.py'
- [] Creer 'main.py' comme point d'entree CLI
- [] Ajouter des cas de test dans '/examples'

---

## Phase 2 - Qualite & Tests
> Objectif : Assurer la stabilite a la reproductibilite

- [] Ecrire des testes unitaires dans le dossier '/tests'
- [] Integrer 'pytest'
- [] Configurer Github Actions pour CI/CD
- [] Generer un rapport de couverture de code (Codecov)
- [] Corriger bugs et ameliorer la robustesse

---
## Phase 3 - Documentation & Visualisation
> Objectif : Documenter et expliquer le fonctionnement
- [] Completer 'docs/cahiers_des_charges.md'
- [] Ajouter un schema visuel ('docs/architecture.png')
- [] Completer le 'README.md' (usage, exemple CLI)
- [] Ajouter des jeux de donnees d'exemple dans '/examples'

--- Phase 4 - Interface & UX
> Objectif : Faciliter l'utilisation pour tout le monde
- [] Implementer 'cli/comressor_cli.py'
- [] Ajouter options '--compress', '--decompress', '--view'
- [] (Optionnel) Creer une version web simple (Flask)
- [] (Optionnel) Creer un visualiseur '.dna' (Graphiz)


---
## Phase 5 - Opne Source & Communaute
> Objectif : Structurer le projet pour les contributeurs

- [] Ajouter 'CONTRIBUTING.md' avec les bonnes pratiques
- [] Ajouter 'CODE_OF_CONDUCT.md'
- [] Creer des issues type << Good First Issue >>
- [] Ajouter des badget dans le 'README.md' (build, licence, etc.)
- [] Promouvoir le projet sur GITHUB (tags, description)

---

## Suivi
N'hesiter pas a creer un tableau Github Projet pour suivre les taches, ou utiliser un Kanban board sur GitHub.