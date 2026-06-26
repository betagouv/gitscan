## Changelog : menshen (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, le projet Menshen a connu des améliorations significatives en termes de performance et de structure interne. L'utilisation d'Uvicorn pour la production et l'adoption de `msgspec` pour la sérialisation et la structuration des données visent à optimiser la vitesse et l'efficacité du serveur d'autorisation. De plus, la suppression de certaines dépendances et l'organisation du code en services améliorent la maintenabilité du projet.

### Évolutions fonctionnelles
- Ajout des "grants" à la réponse de l'échange de jetons, offrant plus de flexibilité et de contrôle sur les autorisations.
- Amélioration de la gestion des requêtes d'échange de jetons en les déplaçant vers un service dédié pour une meilleure organisation et testabilité.
- Suppression du "feature flag" `TOKEN_EXCHANGE_ENABLED`, indiquant que l'échange de jetons est maintenant pleinement activé et stable.

### Évolutions techniques
- Passage à Python 3.14.6 pour bénéficier des dernières optimisations et corrections de sécurité.
- Utilisation d'Uvicorn pour l'exécution en production, améliorant les performances et la scalabilité. [#9414c22](https://github.com/suitenumerique/menshen/commit/9414c22)
- Refactorisation du code pour utiliser `msgspec` pour les structures de données et la sérialisation, optimisant la performance et réduisant les dépendances. [#60bf50a](https://github.com/suitenumerique/menshen/commit/60bf50a), [#dac2ee9](https://github.com/suitenumerique/menshen/commit/dac2ee9)
- Suppression des dépendances `drf-standardized-errors` et `annotated-types` pour alléger le projet et simplifier la gestion des dépendances. [#5add6ac](https://github.com/suitenumerique/menshen/commit/5add6ac), [#60fa40c](https://github.com/suitenumerique/menshen/commit/60fa40c)
- Déplacement du module `token_generator` vers `services.token` pour une meilleure organisation du code. [#80bf387](https://github.com/suitenumerique/menshen/commit/80bf387)
- Amélioration de la structure des tests pour l'échange de jetons, en adoptant le pattern LaSuite. [#48dfce5](https://github.com/suitenumerique/menshen/commit/48dfce5)

### Autres changements
- Ajout d'un workflow pour la publication des images Docker. [#e6246c2](https://github.com/suitenumerique/menshen/commit/e6246c2)
- Automatisation de la génération des variables d'environnement pour le développement et la CI. [#449a218](https://github.com/suitenumerique/menshen/commit/449a218)
- Ajout de tests pour les modèles `token_exchange`. [#ca2fb77](https://github.com/suitenumerique/menshen/commit/ca2fb77)
- Ajout de support pour les types. [#a4a120f](https://github.com/suitenumerique/menshen/commit/a4a120f)
- Suppression d'arguments inutilisés de `TokenGenerator.generate_jwt`. [#851d5b5](https://github.com/suitenumerique/menshen/commit/851d5b5)
