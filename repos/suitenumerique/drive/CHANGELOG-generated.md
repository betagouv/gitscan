## Changelog : drive (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à Drive au cours des 30 derniers jours. Les utilisateurs bénéficieront d'une meilleure expérience avec l'ajout de nouvelles fonctionnalités comme la création de fichiers à partir de modèles, la gestion des fichiers volumineux, et l'amélioration de l'interface utilisateur avec des menus contextuels et une navigation plus intuitive. Des corrections de bugs et des optimisations de performance ont également été apportées pour une meilleure stabilité et réactivité de la plateforme.

### Évolutions fonctionnelles
- Ajout de la possibilité de créer des fichiers à partir de modèles. [#21bdaaa](https://github.com/suitenumerique/drive/commit/21bdaaa)
- Possibilité de télécharger des fichiers de type `text/x-tex` et `application/zed`. [#dfd6d1f](https://github.com/suitenumerique/drive/commit/dfd6d1f)
- Amélioration de la gestion des fichiers volumineux : limitation de la taille des fichiers uploadés et affichage correct de la progression de l'upload. [#d9f8069](https://github.com/suitenumerique/drive/commit/d9f8069), [#bb28499](https://github.com/suitenumerique/drive/commit/bb28499), [#4bfff61](https://github.com/suitenumerique/drive/commit/4bfff61), [#49f39d7](https://github.com/suitenumerique/drive/commit/49f39d7)
- Ajout de menus contextuels (clic droit) dans l'explorateur de fichiers. [#6ed33a3](https://github.com/suitenumerique/drive/commit/6ed33a3)
- Amélioration de la navigation avec l'ajout du chemin racine dans les breadcrumbs. [#179e4c1](https://github.com/suitenumerique/drive/commit/179e4c1)
- Filtrage des éléments récents pour n'afficher que les fichiers. [#15bff8c](https://github.com/suitenumerique/drive/commit/15bff8c)
- Possibilité de copier/coller dans l'éditeur WOPI. [#c4977b8](https://github.com/suitenumerique/drive/commit/c4977b8)
- Amélioration de l'interface utilisateur de l'explorateur et du panneau de droite. [#db5b0f3](https://github.com/suitenumerique/drive/commit/db5b0f3), [#782804f](https://github.com/suitenumerique/drive/commit/782804f), [#5bbf11d](https://github.com/suitenumerique/drive/commit/5bbf11d)
- Ajout de la synchronisation de la langue de l'utilisateur entre le backend et le navigateur. [#35c6c19](https://github.com/suitenumerique/drive/commit/35c6c19)

### Évolutions techniques
- Mise à jour de Django en version 5.2.12. [#d406bf5](https://github.com/suitenumerique/drive/commit/d406bf5)
- Mise à jour de Pillow en version 12.1.1. [#50e19c9](https://github.com/suitenumerique/drive/commit/50e19c9)
- Amélioration de la configuration des probes dans Helm. [#d9a05cb](https://github.com/suitenumerique/drive/commit/d9a05cb), [#e7139aa](https://github.com/suitenumerique/drive/commit/e7139aa)
- Optimisation du workflow Docker Hub. [#564822d](https://github.com/suitenumerique/drive/commit/564822d)
- Ajout de la prise en charge de l'architecture ARM64 pour les images Docker. [#f43c8a4](https://github.com/suitenumerique/drive/commit/f43c8a4)
- Refactorisation du code pour améliorer la maintenabilité et la lisibilité. [#a98a5d7](https://github.com/suitenumerique/drive/commit/a98a5d7), [#c1709b5](https://github.com/suitenumerique/drive/commit/c1709b5), [#26c9eac](https://github.com/suitenumerique/drive/commit/26c9eac)
- Amélioration des tests E2E et ajout de nouvelles couvertures de tests. [#42b24ca](https://github.com/suitenumerique/drive/commit/42b24ca), [#f2730e5](https://github.com/suitenumerique/drive/commit/f2730e5), [#79dc34c](https://github.com/suitenumerique/drive/commit/79dc34c), [#6b56553](https://github.com/suitenumerique/drive/commit/6b56553)
- Activation de règles de linting plus strictes avec Ruff. [#088665c](https://github.com/suitenumerique/drive/commit/088665c)
- Séparation des actions de vérification et de correction de linting avec Ruff. [#01dd5ae](https://github.com/suitenumerique/drive/commit/01dd5ae)

### Autres changements
- Mise à jour de la documentation et du changelog. [#3387246](https://github.com/suitenumerique/drive/commit/3387246), [#5e47250](https://github.com/suitenumerique/drive/commit/5e47250), [#36b39a6](https://github.com/suitenumerique/drive/commit/36b39a6), [#2026-03-10T16:37:28+01:00](https://github.com/suitenumerique/drive/commit/51c71e8)
- Correction de typos dans la documentation. [#5e47250](https://github.com/suitenumerique/drive/commit/5e47250)
- Mise à jour de la version de `@gouvfr-lasuite/ui-kit` à 0.19.10 et 0.19.9. [#356da2b](https://github.com/suitenumerique/drive/commit/356da2b), [#3070460](https://github.com/suitenumerique/drive/commit/3070460)
- Mise à jour des dépendances Python. [#21bdaaa](https://github.com/suitenumerique/drive/commit/21bdaaa)
- Ajout d'une tâche cron pour nettoyer les éléments en attente d'exclusion. [#79dc34c](https://github.com/suitenumerique/drive/commit/79dc34c)
- Suppression d'une authentification ServerToServer inutilisée. [#a19d70c](https://github.com/suitenumerique/drive/commit/a19d70c)
- Suppression de Scalingo pgdump. [#abd055a](https://github.com/suitenumerique/drive/commit/abd055a)
