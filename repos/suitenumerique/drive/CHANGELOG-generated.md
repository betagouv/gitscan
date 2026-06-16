## Changelog : drive (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration des fonctionnalités de conversion de fichiers, notamment l'ajout de la conversion de documents Office hérités via OnlyOffice. De nouvelles options d'exportation de dossiers ont été implémentées, permettant de télécharger des dossiers entiers sous forme d'archives ZIP. Des améliorations ont également été apportées à la gestion des comptes utilisateurs, avec l'introduction d'un processus de réconciliation pour les comptes. Enfin, l'interface utilisateur a été enrichie avec de nouveaux composants et des corrections de bugs pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter des dossiers entiers sous forme d'archives ZIP. [#7b12fdb](https://github.com/suitenumerique/drive/commit/7b12fdb)
- Ajout de la gestion de la réconciliation des comptes utilisateurs, avec des pages de confirmation et un import CSV. [#0ce6c56](https://github.com/suitenumerique/drive/commit/0ce6c56), [#e253868](https://github.com/suitenumerique/drive/commit/e253868), [#6f926c6](https://github.com/suitenumerique/drive/commit/6f926c6)
- Prise en charge de l'upload de fichiers Grist. [#a4105a3](https://github.com/suitenumerique/drive/commit/a4105a3)
- Ajout de composants CTA (Call To Action) pour les fichiers et dossiers publics, avec des actions spécifiques pour les utilisateurs authentifiés et anonymes. [#4adbe9f](https://github.com/suitenumerique/drive/commit/4adbe9f), [#82e57ae](https://github.com/suitenumerique/drive/commit/82e57ae)
- Ajout d'un modal de conversion de fichiers. [#af6ab74](https://github.com/suitenumerique/drive/commit/af6ab74)

### Évolutions techniques
- Implémentation du backend de conversion de fichiers Office hérités avec OnlyOffice, incluant la signature des requêtes avec JWT et la gestion des variables d'environnement. [#5149283](https://github.com/suitenumerique/drive/commit/5149283), [#3e89881](https://github.com/suitenumerique/drive/commit/3e89881), [#212f4f1](https://github.com/suitenumerique/drive/commit/212f4f1), [#350a482](https://github.com/suitenumerique/drive/commit/350a482)
- Amélioration de la gestion des healthchecks pour Collabora. [#2d16361](https://github.com/suitenumerique/drive/commit/2d16361)
- Normalisation de la recherche d'extensions WOPI. [#6a07e18](https://github.com/suitenumerique/drive/commit/6a07e18)
- Suppression des colonnes `numchild` obsolètes de la table `item`. [#06d841c](https://github.com/suitenumerique/drive/commit/06d841c)
- Remplacement de `VersionId` par `Etag` pour WOPI. [#3293ce5](https://github.com/suitenumerique/drive/commit/3293ce5)

### Autres changements
- Mise à jour de la bibliothèque d'interface utilisateur `ui-kit` vers la version 0.22.0. [#3088455](https://github.com/suitenumerique/drive/commit/3088455)
- Correction de bugs mineurs liés à l'affichage et au comportement de l'interface utilisateur. [#b5e8538](https://github.com/suitenumerique/drive/commit/b5e8538), [#caa1dbc](https://github.com/suitenumerique/drive/commit/caa1dbc), [#cbec3ba](https://github.com/suitenumerique/drive/commit/cbec3ba)
- Amélioration de la gestion des erreurs et des états de chargement lors de l'upload de fichiers. [#533606b](https://github.com/suitenumerique/drive/commit/533606b)
- Ajout de documentation sur la réconciliation des comptes utilisateurs. [#9995a2a](https://github.com/suitenumerique/drive/commit/9995a2a)
- Correction de la sanitisation des slashes dans les noms de fichiers créés par template. [#0575463](https://github.com/suitenumerique/drive/commit/0575463)
