## Changelog : drive (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration des fonctionnalités de conversion de fichiers, notamment l'ajout de la conversion de documents Office hérités via OnlyOffice, et l'ajout de la possibilité d'exporter des dossiers entiers en format ZIP. Des améliorations ont également été apportées à la gestion des utilisateurs, avec l'introduction d'un processus de réconciliation des comptes. Enfin, l'expérience utilisateur a été améliorée avec l'ajout de composants d'appel à l'action (CTA) pour les fichiers et dossiers publics.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter des dossiers entiers en format ZIP [#7b12fdb](https://github.com/suitenumerique/drive/commit/7b12fdb).
- Ajout de composants d'appel à l'action (CTA) pour les fichiers et dossiers publics, permettant aux utilisateurs de comprendre leurs options en fonction de leur statut d'authentification [#4adbe9f](https://github.com/suitenumerique/drive/commit/4adbe9f).
- Ajout d'un processus de réconciliation des comptes utilisateurs, incluant une interface d'administration et la possibilité d'importer des données via un fichier CSV [#9995a2a](https://github.com/suitenumerique/drive/commit/9995a2a).
- Prise en charge du téléchargement de fichiers Grist [#a4105a3](https://github.com/suitenumerique/drive/commit/a4105a3).
- Ajout d'une modale de conversion de fichiers [#af6ab74](https://github.com/suitenumerique/drive/commit/af6ab74).

### Évolutions techniques
- Implémentation du backend pour la conversion de fichiers Office hérités via OnlyOffice, incluant la signature des requêtes avec JWT et la gestion des variables d'environnement [#5149283](https://github.com/suitenumerique/drive/commit/5149283).
- Amélioration de la gestion des erreurs et de la robustesse de l'intégration Collabora, notamment la correction du healthcheck en l'absence de `curl` [#2d16361](https://github.com/suitenumerique/drive/commit/2d16361).
- Normalisation de la recherche d'extensions WOPI pour une meilleure compatibilité [#6a07e18](https://github.com/suitenumerique/drive/commit/6a07e18).
- Correction d'un problème où les requêtes WOPI utilisaient l'en-tête `Authorization` au lieu du paramètre de requête [#c67cb28](https://github.com/suitenumerique/drive/commit/c67cb28).
- Suppression des colonnes `numchild` obsolètes de la table `item` [#06d841c](https://github.com/suitenumerique/drive/commit/06d841c).

### Autres changements
- Mise à jour de la bibliothèque UI-kit à la version 0.22.0 [#3088455](https://github.com/suitenumerique/drive/commit/3088455).
- Correction de la gestion des barres obliques dans les noms de fichiers créés par des modèles [#0575463](https://github.com/suitenumerique/drive/commit/0575463).
- Amélioration du libellé du bouton de téléchargement pour l'action d'exportation de dossier [#cbec3ba](https://github.com/suitenumerique/drive/commit/cbec3ba).
- Ajout de traductions manquantes pour l'action d'exportation [#7ac7dd5](https://github.com/suitenumerique/drive/commit/7ac7dd5).
- Correction d'un problème où les éléments en cours d'analyse pendant le téléchargement n'étaient pas correctement interrogés [#caa1dbc](https://github.com/suitenumerique/drive/commit/caa1dbc).
- Ajout d'un suffixe au nom de fichier converti [#533606b](https://github.com/suitenumerique/drive/commit/533606b).
