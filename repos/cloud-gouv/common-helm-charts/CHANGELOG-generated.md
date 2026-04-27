## Changelog : common-helm-charts (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les charts Helm ont bénéficié d'améliorations concernant la publication en OCI, la gestion des secrets externes, et la correction de bugs liés à Restic et à la configuration des jobs CI. Des optimisations ont également été apportées pour améliorer la stabilité et la performance des déploiements.

### Évolutions fonctionnelles
- Possibilité d'utiliser des secrets externes pour les charts, offrant une plus grande flexibilité et sécurité dans la gestion des informations sensibles. [#15](https://github.com/cloud-gouv/common-helm-charts/issues/15)
- Correction d'un bug empêchant le déverrouillage correct de Restic. [#13](https://github.com/cloud-gouv/common-helm-charts/issues/13)

### Évolutions techniques
- Ajout de la publication des charts au format OCI lors des releases, facilitant leur distribution et leur utilisation dans différents environnements. [#12](https://github.com/cloud-gouv/common-helm-charts/issues/12)
- Suppression d'une limite CPU inutile dans certains charts, améliorant potentiellement les performances. [#11](https://github.com/cloud-gouv/common-helm-charts/issues/11)
- Correction du nom de l'application cible dans le chart Copier. [#8](https://github.com/cloud-gouv/common-helm-charts/issues/8) et [#14](https://github.com/cloud-gouv/common-helm-charts/issues/14)
- Désactivation temporaire des jobs CI HTTP pour résoudre des problèmes de stabilité.

### Autres changements
- Nettoyage général du code.
- Mise à jour de l'index de documentation et des packages.
- Correction du nom de la cible "app" dans certains charts. [#11](https://github.com/cloud-gouv/common-helm-charts/issues/11) et [#8](https://github.com/cloud-gouv/common-helm-charts/issues/8)
