## Changelog : drive (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de la compatibilité et de la conversion de fichiers, notamment pour les documents Office hérités. De nouvelles fonctionnalités ont été ajoutées pour permettre l'exportation de dossiers, la réconciliation des comptes utilisateurs et la gestion des invitations. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter des dossiers en tant qu'archives ZIP. [#7b12fdb](https://github.com/suitenumerique/drive/commit/7b12fdb)
- Implémentation d'un processus de réconciliation des comptes utilisateurs, incluant une confirmation par email. [#ff184e1](https://github.com/suitenumerique/drive/commit/ff184e1)
- Prise en charge du téléchargement de fichiers Grist. [#a4105a3](https://github.com/suitenumerique/drive/commit/a4105a3)
- Ajout de boutons d'appel à l'action (CTA) pour les liens publics et les fichiers, permettant aux utilisateurs anonymes et authentifiés d'interagir avec le contenu. [#82e57ae](https://github.com/suitenumerique/drive/commit/82e57ae)
- Ajout d'une interface modale pour la conversion de fichiers. [#af6ab74](https://github.com/suitenumerique/drive/commit/af6ab74)

### Évolutions techniques
- Mise en place d'un backend pour la conversion de fichiers Office hérités via OnlyOffice. [#88e2693](https://github.com/suitenumerique/drive/commit/88e2693)
- Normalisation de la recherche d'extensions WOPI. [#6a07e18](https://github.com/suitenumerique/drive/commit/6a07e18)
- Suppression des colonnes `numchild` obsolètes de la table `item`. [#06d841c](https://github.com/suitenumerique/drive/commit/06d841c)
- Remplacement de `VersionId` par `Etag` pour la compatibilité WOPI. [#3293ce5](https://github.com/suitenumerique/drive/commit/3293ce5)
- Sanityzation du caractère slash dans les noms de fichiers créés par des templates. [#0575463](https://github.com/suitenumerique/drive/commit/0575463)
- Généralisation du poller pour les éléments en cours de conversion. [#4f85801](https://github.com/suitenumerique/drive/commit/4f85801)

### Autres changements
- Mise à jour de la bibliothèque `ui-kit` vers la version 0.22.0. [#3088455](https://github.com/suitenumerique/drive/commit/3088455)
- Mise à jour de la dépendance `django` vers la version 5.2.14 (correctif de sécurité). [#4ecc4d7](https://github.com/suitenumerique/drive/commit/4ecc4d7)
- Mise à jour de la dépendance `urllib3` vers la version 2.7.0 (correctif de sécurité). [#90a5dff](https://github.com/suitenumerique/drive/commit/90a5dff)
- Ajout de documentation sur la réconciliation des comptes utilisateurs. [#9995a2a](https://github.com/suitenumerique/drive/commit/9995a2a)
- Amélioration des tests pour les CTA publiques. [#f17d7a8](https://github.com/suitenumerique/drive/commit/f17d7a8) et [#bdf6c29](https://github.com/suitenumerique/drive/commit/bdf6c29)
- Ajout de tests E2E pour le flux de conversion. [#302bff1](https://github.com/suitenumerique/drive/commit/302bff1)
