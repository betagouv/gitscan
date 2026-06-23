## Changelog : menshen (30 derniers jours, au 22 juin 2026)

### Résumé
Ce mois-ci, le projet Menshen a connu une refonte significative de son architecture interne, notamment en adoptant `msgspec` pour la sérialisation et la structuration des données. Ces changements visent à améliorer la performance et la maintenabilité du code. De plus, la fonctionnalité d'échange de jetons a été enrichie avec l'ajout des "grants" dans la réponse, et une meilleure gestion des requêtes a été implémentée via un nouveau service dédié.

### Évolutions fonctionnelles
- Ajout des "grants" dans la réponse de l'échange de jetons, offrant plus de flexibilité et d'informations aux clients.
- Amélioration de la gestion des requêtes d'échange de jetons grâce à l'introduction d'un service dédié.
- Suppression du *feature flag* `TOKEN_EXCHANGE_ENABLED`, la fonctionnalité étant désormais activée par défaut.

### Évolutions techniques
- Mise à jour de la version de Python à 3.14.6 [#ab12175](https://github.com/suitenumerique/menshen/commit/ab12175).
- Refonte de la gestion des structures de données en utilisant `msgspec.Struc` pour améliorer la performance et la clarté du code [#60bf50a](https://github.com/suitenumerique/menshen/commit/60bf50a).
- Migration des sérializers vers des structures `msgspec` [#dac2ee9](https://github.com/suitenumerique/menshen/commit/dac2ee9).
- Déplacement du module `token_generator` vers le répertoire `services.token` pour une meilleure organisation [#80bf387](https://github.com/suitenumerique/menshen/commit/80bf387).
- Suppression des dépendances `drf-standardized-errors` et `annotated-types` pour alléger le projet [#5add6ac](https://github.com/suitenumerique/menshen/commit/5add6ac) et [#60fa40c](https://github.com/suitenumerique/menshen/commit/60fa40c).
- Ajout de tests pour les modèles `token_exchange` et le service de gestion des requêtes d'échange de jetons [#ca2fb77](https://github.com/suitenumerique/menshen/commit/ca2fb77) et [#adf3c38](https://github.com/suitenumerique/menshen/commit/adf3c38).
- Automatisation de la génération des variables d'environnement pour le développement et la CI [#449a218](https://github.com/suitenumerique/menshen/commit/449a218).

### Autres changements
- Ajout du support des types (type hints) [#a4a120f](https://github.com/suitenumerique/menshen/commit/a4a120f).
- Suppression d'arguments inutilisés de la méthode `TokenGenerator.generate_jwt` [#851d5b5](https://github.com/suitenumerique/menshen/commit/851d5b5).
- Mises à jour des dépendances Docker (ghcr.io/astral-sh/uv, alpine/openssl) et des actions GitHub.
