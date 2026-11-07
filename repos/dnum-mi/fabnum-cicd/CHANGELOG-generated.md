## Changelog : fabnum-cicd (30 derniers jours, au 04/11/2026)

### Résumé
Ce mois-ci, le projet a connu une phase importante de restructuration et d'optimisation. Les workflows Python ont été segmentés pour plus de flexibilité, et de nouveaux outils d'audit de sécurité ont été intégrés. Les performances de la chaîne CI ont été améliorées pour réduire les temps d'attente, tout en renforçant la stabilité du processus de publication des versions.

### Évolutions fonctionnelles
- **Nouveaux workflows réutilisables** : Ajout de workflows dédiés pour le test Python (`test-python`) et la publication sur PyPI (`release-pypi`).
- **Audit de sécurité** : Introduction d'un workflow d'audit (`scan-zizmor`) pour vérifier la conformité et la sécurité des workflows GitHub Actions.

### Évolutions techniques
- **Optimisation des performances** :
    - Exécution des suites de tests en parallèle avec annulation automatique des processus obsolètes.
    - Accélération du scan de sécurité en ne bloquant plus l'exécution sur le traitement des fichiers SARIF par GitHub.
    - Optimisation des tests Helm en ne créant le cluster `kind` que si un chart doit effectivement être installé.
    - Utilisation de l'outil Go déjà présent sur les runners pour la génération de `helm-docs`.
- **Architecture et CI/CD** :
    - Refactorisation du workflow Python : découpage en quatre étapes distinctes (lint, test, build et release) pour une meilleure granularité.
    - Amélioration du build Docker : les builds mono-job sont désormais poussés directement au lieu de passer par une étape de fusion.
    - Synchronisation majeure des workflows réutilisables avec la version 0.40.0 de l'upstream.
    - Centralisation de la validation de la pipeline derrière un check unique obligatoire.
- **Corrections et stabilité** :
    - Stabilisation du processus de synchronisation des branches de pré-release (gestion des ancres de commit et des conflits de fichiers de release).
    - Correction du linting des commits pour supporter les modules ES.
    - Amélioration de la sécurité et de la fiabilité de l'exécution des commandes appelantes dans les workflows.
    - Correction du processus de release Helm pour respecter la configuration de création de release.
    - Rendu des git-hooks exécutables.

### Autres changements
- **Documentation** : Mise à jour de la documentation française, ajout de conseils sur les stratégies de versioning (pinning) et de la documentation sur la compatibilité avec les releases immuables pour Helm.
- **Configuration** : Durcissement des règles de linting YAML pour exiger une indentation de deux espaces.
