## Changelog : menshen (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la mise en place de la fonctionnalité d'échange de jetons OAuth 2.0, qui constitue le cœur de métier de Menshen. Des améliorations ont également été apportées à l'infrastructure et aux outils de développement pour faciliter le déploiement et la maintenance du projet.

### Évolutions fonctionnelles
- Implémentation d'une première version de l'échange de jetons OAuth 2.0 [#9c84614](https://github.com/suitenumerique/menshen/commit/9c84614).
- Refactorisation des applications pour organiser le code autour de la fonctionnalité d'échange de jetons [#cfdc37f](https://github.com/suitenumerique/menshen/commit/cfdc37f), [#2396221](https://github.com/suitenumerique/menshen/commit/2396221).

### Évolutions techniques
- Ajout d'un healthcheck pour le service Docker, permettant de vérifier la disponibilité du serveur [#6b242d2](https://github.com/suitenumerique/menshen/commit/6b242d2).
- Le nom du service Docker a été renommé en `menshen` pour plus de clarté [#7fd622d](https://github.com/suitenumerique/menshen/commit/7fd622d).
- Configuration du serveur pour créer un superutilisateur via les variables d'environnement [#07ab956](https://github.com/suitenumerique/menshen/commit/07ab956).
- Suppression des paramètres liés à OIDC qui ne sont plus utilisés [#77bf3e4](https://github.com/suitenumerique/menshen/commit/77bf3e4).
- Amélioration de l'affichage de l'aide de la commande `make` [#50e4ece](https://github.com/suitenumerique/menshen/commit/50e4ece).
- Ajout d'un environnement de "playground" pour le projet [#2d94c9b](https://github.com/suitenumerique/menshen/commit/2d94c9b).

### Autres changements
- Mise à jour des dépendances Python et Docker (Keycloak, UV, GitHub Actions) via Renovate. Ces mises à jour sont automatiques et visent à maintenir la sécurité et la stabilité du projet.
