## Changelog : drive (30 derniers jours)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment avec l'ajout de fonctionnalités de création de fichiers à partir de modèles, de gestion des accès et de personnalisation de l'interface. Des corrections de bugs ont également été implémentées pour améliorer la stabilité et la fiabilité de la plateforme. Des optimisations techniques ont été réalisées pour améliorer les performances et la scalabilité.

### Évolutions fonctionnelles
- Ajout de la possibilité de créer des fichiers à partir de modèles. [#939a6e4](https://github.com/suitenumerique/drive/commit/939a6e4)
- Ajout d'un menu contextuel (clic droit) dans l'explorateur de fichiers. [#31454e2](https://github.com/suitenumerique/drive/commit/31454e2)
- Amélioration de la gestion des partages de fichiers et dossiers. [#f2730e5](https://github.com/suitenumerique/drive/commit/f2730e5)
- Ajout de la possibilité de personnaliser l'interface avec des CSS et JS injectés. [#a9948b5](https://github.com/suitenumerique/drive/commit/a9948b5)
- Ajout d'une fonctionnalité de notes de version pour informer les utilisateurs des dernières mises à jour. [#9bf7fa7](https://github.com/suitenumerique/drive/commit/9bf7fa7)
- Possibilité de rediriger vers une page d'accueil externe. [#ada6756](https://github.com/suitenumerique/drive/commit/ada6756)
- Amélioration de la navigation dans l'explorateur de fichiers et des actions sur les éléments. [#5414f10](https://github.com/suitenumerique/drive/commit/5414f10)
- Ajout d'une action de téléchargement pour les fichiers. [#4e5aefc](https://github.com/suitenumerique/drive/commit/4e5aefc)
- Amélioration de la gestion des autorisations et des rôles. [#9ada2dc](https://github.com/suitenumerique/drive/commit/9ada2dc)

### Évolutions techniques
- Optimisation du workflow Docker Hub pour des builds plus rapides. [#564822d](https://github.com/suitenumerique/drive/commit/564822d)
- Ajout de support pour l'architecture ARM64 dans les images Docker. [#f43c8a4](https://github.com/suitenumerique/drive/commit/f43c8a4)
- Refactorisation de l'architecture de gestion des accès pour une meilleure performance. [#dca39e3](https://github.com/suitenumerique/drive/commit/dca39e3)
- Amélioration de la gestion des tâches asynchrones avec Celery (configuration multiple workers, retry mechanism). [#ba73c4a](https://github.com/suitenumerique/drive/commit/ba73c4a)
- Mise à jour de plusieurs dépendances (Django, Pillow, cryptography). [#50e19c9](https://github.com/suitenumerique/drive/commit/50e19c9), [#aa5efc3](https://github.com/suitenumerique/drive/commit/aa5efc3)
- Amélioration des tests E2E avec Playwright (ajout de tests, stabilisation, débogage). [#a42e1a3](https://github.com/suitenumerique/drive/commit/a42e1a3)
- Suppression d'un backend d'authentification inutilisé. [#a19d70c](https://github.com/suitenumerique/drive/commit/a19d70c)

### Autres changements
- Mise à jour de la documentation pour la nouvelle fonctionnalité de mirroring. [#31d9be6](https://github.com/suitenumerique/drive/commit/31d9be6)
- Mise à jour de la documentation pour la personnalisation de l'interface. [#c89aa81](https://github.com/suitenumerique/drive/commit/c89aa81)
- Mise à jour des fichiers de configuration Helm pour plus de flexibilité. [#d9a05cb](https://github.com/suitenumerique/drive/commit/d9a05cb)
- Correction de bugs mineurs et améliorations de la qualité du code.
- Suppression de la notion de workspace. [#fcf4635](https://github.com/suitenumerique/drive/commit/fcf4635)
