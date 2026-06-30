## Changelog : menshen (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, le projet Menshen a connu des améliorations significatives en termes de performance et de structure interne. L'utilisation d'Uvicorn pour la production et la migration vers Python 3.14.6 devraient améliorer la rapidité et la sécurité. Des refactorings importants ont été effectués pour simplifier le code et préparer le projet pour de futures évolutions, notamment en matière de gestion des échanges de jetons OAuth 2.0. La publication des images Docker a également été automatisée.

### Évolutions fonctionnelles
- Ajout des "grants" à la réponse de l'échange de jetons, offrant plus de flexibilité et de contrôle sur les autorisations. [#91ed1f4](https://github.com/suitenumerique/menshen/commit/91ed1f4)
- Suppression du "feature flag" `TOKEN_EXCHANGE_ENABLED`, simplifiant la configuration et activant par défaut la fonctionnalité d'échange de jetons. [#64f8163](https://github.com/suitenumerique/menshen/commit/64f8163)

### Évolutions techniques
- Utilisation d'Uvicorn pour l'exécution en production, améliorant les performances et l'efficacité. [#9414c22](https://github.com/suitenumerique/menshen/commit/9414c22)
- Mise à jour de la version de Python à 3.14.6, bénéficiant des dernières améliorations de sécurité et de performance. [#ab12175](https://github.com/suitenumerique/menshen/commit/ab12175)
- Refactoring du code pour utiliser `msgspec.Struc` pour les structures de données, améliorant la performance et la lisibilité. [#60bf50a](https://github.com/suitenumerique/menshen/commit/60bf50a)
- Migration des serializers vers des structures `msgspec`, optimisant la sérialisation et la désérialisation des données. [#dac2ee9](https://github.com/suitenumerique/menshen/commit/dac2ee9)
- Déplacement de la gestion des requêtes d'échange de jetons vers un service dédié, améliorant l'organisation et la maintenabilité du code. [#c25b12a](https://github.com/suitenumerique/menshen/commit/c25b12a)
- Déplacement du module `token_generator` vers `services.token`, améliorant la structure du projet. [#80bf387](https://github.com/suitenumerique/menshen/commit/80bf387)
- Simplification des tests d'échange de jetons en adoptant le pattern LaSuite. [#48dfce5](https://github.com/suitenumerique/menshen/commit/48dfce5)
- Suppression des dépendances inutiles `drf-standardized-errors` et `annotated-types`, allégeant le projet. [#5add6ac](https://github.com/suitenumerique/menshen/commit/5add6ac) et [#60fa40c](https://github.com/suitenumerique/menshen/commit/60fa40c)

### Autres changements
- Ajout d'un workflow pour la publication automatique des images Docker sur GitHub Container Registry. [#e6246c2](https://github.com/suitenumerique/menshen/commit/e6246c2)
- Ajout de tests pour les modèles d'échange de jetons. [#ca2fb77](https://github.com/suitenumerique/menshen/commit/ca2fb77)
- Ajout de tests pour le service de gestion des requêtes d'échange de jetons. [#adf3c38](https://github.com/suitenumerique/menshen/commit/adf3c38)
- Mises à jour des dépendances GitHub Actions et Docker. (renovate[bot])
