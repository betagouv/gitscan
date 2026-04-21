## Changelog : mobilic-api (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, les évolutions de mobilic-api se sont concentrées sur la correction de bugs, l'amélioration de la sécurité et l'optimisation de certaines fonctionnalités existantes. Des corrections ont été apportées concernant les fuseaux horaires dans les exports, la validation automatique des missions, et la gestion des poids des véhicules. Une mise à jour de Flask a également été effectuée.

### Évolutions fonctionnelles
- Correction d'un problème de fuseaux horaires dans les exports et les fichiers PDF [#671](https://github.com/MTES-MCT/mobilic-api/pull/671).
- Amélioration de la validation automatique des missions, notamment pour éviter des erreurs liées aux identifiants d'entreprise [#692](https://github.com/MTES-MCT/mobilic-api/pull/692) et pour gérer les activités en cours [#689](https://github.com/MTES-MCT/mobilic-api/pull/689).
- Mise à jour du label de vérification de la réglementation en cas d'absence de permis [#684](https://github.com/MTES-MCT/mobilic-api/pull/684).
- Correction du format d'affichage du poids des véhicules dans les bulletins de contrôle BDC [#691](https://github.com/MTES-MCT/mobilic-api/pull/691).
- Correction d'un bug lié à l'ordre de tri des fichiers exportés [#678](https://github.com/MTES-MCT/mobilic-api/pull/678).

### Évolutions techniques
- Mise à jour de Flask, la librairie web Python utilisée par l'API [#686](https://github.com/MTES-MCT/mobilic-api/pull/686).
- Ajout d'une protection contre les attaques par complexité de requête GraphQL pour éviter une surcharge du serveur [#694](https://github.com/MTES-MCT/mobilic-api/pull/694).
- Suppression du contexte des accès aux données d'activité pour améliorer la sécurité et la performance [#693](https://github.com/MTES-MCT/mobilic-api/pull/693).
- Désactivation de GraphiQL en production pour des raisons de sécurité, suite à une alerte SonarQube [#5de072e](https://github.com/MTES-MCT/mobilic-api/commit/5de072e).
- Ajout d'une limite de taille pour les requêtes GraphQL afin de prévenir les attaques par déni de service [#9286bc8](https://github.com/MTES-MCT/mobilic-api/commit/9286bc8).

### Autres changements
- Améliorations de la qualité du code et corrections de style pour répondre aux exigences de SonarCloud [#8a097e2](https://github.com/MTES-MCT/mobilic-api/commit/8a097e2).
- Renommage de variables pour une meilleure lisibilité et conformité aux conventions de nommage (snake_case) [#67d0e13](https://github.com/MTES-MCT/mobilic-api/commit/67d0e13), [#21d5f5e](https://github.com/MTES-MCT/mobilic-api/commit/21d5f5e).
- Ajout de logs de débogage pour faciliter le diagnostic des problèmes liés à l'authentification Agent Connect [#f01eecd](https://github.com/MTES-MCT/mobilic-api/commit/f01eecd).
- Corrections mineures liées à la redirection URI dans Agent Connect [#09e4e20](https://github.com/MTES-MCT/mobilic-api/commit/09e4e20), [#50411bd](https://github.com/MTES-MCT/mobilic-api/commit/50411bd).
