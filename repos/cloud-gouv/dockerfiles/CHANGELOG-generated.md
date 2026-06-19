## Changelog : dockerfiles (30 derniers jours, au 2026-06-19)

### Résumé
Ce dépôt a récemment été mis à jour pour améliorer la compatibilité et la fonctionnalité de plusieurs images Docker fournies. Les changements incluent une mise à jour majeure de `clusterctl` et l'ajout de `golang` à l'image des runners GitLab, permettant ainsi une plus grande flexibilité pour les utilisateurs. Des corrections mineures ont également été apportées pour assurer la stabilité des images.

### Évolutions fonctionnelles
- Ajout de `golang` à l'image Docker des runners GitLab, offrant ainsi un environnement de build plus complet.  [#30](https://github.com/cloud-gouv/dockerfiles/issues/30)
- Mise à jour de `clusterctl` de la version 1.8.10 à la version 1.13.1, apportant de nouvelles fonctionnalités et corrections. [#35](https://github.com/cloud-gouv/dockerfiles/issues/35)

### Évolutions techniques
- Correction des sommes SHA des actions utilisées dans les Dockerfiles pour garantir l'intégrité des builds. [#36](https://github.com/cloud-gouv/dockerfiles/issues/36)
