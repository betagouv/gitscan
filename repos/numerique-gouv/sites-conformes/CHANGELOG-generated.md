## Changelog : sites-conformes (30 derniers jours, au 1er juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse de l'application, notamment avec l'ajout de Sentry pour la surveillance des erreurs, et des corrections de bugs sur le frontend. Une nouvelle fonctionnalité majeure permet le stockage des médias directement en base de données PostgreSQL, offrant une alternative à S3. Des travaux de packagification et de documentation ont également été réalisés.

### Évolutions fonctionnelles
- **Stockage des médias en PostgreSQL :** Possibilité de stocker les médias directement dans la base de données PostgreSQL, offrant une alternative à l'utilisation de S3. [#482](https://github.com/numerique-gouv/sites-conformes/issues/482)
- **Correction de bugs frontend :** Résolution de plusieurs bugs impactant l'interface utilisateur. [#486](https://github.com/numerique-gouv/sites-conformes/issues/486)
- **Correction du problème `clean_name` vide :** Résolution d'un bug où le champ `clean_name` pouvait être vide sur les champs de formulaire. [#492](https://github.com/numerique-gouv/sites-conformes/issues/492)

### Évolutions techniques
- **Intégration de Sentry :** Ajout de Sentry pour la surveillance et la gestion des erreurs en production. [#445](https://github.com/numerique-gouv/sites-conformes/issues/445)
- **Packagification :** Travaux de packagification pour améliorer la structure du projet. [#506](https://github.com/numerique-gouv/sites-conformes/issues/506) et [#514](https://github.com/numerique-gouv/sites-conformes/issues/514)
- **Mise à jour des dépendances Python :** Mise à jour des dépendances Python pour bénéficier des dernières corrections et améliorations. [#501](https://github.com/numerique-gouv/sites-conformes/issues/501)
- **Refactoring du code :** Déplacement des sources namespacées dans `sites_conformes/`.
- **Préparation pour la version 3.2.0 :** Application des corrections automatiques de pre-commit et noms de packages.

### Autres changements
- **Documentation :** Mise à jour de la documentation. [#511](https://github.com/numerique-gouv/sites-conformes/issues/511)
- **Changement de nom du dépôt :** Mise à jour du nom du dépôt. [#493](https://github.com/numerique-gouv/sites-conformes/issues/493)
- **Annulation d'une migration :** Annulation d'une migration récente.
