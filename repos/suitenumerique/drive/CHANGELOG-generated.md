## Changelog : drive (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, l'équipe de développement s'est concentrée sur l'amélioration des fonctionnalités de conversion de fichiers, notamment l'ajout de la conversion de documents Office hérités via OnlyOffice. De nouvelles fonctionnalités d'exportation de dossiers ont également été implémentées, permettant aux utilisateurs de télécharger des dossiers entiers sous forme d'archives ZIP. Des améliorations ont été apportées à la gestion des comptes utilisateurs, avec l'ajout d'un processus de réconciliation pour les comptes. Enfin, des corrections de bugs et des optimisations ont été réalisées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter des dossiers entiers sous forme d'archives ZIP. [#7b12fdb](https://github.com/suitenumerique/drive/commit/7b12fdb)
- Implémentation d'un processus de réconciliation des comptes utilisateurs, incluant une confirmation par email. [#0ce6c56](https://github.com/suitenumerique/drive/commit/0ce6c56)
- Ajout de la prise en charge du téléchargement de fichiers Grist. [#a4105a3](https://github.com/suitenumerique/drive/commit/a4105a3)
- Ajout de boutons d'appel à l'action (CTA) pour les fichiers et dossiers publics, différenciés selon l'authentification de l'utilisateur. [#4adbe9f](https://github.com/suitenumerique/drive/commit/4adbe9f)
- Ajout d'une modale de conversion de fichiers. [#af6ab74](https://github.com/suitenumerique/drive/commit/af6ab74)

### Évolutions techniques
- Implémentation d'un backend de conversion de fichiers Office hérités utilisant OnlyOffice, avec signature des requêtes via JWT. [#5149283](https://github.com/suitenumerique/drive/commit/5149283)
- Amélioration de la gestion des erreurs et des états de conversion de fichiers. [#302bff1](https://github.com/suitenumerique/drive/commit/302bff1)
- Normalisation de la recherche d'extensions WOPI. [#6a07e18](https://github.com/suitenumerique/drive/commit/6a07e18)
- Remplacement de `VersionId` par `Etag` pour WOPI. [#3293ce5](https://github.com/suitenumerique/drive/commit/3293ce5)
- Suppression des colonnes `numchild` obsolètes de la table `item`. [#06d841c](https://github.com/suitenumerique/drive/commit/06d841c)

### Autres changements
- Amélioration de la formulation du contenu de la modale de conversion. [#b5e8538](https://github.com/suitenumerique/drive/commit/b5e8538)
- Correction d'un problème de polling des éléments dans un état d'analyse pendant le téléchargement. [#caa1dbc](https://github.com/suitenumerique/drive/commit/caa1dbc)
- Ajout d'un suffixe au nom de fichier converti. [#533606b](https://github.com/suitenumerique/drive/commit/533606b)
- Correction du healthcheck Collabora en l'absence de `curl`. [#2d16361](https://github.com/suitenumerique/drive/commit/2d16361)
- Documentation des variables d'environnement pour la conversion OnlyOffice. [#350a482](https://github.com/suitenumerique/drive/commit/350a482)
- Correction d'un bug empêchant le rejet de la conversion en cas de secret JWT non configuré. [#212f4f1](https://github.com/suitenumerique/drive/commit/212f4f1)
- Correction de la sanitisation des slashes dans les noms de fichiers créés par template. [#0575463](https://github.com/suitenumerique/drive/commit/0575463)
- Mise à jour de la bibliothèque UI-kit à la version 0.22.0. [#3088455](https://github.com/suitenumerique/drive/commit/3088455)
