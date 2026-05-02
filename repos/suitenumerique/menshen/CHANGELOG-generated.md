## Changelog : menshen (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'implémentation initiale de la fonctionnalité d'échange de jetons OAuth 2.0, qui constitue le cœur de métier de Menshen. Des améliorations ont également été apportées à l'infrastructure du projet, notamment au niveau du Docker et des outils de développement.

### Évolutions fonctionnelles
- Implémentation d'une première version de l'échange de jetons OAuth 2.0 [#9c84614](https://github.com/suitenumerique/menshen/commit/9c84614).
- Refactorisation des applications pour préparer l'implémentation de l'échange de jetons, avec le déplacement de l'application `tx` vers `token_exchange` [#cfdc37f](https://github.com/suitenumerique/menshen/commit/cfdc37f) et [#2396221](https://github.com/suitenumerique/menshen/commit/2396221).

### Évolutions techniques
- Ajout d'un healthcheck pour le service Docker afin de surveiller son bon fonctionnement [#6b242d2](https://github.com/suitenumerique/menshen/commit/6b242d2).
- Modification du nom du service Docker en `menshen` pour plus de clarté [#7fd622d](https://github.com/suitenumerique/menshen/commit/7fd622d).
- Configuration du processus de création d'un superutilisateur via les variables d'environnement [#07ab956](https://github.com/suitenumerique/menshen/commit/07ab956).
- Amélioration de l'affichage de l'aide de la commande `make` [#50e4ece](https://github.com/suitenumerique/menshen/commit/50e4ece).
- Ajout d'un "playground" pour le projet, facilitant les tests et l'exploration [#2d94c9b](https://github.com/suitenumerique/menshen/commit/2d94c9b).

### Autres changements
- Mise à jour des dépendances Python et Docker (Keycloak, UV, GitHub Actions) via Renovate. Ces mises à jour sont automatiques et visent à maintenir la sécurité et la stabilité du projet.
