## Changelog : ds_proxy (30 derniers jours, au 6 juillet 2026)

### Résumé
Les dernières mises à jour de ds_proxy améliorent la flexibilité de la configuration, notamment en ajoutant la prise en charge de S3 et Swift, et en permettant de spécifier le chemin du socket. Des corrections de bugs et des optimisations de dépendances ont également été apportées pour améliorer la stabilité et la performance.

### Évolutions fonctionnelles
- Ajout de la prise en charge de S3 et Swift avec détection automatique du type de stockage par requête. [#158](https://github.com/demarche-numerique/ds_proxy/pull/158)
- Possibilité de spécifier le chemin du socket via un nouveau paramètre de configuration. [#159](https://github.com/demarche-numerique/ds_proxy/pull/159)
- Correction d'un bug empêchant l'écriture correcte des URLs presigned S3. [#156](https://github.com/demarche-numerique/ds_proxy/pull/156)
- Correction d'une erreur dans la documentation concernant le flag `--upstream-url`. [#157](https://github.com/demarche-numerique/ds_proxy/pull/157)
- Ajout d'exemples de configuration pour Rails et rclone dans la documentation. [#155](https://github.com/demarche-numerique/ds_proxy/pull/155)

### Évolutions techniques
- Refactorisation de la configuration S3 pour une meilleure organisation. [#162](https://github.com/demarche-numerique/ds_proxy/pull/162)
- Simplification des dépendances du projet, notamment en supprimant des dépendances inutiles et en allégeant les dépendances AWS. [#161](https://github.com/demarche-numerique/ds_proxy/pull/161), [#160](https://github.com/demarche-numerique/ds_proxy/pull/160), [#152](https://github.com/demarche-numerique/ds_proxy/pull/152)
- Introduction d'une méthode `apply_connect_url` pour gérer la connexion à l'upstream. [#153](https://github.com/demarche-numerique/ds_proxy/pull/153)
- Suppression du header `content-md5` qui était altéré par le proxy. [#150](https://github.com/demarche-numerique/ds_proxy/pull/150)

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et configurations.
- Mises à jour de dépendances mineures.
