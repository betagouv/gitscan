## Changelog : drive (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration des fonctionnalités de conversion de fichiers, notamment l'ajout de la conversion de documents Office hérités via OnlyOffice. De nouvelles options d'exportation de dossiers ont été implémentées, permettant aux utilisateurs de télécharger des dossiers entiers sous forme d'archives ZIP. Des améliorations ont également été apportées à la gestion des comptes utilisateurs, avec l'introduction d'un processus de réconciliation pour les comptes. Enfin, l'interface utilisateur a été enrichie avec de nouveaux composants et des corrections de bugs pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter des dossiers entiers sous forme d'archives ZIP. [#7b12fdb](https://github.com/suitenumerique/drive/commit/7b12fdb)
- Implémentation d'un processus de réconciliation des comptes utilisateurs, incluant une interface d'administration et des pages de confirmation. [#9995a2a](https://github.com/suitenumerique/drive/commit/9995a2a)
- Ajout de la prise en charge du téléchargement de fichiers Grist. [#a4105a3](https://github.com/suitenumerique/drive/commit/a4105a3)
- Ajout de boutons d'appel à l'action (CTA) pour les fichiers et dossiers publics, permettant aux utilisateurs authentifiés et anonymes d'interagir avec le contenu. [#4adbe9f](https://github.com/suitenumerique/drive/commit/4adbe9f)
- Ajout d'une modale de conversion de fichiers. [#af6ab74](https://github.com/suitenumerique/drive/commit/af6ab74)

### Évolutions techniques
- Implémentation du backend de conversion OnlyOffice, permettant la conversion de documents Office hérités. [#88e2693](https://github.com/suitenumerique/drive/commit/88e2693)
- Amélioration de la gestion des requêtes WOPI, en privilégiant le paramètre de requête WOPI sur l'en-tête d'autorisation. [#c67cb28](https://github.com/suitenumerique/drive/commit/c67cb28)
- Signature des requêtes de conversion OnlyOffice avec JWT pour une meilleure sécurité. [#5149283](https://github.com/suitenumerique/drive/commit/5149283)
- Correction du healthcheck Collabora pour fonctionner sans curl. [#2d16361](https://github.com/suitenumerique/drive/commit/2d16361)
- Normalisation de la recherche d'extensions WOPI. [#6a07e18](https://github.com/suitenumerique/drive/commit/6a07e18)
- Ajout d'un endpoint de streaming pour l'exportation de dossiers. [#ded840a](https://github.com/suitenumerique/drive/commit/ded840a)

### Autres changements
- Mise à jour de la bibliothèque UI-kit à la version 0.22.0. [#3088455](https://github.com/suitenumerique/drive/commit/3088455)
- Correction de la gestion des barres obliques dans les noms de fichiers créés par des modèles. [#0575463](https://github.com/suitenumerique/drive/commit/0575463)
- Amélioration de la gestion des éléments en cours d'analyse lors du téléchargement. [#caa1dbc](https://github.com/suitenumerique/drive/commit/caa1dbc)
- Ajout d'un suffixe au nom de fichier converti. [#533606b](https://github.com/suitenumerique/drive/commit/533606b)
- Mise à jour de la documentation pour inclure des informations sur la réconciliation des comptes utilisateurs. [#6f926c6](https://github.com/suitenumerique/drive/commit/6f926c6)
- Modification du libellé de téléchargement pour l'action d'exportation de dossier. [#cbec3ba](https://github.com/suitenumerique/drive/commit/cbec3ba)
- Correction de l'affichage des traductions pour l'action d'exportation. [#7ac7dd5](https://github.com/suitenumerique/drive/commit/7ac7dd5)
