## Changelog : datagouv_client (30 derniers jours, au 20 mai 2026)

### Résumé
Les dernières mises à jour de `datagouv_client` se concentrent sur l'ajout d'une interface en ligne de commande (CLI) pour interagir avec l'API data.gouv.fr, améliorant ainsi l'accessibilité et la facilité d'utilisation pour les développeurs. Des corrections ont également été apportées pour gérer des cas spécifiques de l'API et améliorer la robustesse de la bibliothèque.

### Évolutions fonctionnelles
- Ajout d'une interface en ligne de commande (CLI) permettant d'effectuer des opérations sur les objets de l'API data.gouv.fr, notamment une méthode `get` pour récupérer des données. [#48](https://github.com/datagouv/datagouv_client/pull/48)
- La CLI permet désormais de rester anonyme lors de la simple récupération de données. [#52](https://github.com/datagouv/datagouv_client/pull/52)
- Correction d'un problème lié à l'URL de l'API Tabular sur l'environnement de démonstration. [#49](https://github.com/datagouv/datagouv_client/pull/49)
- Gestion de l'absence inattendue de l'API Tabular. [#56](https://github.com/datagouv/datagouv_client/pull/56)
- Ajout d'un alias `prod` pour `www` afin de simplifier l'utilisation de l'API de production. [#50](https://github.com/datagouv/datagouv_client/pull/50)

### Évolutions techniques
- Ajout d'en-têtes `User-Agent` pour identifier le client lors des requêtes API. [#55](https://github.com/datagouv/datagouv_client/pull/55)
- Correction de l'environnement dans l'URI utilisé par la CLI. [#51](https://github.com/datagouv/datagouv_client/pull/51)
