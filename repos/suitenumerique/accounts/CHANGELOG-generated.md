## Changelog : accounts (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'infrastructure CI/CD, la qualité du code et la préparation pour l'ajout d'une interface utilisateur (frontend). Des fondations ont été posées pour les tests end-to-end et une refonte de l'application frontend est en cours.

### Évolutions fonctionnelles
- Reconstruction de l'application frontend en utilisant de nouvelles conventions.
- Suppression de l'ancien code boilerplate du frontend.

### Évolutions techniques
- **CI/CD :** Amélioration de la détection des commits de type `fixup!` et `squash!`.
- **CI/CD :** Optimisation du processus de CI pour ne scanner que les lignes de code ajoutées à la recherche de `print()`.
- **CI/CD :** Autorisation d'URL longues dans le corps des messages de commit.
- **CI/CD :** Passage explicite des secrets au lieu d'hériter de tous.
- **CI/CD :** Synchronisation avec Crowdin intégrée à l'installation des dépendances.
- **CI/CD :** Mise en place de groupes de concurrence pour les workflows `pull_request`.
- **CI/CD :** Exécution des workflows basée sur les modifications du code.
- **CI/CD :** Identification et extraction des workflows réutilisables.
- **CI/CD :** Extraction des étapes de qualité globales dans un workflow dédié.
- **CI/CD :** Extraction des vérifications du changelog dans un workflow dédié.
- **Qualité du code :** Activation des règles `pyupgrade` et `Pyflakes` de Ruff pour améliorer la qualité du code Python.
- **Docker :** Simplification de la gestion des versions avec l'utilisation de `ARG`.
- **Docker :** Utilisation de la même version de `uv` lors de la construction des images.
- **Dépendances :** Suppression du fichier `setup.py` obsolète.
- **Dépendances :** Utilisation de dépendances verrouillées pour les workflows backend.
- **Shell scripts :** Correction de plusieurs erreurs shellcheck (SC2034, SC2086, SC2164, SC2181).
- **Runtime :** Mise à jour de Python vers la version 3.14.5.
- **Backend :** Utilisation de groupes de dépendances pour l'environnement de développement (`dev`).
- **Helm :** Correction du script `generate-readme.sh` pour qu'il fonctionne depuis n'importe quel emplacement.
- **Divers :** Amélioration de la gestion des arguments optionnels dans les scripts.
- **Divers :** Suppression d'un script lié à un sous-module Git.

### Autres changements
- Mise en place de la stack de tests end-to-end.
- Initialisation de l'application frontend.
