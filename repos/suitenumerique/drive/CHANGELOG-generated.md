## Changelog : drive (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration des fonctionnalités de conversion de fichiers, notamment en ajoutant la prise en charge de la conversion de documents hérités via OnlyOffice. De plus, de nouvelles fonctionnalités d'exportation de dossiers ont été implémentées, permettant aux utilisateurs de télécharger des dossiers entiers sous forme d'archives ZIP. Des améliorations ont également été apportées à la gestion des comptes utilisateurs, avec l'introduction d'un processus de réconciliation.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter des dossiers entiers en tant qu'archives ZIP. [#cd7bebf](https://github.com/suitenumerique/drive/commit/cd7bebf)
- Ajout de pages de confirmation pour la réconciliation des comptes utilisateurs.
- Ajout de CTAs (Call To Action) pour les fichiers et dossiers publics, permettant aux utilisateurs anonymes et authentifiés d'accéder plus facilement aux fonctionnalités.
- Prise en charge du téléchargement de fichiers Grist. [#a4105a3](https://github.com/suitenumerique/drive/commit/a4105a3)
- Ajout d'un point de terminaison pour la confirmation par email lors de la réconciliation des utilisateurs.
- Ajout d'une interface d'administration pour la réconciliation des utilisateurs.
- Ajout de modèles de données pour la réconciliation des utilisateurs.
- Ajout d'une commande de démonstration pour la réconciliation des utilisateurs.
- Documentation de la réconciliation des comptes utilisateurs.

### Évolutions techniques
- Implémentation du backend pour la conversion de fichiers via OnlyOffice, incluant la signature des requêtes avec JWT. [#5149283](https://github.com/suitenumerique/drive/commit/5149283)
- Mise en place d'une file d'attente pour la conversion des fichiers hérités. [#10f5724](https://github.com/suitenumerique/drive/commit/10f5724)
- Normalisation de la recherche d'extensions WOPI. [#6a07e18](https://github.com/suitenumerique/drive/commit/6a07e18)
- Amélioration de la gestion des erreurs et de la robustesse du code de conversion.
- Refactorisation du poller pour gérer les éléments en cours de conversion. [#302bff1](https://github.com/suitenumerique/drive/commit/302bff1)
- Suppression des colonnes `numchild` obsolètes de la table `item`. [#06d841c](https://github.com/suitenumerique/drive/commit/06d841c)
- Remplacement de `VersionId` par `Etag` pour WOPI. [#3293ce5](https://github.com/suitenumerique/drive/commit/3293ce5)
- Correction de la gestion des barres obliques dans les noms de fichiers créés par des templates. [#0575463](https://github.com/suitenumerique/drive/commit/0575463)

### Autres changements
- Documentation des variables d'environnement pour la conversion OnlyOffice. [#350a482](https://github.com/suitenumerique/drive/commit/350a482)
- Mise à jour de la bibliothèque `ui-kit` vers la version 0.22.0.
- Mise à jour de la dépendance `urllib3` pour corriger une vulnérabilité de sécurité.
- Mise à jour de la dépendance `django` pour corriger une vulnérabilité de sécurité.
- Ajout de tests E2E pour le flux de conversion.
- Amélioration des tests pour les CTAs publiques.
- Déplacement des imports de mimes vers `ui-kit`.
- Mise à jour de la documentation du changelog.
