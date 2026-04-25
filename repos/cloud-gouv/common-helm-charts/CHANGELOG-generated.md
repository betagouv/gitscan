## Changelog : common-helm-charts (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les charts Helm ont été améliorés pour offrir plus de flexibilité et de contrôle aux utilisateurs. Des corrections ont été apportées pour améliorer la stabilité, notamment concernant le déverrouillage de Restic et la publication des images OCI. De nouvelles fonctionnalités permettent l'utilisation de secrets externes et la personnalisation du chemin d'accès aux applications.

### Évolutions fonctionnelles
- Possibilité d'utiliser des secrets externes pour les charts. [#15](https://github.com/cloud-gouv/common-helm-charts/issues/15)
- Correction d'un problème empêchant le déverrouillage de Restic. [#13](https://github.com/cloud-gouv/common-helm-charts/issues/13)
- Correction du nom de l'application cible dans le chart Copier. [#12](https://github.com/cloud-gouv/common-helm-charts/issues/12)
- Possibilité de définir un chemin d'accès personnalisé pour les applications. [#4](https://github.com/cloud-gouv/common-helm-charts/issues/4)

### Évolutions techniques
- Ajout de la publication d'images OCI lors des releases. [#12](https://github.com/cloud-gouv/common-helm-charts/issues/12)
- Suppression d'une limite CPU inutile. [#11](https://github.com/cloud-gouv/common-helm-charts/issues/11)
- Désactivation temporaire du CI pour certains workflows et mise à jour de l'index de documentation.

### Autres changements
- Nettoyage du code.
- Mise à jour de l'index de documentation et des packages par les actions automatisées.
