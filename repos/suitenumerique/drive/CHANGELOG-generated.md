## Changelog : drive (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par une amélioration significative de l'expérience utilisateur, notamment avec l'ajout de nouvelles fonctionnalités comme la création de fichiers à partir de modèles, la gestion du mirroring de fichiers vers S3, et l'amélioration de l'interface utilisateur avec un menu contextuel et des breadcrumbs plus intuitifs. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Ajout de la possibilité de créer des fichiers à partir de modèles. [#939a6e4](https://github.com/suitenumerique/drive/commit/939a6e4)
- Implémentation d'un système de mirroring de fichiers vers S3 pour la sauvegarde et la redondance. [#5a30a98](https://github.com/suitenumerique/drive/commit/5a30a98)
- Ajout d'un menu contextuel (clic droit) dans l'explorateur de fichiers. [#6ed33a3](https://github.com/suitenumerique/drive/commit/6ed33a3)
- Amélioration des breadcrumbs pour afficher la page racine lors de la navigation. [#fcf4635](https://github.com/suitenumerique/drive/commit/fcf4635)
- Ajout d'un système de notes de version affichées aux utilisateurs. [#9bf7fa7](https://github.com/suitenumerique/drive/commit/9bf7fa7)
- Possibilité de télécharger un fichier via une URL dédiée. [#4e5aefc](https://github.com/suitenumerique/drive/commit/4e5aefc)
- Possibilité de personnaliser l'apparence de l'interface avec des CSS et JS injectés. [#abe4ca1](https://github.com/suitenumerique/drive/commit/abe4ca1)
- Filtrage des éléments récents pour n'afficher que les fichiers. [#15bff8c](https://github.com/suitenumerique/drive/commit/15bff8c)

### Évolutions techniques
- Mise à jour de Django en version 5.2.12. [#d406bf5](https://github.com/suitenumerique/drive/commit/d406bf5)
- Mise à jour de Pillow en version 12.1.1. [#50e19c9](https://github.com/suitenumerique/drive/commit/50e19c9)
- Mise à jour de cryptography en version 46.0.5. [#aa5efc3](https://github.com/suitenumerique/drive/commit/aa5efc3)
- Amélioration de la configuration des probes dans Helm. [#e688fd1](https://github.com/suitenumerique/drive/commit/e688fd1) et [#d9a05cb](https://github.com/suitenumerique/drive/commit/d9a05cb)
- Optimisation du workflow Docker Hub CI/CD. [#564822d](https://github.com/suitenumerique/drive/commit/564822d)
- Ajout de support pour l'architecture ARM64 dans les images Docker. [#f43c8a4](https://github.com/suitenumerique/drive/commit/f43c8a4)
- Refactoring du code pour améliorer la maintenabilité et la lisibilité. (nombreux commits)
- Ajout d'une commande de gestion pour nettoyer les éléments en attente de mirroring. [#0dde4d2](https://github.com/suitenumerique/drive/commit/0dde4d2)
- Configuration de plusieurs workers Celery. [#2065ffb](https://github.com/suitenumerique/drive/commit/2065ffb)

### Autres changements
- Correction de typos dans la documentation. [#5e47250](https://github.com/suitenumerique/drive/commit/5e47250)
- Mise à jour de la documentation pour le mirroring de fichiers. [#31d9be6](https://github.com/suitenumerique/drive/commit/31d9be6)
- Mise à jour de la documentation pour la personnalisation de l'interface. [#c89aa81](https://github.com/suitenumerique/drive/commit/c89aa81)
- Mise à jour des dépendances Python. [#21bdaaa](https://github.com/suitenumerique/drive/commit/21bdaaa)
