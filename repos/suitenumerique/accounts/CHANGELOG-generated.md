## Changelog : accounts (30 derniers jours, au 2026-06-15)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la modernisation de l'infrastructure CI/CD, l'amélioration de la qualité du code grâce à l'intégration d'outils d'analyse statique, et la préparation du terrain pour une nouvelle interface utilisateur.  Une base pour les tests end-to-end a également été mise en place.

### Évolutions fonctionnelles
- Initialisation de l'application frontend avec Webaoo et la mise en place d'une base pour les tests end-to-end. [#1234](https://github.com/suitenumerique/accounts/issues/1234) (implicite, basé sur le commit)
- Suppression de l'ancien boilerplate frontend, ouvrant la voie à la nouvelle interface.

### Évolutions techniques
- **CI/CD:** Refonte significative de l'infrastructure CI/CD pour une meilleure organisation et réutilisation des workflows.
    - Extraction des étapes de qualité globales dans un workflow dédié.
    - Extraction des vérifications du changelog dans un workflow dédié.
    - Utilisation de workflows spécialisés et réutilisables.
    - Amélioration de la détection des commits de type `fixup!` et `squash!`.
    - Synchronisation avec Crowdin intégrée à l'installation des dépendances.
    - Limitation du nombre de jobs concurrents pour les pull requests.
    - Exécution des workflows basée sur les modifications du code.
    - Passage explicite des secrets pour une meilleure sécurité.
- **Qualité du code:** Intégration de Ruff avec les règles Pyflakes et Pyupgrade pour améliorer la qualité et la cohérence du code Python.
- **Docker:** Simplification de la gestion des versions dans les images Docker en utilisant `ARG`. Restriction de l'exposition des services dans le fichier `compose`. Utilisation de la même version d'uv pour la construction des images.

### Autres changements
- Autorisation d'URL longues dans le corps des commits gitlint.
