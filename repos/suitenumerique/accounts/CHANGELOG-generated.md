## Changelog : accounts (30 derniers jours, au 2026-06-16)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'infrastructure CI/CD, la qualité du code et la préparation de l'intégration d'une nouvelle interface utilisateur. Des fondations ont été posées pour des tests end-to-end et une refonte de l'application frontend.

### Évolutions fonctionnelles
- Initialisation de l'application frontend avec Webaoo et la mise en place d'un stack de tests end-to-end. [#1234](https://github.com/suitenumerique/accounts/issues/1234) (impliqué par le commit c725e59)

### Évolutions techniques
- **CI/CD :** Amélioration significative de la configuration CI/CD, incluant l'extraction de tâches communes dans des workflows réutilisables, l'optimisation de la détection des commits de type `fixup!` et `squash!`, et la gestion plus sécurisée des secrets.
- **Qualité du code :** Activation de règles supplémentaires de Ruff (Pyflakes et Pyupgrade) pour améliorer la qualité et la cohérence du code Python.
- **Docker :** Simplification de la gestion des versions dans les images Docker et restriction de l'exposition des services.
- **Python :** Suppression du fichier `setup.py` devenu inutile.
- **Frontend :** Suppression de l'ancien boilerplate frontend et reconstruction de l'application selon les conventions Drive. (aecdcaf, 46f0f68)

### Autres changements
- Configuration améliorée de l'action `setup-python` pour Crowdin (923f370).
- Autorisation d'URL plus longues dans le corps des commits git (18c2518).
- Synchronisation avec Crowdin intégrée à l'installation des dépendances (2e404aa).
- Groupement des workflows pull request pour une meilleure gestion de la concurrence (619f916).
- Extraction des vérifications du changelog dans un workflow dédié (900cd9a).
