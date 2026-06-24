## Changelog : dockerfiles (30 derniers jours, au 23 juin 2026)

### Résumé
Ce changelog présente les mises à jour récentes des Dockerfiles du projet. Les changements notables incluent une mise à jour majeure de la version de `clusterctl` et l'ajout de `golang` à l'image des runners GitLab, améliorant ainsi la flexibilité et les capacités de déploiement des outils. Des corrections mineures concernant les sommes de contrôle des actions ont également été apportées.

### Évolutions fonctionnelles
- Ajout de `golang` à l'image Docker des runners GitLab, permettant de construire et d'exécuter des projets Go directement dans l'environnement du runner.  [#30](https://github.com/cloud-gouv/dockerfiles/issues/30)
- Mise à jour de la version de `clusterctl` de 1.8.10 à 1.13.1, apportant de nouvelles fonctionnalités et corrections de bugs. [#35](https://github.com/cloud-gouv/dockerfiles/issues/35)

### Évolutions techniques
- Correction des sommes de contrôle (shasum) pour les actions utilisées dans les Dockerfiles, assurant l'intégrité et la sécurité des images. [#36](https://github.com/cloud-gouv/dockerfiles/issues/36)
