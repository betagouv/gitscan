## Changelog : menshen (30 derniers jours, au 02 juillet 2026)

### Résumé
Ce mois-ci, le projet menshen a connu des avancées significatives en termes de déploiement et de développement. L'ajout d'un chart Helm permet une gestion simplifiée du déploiement Kubernetes, tandis que des optimisations internes améliorent la performance et la structure du code, notamment avec l'adoption de `msgspec` pour la sérialisation et la suppression de dépendances inutiles.

### Évolutions fonctionnelles
- Ajout de la possibilité de renvoyer les "grants" dans la réponse de l'échange de jetons OAuth 2.0.
- Suppression du *feature flag* `TOKEN_EXCHANGE_ENABLED`, la fonctionnalité étant désormais activée par défaut.
- Amélioration de la gestion des requêtes d'échange de jetons en introduisant un service dédié.

### Évolutions techniques
- Intégration d'un chart Helm pour faciliter le déploiement Kubernetes et éviter les états "out-of-sync" avec ArgoCD [#573a09a](https://github.com/suitenumerique/menshen/commit/573a09a).
- Automatisation et documentation du développement basé sur Kubernetes [#7b027c6](https://github.com/suitenumerique/menshen/commit/7b027c6).
- Ajout du support du *connection pool* pour PostgreSQL [#5840f47](https://github.com/suitenumerique/menshen/commit/5840f47).
- Utilisation de Uvicorn pour l'exécution en production, améliorant potentiellement les performances [#9414c22](https://github.com/suitenumerique/menshen/commit/9414c22).
- Refactorisation du code pour utiliser `msgspec` pour la sérialisation, améliorant la performance et la concision [#60bf50a](https://github.com/suitenumerique/menshen/commit/60bf50a).
- Suppression des dépendances `drf-standardized-errors` et `annotated-types` pour alléger le projet [#5add6ac](https://github.com/suitenumerique/menshen/commit/5add6ac) et [#60fa40c](https://github.com/suitenumerique/menshen/commit/60fa40c).
- Migration des serializers vers des structures `msgspec` [#dac2ee9](https://github.com/suitenumerique/menshen/commit/dac2ee9).
- Refactorisation des tests d'échange de jetons pour adopter le pattern LaSuite [#48dfce5](https://github.com/suitenumerique/menshen/commit/48dfce5).
- Déplacement du module `token_generator` vers le dossier `services.token` [#80bf387](https://github.com/suitenumerique/menshen/commit/80bf387).

### Autres changements
- Ajout de workflows pour le linting et la publication du chart Helm [#6f1dddc](https://github.com/suitenumerique/menshen/commit/6f1dddc).
- Ajout de workflows pour la publication des images Docker [#e6246c2](https://github.com/suitenumerique/menshen/commit/e6246c2).
- Mise à jour de la version de Python à 3.14.6 [#ab12175](https://github.com/suitenumerique/menshen/commit/ab12175).
- Ajout de tests pour les modèles d'échange de jetons [#ca2fb77](https://github.com/suitenumerique/menshen/commit/ca2fb77).
- Ajout de tests pour le service de requête d'échange de jetons [#adf3c38](https://github.com/suitenumerique/menshen/commit/adf3c38).
- Inclusion des fichiers statiques dans l'image Docker [#af7fd64](https://github.com/suitenumerique/menshen/commit/af7fd64).
- Ajout des paramètres OIDC manquants [#5e30abc](https://github.com/suitenumerique/menshen/commit/5e30abc).
- Correction d'une erreur de copier/coller dans le playground [#f76e461](https://github.com/suitenumerique/menshen/commit/f76e461).
