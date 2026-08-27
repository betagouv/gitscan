## Changelog : account-manager (30 derniers jours, au 25 août 2026)

### Résumé
Ce mois-ci, l'outil a franchi une étape majeure en automatisant les processus d'accueil et de départ des utilisateurs. Grâce à la mise en place de parcours structurés (plans d'arrivée et de départ) et d'un tableau de bord de suivi, l'administration peut désormais piloter les accès de manière plus fluide, sécurisée et prévisible, tout en bénéficiant d'une meilleure visibilité sur l'état des comptes et des entreprises.

### Évolutions fonctionnelles
- **Automatisation de l'onboarding et l'offboarding** : mise en place de plans d'arrivée et de départ avec des étapes concrètes, incluant une phase de simulation [#56](https://github.com/incubateur-ademe/account-manager/issues/56) et la possibilité d'annuler un départ en cours [#27](https://github.com/incubateur-ademe/account-manager/issues/27).
- **Pilotage des accès** : les dossiers sont désormais utilisés pour gérer les mouvements d'accès [#51](https://github.com/incubateur-ademe/account-manager/issues/51) et les équipes sont traitées comme des entités de gestion des droits [#28](https://github.com/incubateur-ademe/account-manager/issues/28).
- **Supervision et visibilité** : ajout d'un tableau de bord centralisant les données des connecteurs [#47](https://github.com/incubateur-ademe/account-manager/issues/47), d'un historique des exécutions [#8514bb6](https://github.com/incubateur-ademe/account-manager/issues/8514bb6) et d'un écran récapitulatif des capacités du système [#2c681e8](https://github.com/incubateur-ademe/account-manager/issues/2c681e8).
- **Gestion des entités** : amélioration du traitement des membres de startups et de la gestion des comptes isolés [#41](https://github.com/incubateur-ademe/account-manager/issues/41), [#43](https://github.com/incubateur-ademe/account-manager/issues/43).
- **Améliorations de l'interface** : possibilité d'agir sur un constat sans quitter la fiche utilisateur [#26](https://github.com/incubateur-ademe/account-manager/issues/26) et correction de l'affichage des messages d'obligation [#09061dd](https://github.com/incubateur-ademe/account-manager/issues/09061dd).

### Évolutions techniques
- **Architecture des connecteurs** : évolution du modèle pour permettre aux connecteurs de délivrer des accès basés sur les profils utilisateurs [#55](https://github.com/incubateur-ademe/account-manager/issues/55).
- **Optimisation de l'infrastructure et CI/CD** : réduction de la taille de l'image Docker en optimisant les dépendances Prisma [f2149d7](https://github.com/incubateur-ademe/account-manager/issues/f2149d7), mise à jour des workflows pour les nouvelles versions de Node [52a00b9](https://github.com/incubateur-ademe/account-manager/issues/52a00b9) et automatisation de la récupération des politiques de sécurité lors du build [#2a1e6ba](https://github.com/incubateur-ademe/account-manager/issues/2a1e6ba).
- **Refactoring et maintenance** : renommage de composants pour plus de cohérence (ex: passage du "dossier de départ" au "dossier d'accès" [#48](https://github.com/incubateur-ademe/account-manager/issues/48)) et standardisation des noms techniques en anglais [97de2b2](https://github.com/incubateur-ademe/account-manager/issues/97de2b2).
- **Configuration** : refactorisation de la gestion des envois d'emails (SMTP) [9f5488b](https://github.com/incubateur-ademe/account-manager/issues/9f5488b).

### Autres changements
- **Documentation** : enrichissement important de la documentation technique, incluant les plans d'implémentation, les procédures de restauration de sauvegarde et les explications sur la configuration des variables d'environnement (Coolify, POLICY_DIR).
