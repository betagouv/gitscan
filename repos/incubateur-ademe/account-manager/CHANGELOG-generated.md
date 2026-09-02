## Changelog : account-manager (30 derniers jours, au 31 août 2026)

### Résumé
Le projet a franchi une étape majeure avec le déploiement des fonctionnalités de gestion des cycles de vie des utilisateurs (arrivées et départs) et la mise en place d'un système de collecte de données. L'outil permet désormais de piloter l'onboarding et l'offboarding de manière structurée, tout en offrant une visibilité accrue sur les accès et les activités via un nouveau tableau de bord.

### Évolutions fonctionnelles
- **Gestion des cycles de vie (Onboarding/Offboarding) :**
    - Mise en place de plans d'arrivée et de départ avec exécution d'étapes et possibilité d'annulation [#27](https://github.com/incubateur-ademe/account-manager/issues/27), [#31](https://github.com/incubateur-ademe/account-manager/issues/31).
    - Capacité de confirmer un plan de départ, de pointer les étapes réalisées et de clore les dossiers [#e3abee6].
    - Gestion spécifique des membres et des startups lors des processus de fin d'activité [#43](https://github.com/incubateur-ademe/account-manager/issues/43).
- **Pilotage et visibilité :**
    - Création d'un tableau de bord centralisant les données issues des connecteurs [#47](https://github.com/incubateur-ademe/account-manager/issues/47).
    - Interface permettant de lancer des collectes de données et de consulter l'historique des exécutions [#8514bb6].
    - Nouveau système de gestion des "fiches" et des rattachements [#17](https://github.com/incubateur-ademe/account-manager/issues/17).
    - Écran de visibilité sur les capacités opérationnelles de chaque système connecté [#2c681e8].
- **Corrections et améliorations de l'expérience utilisateur :**
    - Sécurisation des actions serveur par une vérification systématique de la session [#74](https://github.com/incubateur-ademe/account-manager/issues/74).
    - Résolution de problèmes d'intégrité des données (échéances, verdicts ou étapes effacés par erreur lors de processus automatiques) [#60](https://github.com/incubateur-ademe/account-manager/issues/60), [#64](https://github.com/incubateur-ademe/account-manager/issues/64).
    - Amélioration de l'interface (gestion de l'hydratation des pages, mode aide et messages d'obligation de saisie) [#22426ef](https://github.com/incubateur-ademe/account-manager/issues/22426ef), [#09061dd].
    - Correction de la gestion des noms composés et des identités.

### Évolutions techniques
- **Architecture et données :**
    - Refactorisation des structures de données : passage du "dossier de départ" au "dossier d'accès" [#48](https://github.com/incubateur-ademe/account-manager/issues/48).
    - Optimisation de la gestion des accès : les équipes sont désormais traitées comme des accès et le reste est géré en métadonnées [#28](https://github.com/incubateur-ademe/account-manager/issues/28), [#32](https://github.com/incubateur-ademe/account-manager/issues/32).
    - Amélioration de la logique des connecteurs pour la gestion des droits d'accès et la remontée de données [#55](https://github.com/incubateur-ademe/account-manager/issues/55).
- **Infrastructure et CI/CD :**
    - Optimisation de l'image Docker (réduction de la taille en retirant les composants Prisma inutiles) [#f2149d7].
    - Mise à jour de la CI pour supporter les nouvelles versions de Node.js [#52a00b9].
    - Stabilisation de l'environnement de déploiement (configuration SMTP, variables Coolify et récupération de la politique au build) [#9f5488b], [#3ee2b18], [#2a1e6ba].
- **Refactoring :**
    - Standardisation du nommage (utilisation de l'anglais pour les éléments techniques et machines) [#97de2b2].
    - Centralisation de la configuration des fournisseurs de périmètre [#09b4fdc].

### Autres changements
- **Documentation :** Mise à jour massive de la documentation technique couvrant l'architecture, les plans d'implémentation, les procédures de sauvegarde et les configurations d'environnement [#71](https://github.com/incubateur-ademe/account-manager/issues/71), [#70](https://github.com/incubateur-ademe/account-manager/issues/70), [#69](https://github.com/incubateur-ademe/account-manager/issues/69), [#3203df0].
- **Processus :** Conventionnalisation des messages de commit/squash pour les Pull Requests [#2696d95].
