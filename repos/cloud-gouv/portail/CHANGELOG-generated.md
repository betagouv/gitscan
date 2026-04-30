## Changelog : portail (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse et les fonctionnalités du serveur RPC, ainsi que sur l'ajout de tests d'intégration pour améliorer la qualité du code. Des corrections ont été apportées pour éviter les paniques et assurer une configuration TLS correcte.

### Évolutions fonctionnelles
- Le serveur RPC prend désormais en charge les groupes supplémentaires, permettant une gestion plus fine des permissions et de l'accès. [#76](https://github.com/cloud-gouv/portail/issues/76)
- Ajout d'un test E2E pour le proxy upstream Tinyproxy, validant son intégration et son bon fonctionnement. [#70](https://github.com/cloud-gouv/portail/issues/70)

### Évolutions techniques
- Correction d'une potentielle panique en supprimant l'utilisation de `unwrap()` dans le code. [#76](https://github.com/cloud-gouv/portail/issues/76)
- Correction d'un problème de configuration TLS où le nom du serveur était manquant, assurant une connexion sécurisée. [#75](https://github.com/cloud-gouv/portail/issues/75)
- Ajout de commandes CI Cargo pour automatiser les processus de construction et de test. [#68](https://github.com/cloud-gouv/portail/issues/68)

### Autres changements
- Mise à jour de certaines dépendances :
    - `actions/checkout` vers la version 4.3.1
    - `annotate-snippets` vers la version 0.12.15
    - `tokio` vers la version 1.52.1
    - `zlink` vers les versions 0.4.1 et 0.4.2
