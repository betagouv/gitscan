## Changelog : menshen (30 derniers jours, au 2 juillet 2026)

### Résumé
Ce mois-ci, le projet Menshen a connu des avancées significatives en termes de déploiement et de développement. L'ajout d'un chart Helm permet une gestion simplifiée du déploiement Kubernetes, tandis que des optimisations internes améliorent la performance et la structure du code, notamment avec l'adoption de `msgspec` pour la sérialisation et la suppression de dépendances inutiles.

### Évolutions fonctionnelles
- Ajout des "grants" à la réponse de l'échange de jetons, offrant plus de flexibilité et de contrôle sur les autorisations.
- Amélioration de la gestion des requêtes d'échange de jetons en introduisant un service dédié.
- Suppression du *feature flag* `TOKEN_EXCHANGE_ENABLED`, simplifiant la configuration et activant la fonctionnalité par défaut.

### Évolutions techniques
- Implémentation d'un chart Helm pour faciliter le déploiement et la gestion de l'application sur Kubernetes [#573a09a](https://github.com/suitenumerique/menshen/commit/573a09a).
- Ajout de workflows CI/CD pour le linting et la publication du chart Helm [#6f1dddc](https://github.com/suitenumerique/menshen/commit/6f1dddc).
- Automatisation et documentation du développement basé sur Kubernetes [#7b027c6](https://github.com/suitenumerique/menshen/commit/7b027c6).
- Support du *connection pooling* pour PostgreSQL, améliorant la performance et la gestion des connexions à la base de données [#5840f47](https://github.com/suitenumerique/menshen/commit/5840f47).
- Utilisation de Uvicorn pour l'exécution en production, optimisant les performances du serveur [#9414c22](https://github.com/suitenumerique/menshen/commit/9414c22).
- Migration des sérializers vers des structures `msgspec`, améliorant la performance et la concision du code [#dac2ee9](https://github.com/suitenumerique/menshen/commit/dac2ee9).
- Refactorisation des tests pour adopter le pattern LaSuite [#48dfce5](https://github.com/suitenumerique/menshen/commit/48dfce5).
- Suppression des dépendances `drf-standardized-errors` et `annotated-types`, allégeant le projet et réduisant les risques de conflits [#60bf50a](https://github.com/suitenumerique/menshen/commit/60bf50a), [#60fa40c](https://github.com/suitenumerique/menshen/commit/60fa40c).
- Mise à jour de la version de Python à 3.14.6 [#ab12175](https://github.com/suitenumerique/menshen/commit/ab12175).
- Déplacement du module `token_generator` vers `services.token` pour une meilleure organisation du code [#80bf387](https://github.com/suitenumerique/menshen/commit/80bf387).

### Autres changements
- Publication des images Docker via un workflow CI/CD [#e6246c2](https://github.com/suitenumerique/menshen/commit/e6246c2).
- Bundle des fichiers statiques dans l'image Docker [#af7fd64](https://github.com/suitenumerique/menshen/commit/af7fd64).
- Ajout des paramètres OIDC manquants [#5e30abc](https://github.com/suitenumerique/menshen/commit/5e30abc).
- Correction d'une erreur de copier/coller dans le playground [#f76e461](https://github.com/suitenumerique/menshen/commit/f76e461).
- Ajout de tests pour les modèles `token_exchange` [#ca2fb77](https://github.com/suitenumerique/menshen/commit/ca2fb77).
- Ajout de tests pour le service de requête d'échange de jetons [#adf3c38](https://github.com/suitenumerique/menshen/commit/adf3c38).
