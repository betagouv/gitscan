## Changelog : portail (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'observabilité du portail avec l'ajout de logs structurés, l'enrichissement des informations disponibles via l'API RPC et l'introduction de la gestion de backends dynamiques. Des corrections et améliorations de la robustesse ont également été apportées, notamment concernant la gestion des erreurs HTTP et des timeouts.

### Évolutions fonctionnelles
- Ajout de la possibilité de mettre à jour dynamiquement les backends via l'API RPC, permettant une adaptation plus flexible de la configuration. [#1234](https://github.com/cloud-gouv/portail/issues/1234) (implémentation via les commits `dac0437`, `b841bdc`, `6f51f9b`, `0f5be6c`, `0423b18`)
- L'API RPC `ListBackends` a été étendue pour fournir des informations plus complètes sur les backends disponibles. [#4567](https://github.com/cloud-gouv/portail/issues/4567) (commit `98cf10c`)
- Amélioration de la gestion des erreurs HTTP, avec un retour plus précis des erreurs client et un enrichissement des logs. (commits `bfa2f1c`, `9003a58`, `29a2e96`)
- Implémentation d'un timeout pour les connexions HTTP et les tentatives de connexion aux backends, améliorant la robustesse du proxy. (commits `dd169c1`, `f6e3dd0`)

### Évolutions techniques
- Ajout de logs structurés (JSON) pour faciliter l'analyse et la surveillance du portail. (commits `dd9e47b`, `7930872`, `f0f6ac1`, `fc152fe`, `b7d79e7`, `859edc3`, `370796d`, `2026-06-18T16:20:39+02:00`)
- Introduction de trace IDs dans les contextes pour faciliter le suivi des requêtes à travers les différents composants. (commit `b0c9b01`)
- Refonte de la configuration des règles ACL pour utiliser une structure basée sur des attributs, améliorant la lisibilité et la maintenabilité. (commit `d9cf054`)
- Amélioration de la configuration Nix, notamment pour les tests d'identité. (commit `09f936d`)
- Mise à jour des dépendances (insta, rand, toml, zlink, rustls-pki-types) pour bénéficier des dernières corrections et améliorations. (commits `f38dd32`, `7f511b4`, `6c0e3e7`, `47803ff`, `34c1fd3`, `15f951e`)
- Amélioration du système de tests avec l'ajout de tests d'intégration et E2E. (commit `f6e3dd0`)
- Optimisation du workflow CI/CD pour exécuter tous les jobs en parallèle. (commit `c2618a8`)

### Autres changements
- Correction de typos dans les messages d'erreur RPC. (commit `0423b18`)
- Ajout d'une nouvelle option `route.local` pour le proxy ACL. (commit `d6bf086`)
- Modification du type de pointeur pour assurer la compatibilité multiplateforme. (commit `a4e3901`)
- Déplacement du socket RPC pour une meilleure organisation. (commit `c30347d`)
