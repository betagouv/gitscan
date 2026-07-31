## Changelog : menshen (30 derniers jours, au 29 juillet 2026)

### Résumé
Les 30 derniers jours ont été marqués par une refonte significative de l'architecture backend de menshen, avec le passage de Django REST Framework à Django Ninja pour une meilleure performance et maintenabilité. De plus, l'intégration d'un chart Helm a été réalisée pour faciliter le déploiement et la gestion de l'application en Kubernetes.

### Évolutions fonctionnelles
- Ajout d'une base pour un client API permettant l'interaction avec le serveur d'autorisation.
- Amélioration des messages d'avertissement lorsque des scopes supplémentaires sont demandés lors des échanges de jetons.
- Correction d'un bug qui restreignait le scope de l'échange de jetons dans le playground à `openid`.
- Correction de bugs liés au content-type des requêtes d'échange de jetons (maintenant forcé à JSON) et à la gestion des champs supplémentaires dans les réponses d'introspection de jetons.

### Évolutions techniques
- Migration de l'API REST de Django REST Framework vers Django Ninja pour une meilleure performance et une syntaxe plus moderne [#822aeed](https://github.com/suitenumerique/menshen/commit/822aeed).
- Refactorisation du service de validation des jetons et de l'introspection des jetons échangés pour une meilleure organisation du code.
- Déplacement de la logique de révocation de jetons vers un service dédié.
- Factorisation des utilitaires principaux du service dans un mixin pour éviter la duplication de code.
- Ajout de support pour un pool de connexions PostgreSQL pour améliorer les performances.
- Intégration d'un chart Helm pour simplifier le déploiement Kubernetes et automatiser les workflows associés [#6f1dddc](https://github.com/suitenumerique/menshen/commit/6f1dddc).
- Ajout de workflows CI/CD pour le linting et la publication du chart Helm.
- Utilisation d'Uvicorn comme serveur d'application.
- Bundle des fichiers statiques dans l'image Docker.
- Mise à jour de la commande de lancement en production.

### Autres changements
- Ajout de `django.extra` à `sentry-sdk` pour une meilleure intégration avec Sentry.
- Suppression des paramètres OIDC inutilisés.
- Correction d'une erreur d'importation de module.
- Suppression du suffixe "Enum" des énumérations pour une meilleure cohérence du code.
- Correction d'une erreur de copier/coller dans le playground.
- Bump de version à 0.2.0 et 0.1.0.
