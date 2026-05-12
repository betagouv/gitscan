## Changelog : menshen (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'implémentation initiale de l'échange de jetons OAuth 2.0, une fonctionnalité clé du projet. Des améliorations ont également été apportées à l'infrastructure de développement, notamment l'ajout de vérifications de santé pour les conteneurs Docker et l'amélioration de l'aide de la commande `make`.

### Évolutions fonctionnelles
- Implémentation d'une première version de l'échange de jetons OAuth 2.0 [#9c84614](https://github.com/suitenumerique/menshen/commit/9c84614).
- Renommage du service Docker en `menshen` pour une meilleure clarté [#7fd622d](https://github.com/suitenumerique/menshen/commit/7fd622d).

### Évolutions techniques
- Ajout d'une vérification de santé pour le service Docker, améliorant la robustesse et la surveillance de l'application [#6b242d2](https://github.com/suitenumerique/menshen/commit/6b242d2).
- Amélioration de l'affichage de l'aide de la commande `make` pour une meilleure expérience développeur [#50e4ece](https://github.com/suitenumerique/menshen/commit/50e4ece).
- Modification de la configuration pour utiliser les variables d'environnement pour la création d'un superutilisateur, augmentant la flexibilité et la sécurité [#07ab956](https://github.com/suitenumerique/menshen/commit/07ab956).
- Refactorisation du code pour déplacer l'application `tx` vers le module `token_exchange` [#cfdc37f](https://github.com/suitenumerique/menshen/commit/cfdc37f) et [#2396221](https://github.com/suitenumerique/menshen/commit/2396221).
- Suppression des paramètres liés à OIDC qui ne sont plus utilisés [#77bf3e4](https://github.com/suitenumerique/menshen/commit/77bf3e4).

### Autres changements
- Ajout d'un "playground" pour le projet, facilitant l'exploration et le test de l'API [#2d94c9b](https://github.com/suitenumerique/menshen/commit/2d94c9b).
- Mises à jour automatiques des dépendances via Renovate (Python, Docker, GitHub Actions, etc.). Ces mises à jour sont de routine et n'impactent pas directement l'utilisation du logiciel.
