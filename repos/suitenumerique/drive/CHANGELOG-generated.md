## Changelog : drive (30 derniers jours, au 29 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de la recherche et du filtrage de fichiers, ainsi que sur l'ajout de la conversion de fichiers hérités (Office) via OnlyOffice. Des améliorations ont également été apportées à la gestion des fichiers en cours d'analyse et à l'expérience utilisateur générale, notamment avec l'ajout de CTAs (Call To Action) pour les fichiers publics.

### Évolutions fonctionnelles
- Ajout de filtres de recherche avancés : possibilité de filtrer par emplacement, type de fichier, contact associé et date de modification. [#21284be](https://github.com/suitenumerique/drive/commit/21284be)
- Ajout de filtres d'explorateur : les filtres sont maintenant contrôlés et séparés pour une meilleure organisation. [#ae60204](https://github.com/suitenumerique/drive/commit/ae60204)
- Ajout de présélections de date de modification : incluant une option "plus d'un an". [#77b3156](https://github.com/suitenumerique/drive/commit/77b3156)
- Ajout de CTAs (Call To Action) pour les fichiers et dossiers publics, permettant aux utilisateurs de comprendre les actions possibles (téléchargement, etc.). [#4adbe9f](https://github.com/suitenumerique/drive/commit/4adbe9f)
- Prise en charge de l'upload de fichiers Grist. [#a4105a3](https://github.com/suitenumerique/drive/commit/a4105a3)
- Ajout d'un modal de conversion de fichiers pour les formats hérités. [#af6ab74](https://github.com/suitenumerique/drive/commit/af6ab74)
- Affichage des fichiers en cours de conversion dans l'explorateur. [#aeb6c9b](https://github.com/suitenumerique/drive/commit/aeb6c9b)

### Évolutions techniques
- Intégration de OnlyOffice pour la conversion de fichiers Office hérités. Cela inclut la configuration de l'authentification JWT, la gestion des requêtes WOPI et la mise en place d'un service de conversion. [#20596fa](https://github.com/suitenumerique/drive/commit/20596fa) et commits associés.
- Amélioration de la gestion des fichiers en cours d'analyse : possibilité d'accepter les requêtes de conversion pendant l'analyse, et affichage des éléments analysés. [#d49b79a](https://github.com/suitenumerique/drive/commit/d49b79a) et commits associés.
- Optimisation du streaming des fichiers exportés depuis S3 pour éviter le buffering. [#dd7b20b](https://github.com/suitenumerique/drive/commit/dd7b20b)
- Mise à jour de la bibliothèque UI-kit vers la version 0.24.0. [#cc39a65](https://github.com/suitenumerique/drive/commit/cc39a65)
- Amélioration de la gestion des erreurs et des tests E2E.
- Amélioration de la gestion des requêtes WOPI. [#c67cb28](https://github.com/suitenumerique/drive/commit/c67cb28)

### Autres changements
- Amélioration de la documentation README pour plus de clarté. [#f53d80d](https://github.com/suitenumerique/drive/commit/f53d80d)
- Enrichissement des guidelines de contribution. [#1843036](https://github.com/suitenumerique/drive/commit/1843036)
- Correction de problèmes liés aux tests E2E et à la résolution des exports subpaths. [#d0d3083](https://github.com/suitenumerique/drive/commit/d0d3083)
- Mise à jour des dépendances de sécurité (PyJWT et cryptography). [#630209f](https://github.com/suitenumerique/drive/commit/630209f)
