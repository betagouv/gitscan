## Changelog : account-manager (30 derniers jours, au 16 septembre 2026)

### Résumé
Ce mois-ci, l'outil a franchi une étape majeure dans l'automatisation du cycle de vie des accès. L'accent a été mis sur la gestion structurée des arrivées et des départs (onboarding/offboarding), la gestion des exceptions via un système de dérogations, et l'intégration de nouveaux types de comptes (comptes machines). L'interface de pilotage a également été enrichie pour offrir une meilleure visibilité sur l'état des accès et des collectes de données.

### Évolutions fonctionnelles
- **Gestion du cycle de vie (Onboarding/Offboarding) :**
    - Mise en place de plans d'arrivée et de départ avec suivi des étapes, possibilité d'annulation et clôture de dossiers ([#56](https://github.com/incubateur-ademe/account-manager/issues/56), [#54](https://github.com/incubateur-ademe/account-manager/issues/54), [#27](https://github.com/incubateur-ademe/account-manager/issues/27), [#31](https://github.com/incubateur-ademe/account-manager/issues/31)).
    - Automatisation de la confrontation entre les actions déclarées et les observations réelles ([#8](https://github.com/incubateur-ademe/account-manager/issues/8)).
- **Gestion des accès et des comptes :**
    - Introduction de la gestion des comptes machines et des comptes isolés ([#106](https://github.com/incubateur-ademe/account-manager/issues/106), [#105](https://github.com/incubateur-ademe/account-manager/issues/105), [#41](https://github.com/incubateur-ademe/account-manager/issues/41)).
    - Nouveau système de gestion des équipes traitées comme des accès ([#28](https://github.com/incubateur-ademe/account-manager/issues/28), [#32](https://github.com/incubateur-ademe/account-manager/issues/32)).
    - Gestion des droits nominatifs pour les non-opérateurs ([#75](https://github.com/incubateur-ademe/account-manager/issues/75)).
- **Pilotage et administration :**
    - Nouveau tableau de bord centralisant les données des connecteurs ([#47](https://github.com/incubateur-ademe/account-manager/issues/47)).
    - Interface permettant de lancer des collectes de données et de consulter l'historique des exécutions ([#85](https://github.com/incubateur-ademe/account-manager/issues/85)).
    - Gestion des dérogations permettant de tolérer certains systèmes ou d'écarter des écarts du plan ([#98](https://github.com/incubateur-ademe/account-manager/issues/98), [#95](https://github.com/incubateur-ademe/account-manager/issues/95), [#94](https://github.com/incubateur-ademe/account-manager/issues/94), [#92](https://github.com/incubateur-ademe/account-manager/issues/92)).
    - Prise en charge du traitement des membres des startups ([#43](https://github.com/incubateur-ademe/account-manager/issues/43)).
    - Possibilité de régler la configuration directement depuis l'outil ([#104](https://github.com/incubateur-ademe/account-manager/issues/104)).

### Évolutions techniques
- **Architecture et Qualité :**
    - Refonte du modèle de données : transition du concept de "dossier de départ" vers celui de "dossier d'accès" ([#48](https://github.com/incubateur-ademe/account-manager/issues/48)).
    - Uniformisation du vocabulaire métier sur l'ensemble des interfaces ([#84](https://github.com/incubateur-ademe/account-manager/issues/84)).
    - Renforcement de la sécurité via l'amélioration des garde-fous de session et des contrôles de périmètre ([#74](https://github.com/incubateur-ademe/account-manager/issues/74), [#80](https://github.com/incubateur-ademe/account-manager/issues/80)).
- **Infrastructure et Build :**
    - Mise à jour de Next.js vers la version 16.3.5 ([#85](https://github.com/incubateur-ademe/account-manager/issues/85)).
    - Optimisation de l'image Docker, notamment par la réduction de la taille du CLI Prisma ([#99](https://github.com/incubateur-ademe/account-manager/issues/99)).
    - Mise à jour de la CI/CD pour s'affranchir des cibles Node 20 ([#52](https://github.com/incubateur-ademe/account-manager/issues/52)).
- **Tests :**
    - Amélioration de la stratégie de test avec une structure à trois niveaux pour plus de fiabilité ([#83](https://github.com/incubateur-ademe/account-manager/issues/83)).
    - Optimisation des tests de session et de base de données ([#91](https://github.com/incubateur-ademe/account-manager/issues/91), [#89](https://github.com/incubateur-ademe/account-manager/issues/89)).

### Autres changements
- **Documentation :** Mise à jour massive de la documentation technique, incluant les plans d'implémentation, les procédures de sauvegarde, les guides de configuration et les détails d'architecture.
