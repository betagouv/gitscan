## Changelog : menshen (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, le projet menshen a connu des améliorations significatives en termes de performance et de structure interne. L'utilisation d'Uvicorn pour la production et la migration vers des structures de données `msgspec` optimisent la rapidité et l'efficacité du serveur d'autorisation. De plus, la publication d'images Docker a été automatisée, facilitant le déploiement.

### Évolutions fonctionnelles
- Ajout des "grants" à la réponse de l'échange de jetons, offrant plus de flexibilité. [#91ed1f4](https://github.com/suitenumerique/menshen/commit/91ed1f4)
- Suppression du *feature flag* `TOKEN_EXCHANGE_ENABLED`, simplifiant la configuration et activant définitivement la fonctionnalité d'échange de jetons. [#64f8163](https://github.com/suitenumerique/menshen/commit/64f8163)

### Évolutions techniques
- Utilisation d'Uvicorn pour l'exécution en production, améliorant les performances. [#9414c22](https://github.com/suitenumerique/menshen/commit/9414c22)
- Mise à jour de la version de Python à 3.14.6 pour bénéficier des dernières optimisations et correctifs de sécurité. [#ab12175](https://github.com/suitenumerique/menshen/commit/ab12175)
- Refactorisation du code pour utiliser les structures `msgspec.Struc`, améliorant la performance et réduisant la consommation de mémoire. [#60bf50a](https://github.com/suitenumerique/menshen/commit/60bf50a) et [#dac2ee9](https://github.com/suitenumerique/menshen/commit/dac2ee9)
- Déplacement de la gestion de la requête d'échange de jeton vers un service dédié pour une meilleure organisation du code. [#c25b12a](https://github.com/suitenumerique/menshen/commit/c25b12a)
- Déplacement du module `token_generator` vers `services.token` pour une meilleure organisation. [#80bf387](https://github.com/suitenumerique/menshen/commit/80bf387)
- Suppression des dépendances `drf-standardized-errors` et `annotated-types` pour alléger le projet. [#5add6ac](https://github.com/suitenumerique/menshen/commit/5add6ac) et [#60fa40c](https://github.com/suitenumerique/menshen/commit/60fa40c)
- Amélioration de la structure des tests pour l'échange de jetons, en adoptant le pattern LaSuite. [#48dfce5](https://github.com/suitenumerique/menshen/commit/48dfce5)
- Ajout de tests pour le service de requête d'échange de jetons. [#adf3c38](https://github.com/suitenumerique/menshen/commit/adf3c38)
- Ajout de tests pour les modèles d'échange de jetons. [#ca2fb77](https://github.com/suitenumerique/menshen/commit/ca2fb77)
- Automatisation de la publication des images Docker sur GitHub Container Registry. [#e6246c2](https://github.com/suitenumerique/menshen/commit/e6246c2)

### Autres changements
- Mise à jour des dépendances GitHub Actions. [#965ce32](https://github.com/suitenumerique/menshen/commit/965ce32)
- Mise à jour des dépendances Python. [#9dd879b](https://github.com/suitenumerique/menshen/commit/9dd879b)
- Mise à jour des tags Docker `ghcr.io/astral-sh/uv` et `alpine/openssl`. [#62c648b](https://github.com/suitenumerique/menshen/commit/62c648b) et [#9080805](https://github.com/suitenumerique/menshen/commit/9080805)
