## Changelog : dockerfiles (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les mises à jour du dépôt se concentrent sur l'amélioration de la gestion des versions des outils inclus dans les images Docker, notamment `clusterctl`, et l'ajout de `golang` à l'image `gitlab-runner`. Ces changements visent à fournir des environnements de développement et d'exécution plus récents et plus complets.

### Évolutions fonctionnelles
- Ajout de `golang` à l'image Docker `gitlab-runner` pour faciliter l'exécution de projets Go.  [#30](https://github.com/cloud-gouv/dockerfiles/issues/30)
- Mise à jour de `clusterctl` de la version 1.8.10 à la version 1.13.1, offrant ainsi les dernières fonctionnalités et corrections de bugs. [#35](https://github.com/cloud-gouv/dockerfiles/issues/35)

### Évolutions techniques
- Correction des sommes SHA des actions utilisées dans les Dockerfiles pour garantir l'intégrité et la reproductibilité des builds. [#36](https://github.com/cloud-gouv/dockerfiles/issues/36)
