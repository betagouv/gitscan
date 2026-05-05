## Changelog : menshen (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'implémentation initiale de la fonctionnalité d'échange de jetons OAuth 2.0, une des fonctions principales du projet. Des améliorations ont également été apportées à l'environnement de développement et au processus de construction du projet.

### Évolutions fonctionnelles
- **Implémentation initiale de l'échange de jetons:** Une première version de l'échange de jetons OAuth 2.0 est maintenant disponible. [#9c84614](https://github.com/suitenumerique/menshen/commit/9c84614)
- **Création d'un superutilisateur simplifiée:** La création d'un superutilisateur se fait désormais via les variables d'environnement, facilitant la configuration initiale. [#07ab956](https://github.com/suitenumerique/menshen/commit/07ab956)

### Évolutions techniques
- **Refactoring des applications:** L'application `tx` a été renommée et déplacée vers un nouveau module `token_exchange` pour une meilleure organisation du code. [#cfdc37f](https://github.com/suitenumerique/menshen/commit/cfdc37f), [#2396221](https://github.com/suitenumerique/menshen/commit/2396221), [#dabb7a2](https://github.com/suitenumerique/menshen/commit/dabb7a2)
- **Healthcheck Docker:** Ajout d'un healthcheck au service Docker pour une meilleure gestion de la disponibilité du conteneur. [#6b242d2](https://github.com/suitenumerique/menshen/commit/6b242d2)
- **Amélioration de l'aide de `make`:** L'affichage de l'aide de la commande `make` a été amélioré pour une meilleure lisibilité. [#50e4ece](https://github.com/suitenumerique/menshen/commit/50e4ece)
- **Playground du projet:** Ajout d'un environnement de test (playground) pour faciliter l'expérimentation avec le projet. [#2d94c9b](https://github.com/suitenumerique/menshen/commit/2d94c9b)
- **Renommage du service Docker:** Le service Docker a été renommé en `menshen` pour plus de clarté. [#7fd622d](https://github.com/suitenumerique/menshen/commit/7fd622d)

### Autres changements
- Mise à jour de la documentation et de la configuration du projet.
- Mises à jour mineures des dépendances (renovate bot).
