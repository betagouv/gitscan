## Changelog : service-national-universel (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la correction de bugs et l'amélioration de la gestion des dates de mission, ainsi que sur la suppression d'une fonctionnalité obsolète. Une mise à jour de sécurité a également été appliquée pour corriger une vulnérabilité dans la librairie Mongoose.

### Évolutions fonctionnelles
- Mise à jour de la logique de validation et de soumission des dates de mission dans l'interface d'administration et l'API. [#5268](https://github.com/betagouv/service-national-universel/issues/5268)
- Correction de la configuration de la variable d'environnement `JWT_SECRET` pour l'environnement de développement et vérification de sa présence en production. [#5271](https://github.com/betagouv/service-national-universel/issues/5271)

### Évolutions techniques
- Suppression de l'archivage des représentants légaux, simplifiant ainsi le code et réduisant sa complexité. [#5269](https://github.com/betagouv/service-national-universel/issues/5269)
- Mise à jour de la librairie Mongoose vers la version 7.8.3 pour corriger une vulnérabilité de sécurité (CVE $where). [#5267](https://github.com/betagouv/service-national-universel/issues/5267)

### Autres changements
- Aucun changement significatif à signaler.
