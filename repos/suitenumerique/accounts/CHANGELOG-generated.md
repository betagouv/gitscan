## Changelog : accounts (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'infrastructure CI/CD, la qualité du code et la préparation du terrain pour l'ajout d'une nouvelle interface utilisateur. Des corrections et des optimisations ont été apportées aux workflows, aux outils de linting et à la gestion des dépendances. La migration vers Python 3.14.5 a également été effectuée.

### Évolutions fonctionnelles
- Reconstruction de l'application frontend en utilisant les conventions "drive" pour une meilleure cohérence et expérience utilisateur. [#issue à venir]
- Suppression de l'ancien code boilerplate frontend, préparant le terrain pour la nouvelle interface. [#issue à venir]
- Mise en place de la stack de tests end-to-end (e2e) pour assurer la qualité de l'application. [#issue à venir]

### Évolutions techniques
- Amélioration de la détection des commits de type "fixup!" et "squash!" dans le CI.
- Optimisation du CI pour ne scanner que les lignes ajoutées lors de la recherche de `print()`.
- Autorisation des URLs longues dans le corps des commits pour une meilleure lisibilité.
- Sécurisation du CI en passant explicitement les secrets nécessaires au lieu d'hériter de tous.
- Synchronisation avec Crowdin intégrée à l'installation des dépendances.
- Mise en place de groupes de concurrence pour les workflows `pull_request` afin d'optimiser l'utilisation des ressources.
- Refonte des workflows CI pour une meilleure organisation et réutilisation du code.
- Extraction des étapes de qualité globales dans un workflow dédié.
- Extraction des vérifications du changelog dans un workflow dédié.
- Activation des règles Pyflakes et Pyupgrade de Ruff pour améliorer la qualité du code Python.
- Utilisation de `ARG` dans le Dockerfile pour simplifier la gestion des versions.
- Utilisation de la même version d'uv dans tous les builds d'images Docker.
- Suppression du fichier `setup.py` devenu inutile.
- Mise à jour de la configuration de `action/setup-python` pour Crowdin.
- Utilisation de groupes de dépendances pour l'environnement de développement.
- Utilisation de dépendances verrouillées pour les workflows backend.
- Correction de plusieurs erreurs shellcheck dans les scripts shell.
- Suppression d'un script lié à un sous-module Git obsolète.
- Mise à jour de Python vers la version 3.14.5.

### Autres changements
- Amélioration de la gestion des arguments optionnels dans les scripts binaires.
- Correction du script `generate-readme.sh` pour qu'il fonctionne depuis n'importe quel répertoire.
- Modification de la configuration de Docker pour ne pas exposer les services inutilement.
