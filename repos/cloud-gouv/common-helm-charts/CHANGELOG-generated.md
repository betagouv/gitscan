## Changelog : common-helm-charts (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les mises à jour se concentrent sur l'amélioration de la flexibilité et de la robustesse des charts Helm. Des correctifs ont été apportés pour résoudre des problèmes de déverrouillage de Restic et de configuration du CI, tandis que de nouvelles fonctionnalités permettent l'utilisation de secrets externes et l'ajout de publication OCI lors des releases.

### Évolutions fonctionnelles
- Possibilité d'utiliser des secrets externes pour les charts. [#15](https://github.com/cloud-gouv/common-helm-charts/issues/15)
- Correction d'un problème de déverrouillage de Restic. [#13](https://github.com/cloud-gouv/common-helm-charts/issues/13)
- Correction de l'application du nom cible des applications.

### Évolutions techniques
- Ajout de la publication OCI lors des releases, améliorant le processus de déploiement. [#12](https://github.com/cloud-gouv/common-helm-charts/issues/12)
- Suppression d'une limite CPU inutile dans un chart. [#11](https://github.com/cloud-gouv/common-helm-charts/issues/11)
- Désactivation temporaire du CI et mise à jour de l'index de développement pour améliorer la stabilité.
- Correction de la configuration du CI pour éviter des erreurs.

### Autres changements
- Nettoyage général du code.
- Mise à jour de l'index de documentation et des packages.
