## Changelog : menshen (30 derniers jours, au 29 avril 2026)

### Résumé
Les dernières évolutions se concentrent sur la mise en place de la fonctionnalité d'échange de jetons OAuth 2.0, qui constitue le cœur de métier de Menshen. Des refactorings ont été effectués pour préparer l'implémentation et organiser le code, notamment en déplaçant les applications liées à l'échange de jetons vers un nouveau module dédié.

### Évolutions fonctionnelles
- Implémentation d'une première version de l'échange de jetons OAuth 2.0. [#9c84614](https://github.com/suitenumerique/menshen/commit/9c84614)
- Préparation du code pour l'échange de jetons en déplaçant l'application `tx` vers le module `token_exchange`. [#cfdc37f](https://github.com/suitenumerique/menshen/commit/cfdc37f), [#2396221](https://github.com/suitenumerique/menshen/commit/2396221)

### Évolutions techniques
- Refactoring du code pour organiser les applications liées à l'échange de jetons. [#cfdc37f](https://github.com/suitenumerique/menshen/commit/cfdc37f), [#2396221](https://github.com/suitenumerique/menshen/commit/2396221)

### Autres changements
- Mise à jour des dépendances Python et Docker (Keycloak, Uvicorn, GitHub Actions). Ces mises à jour sont gérées automatiquement par Renovate.
