## Changelog : federation (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse et de la surveillance de la plateforme, notamment en ajoutant des vérifications de santé (healthchecks) et en corrigeant des problèmes liés à la disponibilité des services. Des améliorations ont également été apportées à la configuration et à la flexibilité de certains composants, ainsi qu'à la validation des adresses email.

### Évolutions fonctionnelles
- Ajout d'un indicateur pour activer ou désactiver la validation des adresses email via le flag `FEATURE_VALIDATE_EMAIL` [#1144](https://github.com/proconnect-gouv/federation/pull/1144).
- Ajout d'une bannière d'avertissement pour l'environnement de test [#1141](https://github.com/proconnect-gouv/federation/pull/1141).
- Ajout d'une bannière de maintenance [#1091](https://github.com/proconnect-gouv/federation/pull/1091).

### Évolutions techniques
- Implémentation d'un pattern ping/pong pour la vérification de l'état du broker de messages [#1117](https://github.com/proconnect-gouv/federation/pull/1117).
- Ajout de vérifications de santé (healthchecks) pour les différents services (csmr, hyyyperbridge) avec des points de terminaison `/livez` et `/readyz` [#1114](https://github.com/proconnect-gouv/federation/pull/1114), [#1110](https://github.com/proconnect-gouv/federation/pull/1110), [#1111](https://github.com/proconnect-gouv/federation/pull/1111).
- Suppression des healthchecks intégrés au Dockerfile et passage à la configuration via les points de terminaison dédiés [#1119](https://github.com/proconnect-gouv/federation/pull/1119).
- Correction d'un problème de proxy axios dans le service csmr, permettant à l'environnement natif de gérer les requêtes [#1125](https://github.com/proconnect-gouv/federation/pull/1125).
- Correction de tests ChangeStream Mongoose instables [#1096](https://github.com/proconnect-gouv/federation/pull/1096).
- Utilisation de HTTPS pour récupérer les informations du core-fca [#1118](https://github.com/proconnect-gouv/federation/pull/1118).
- Amélioration de la configuration du client OIDC pour utiliser `customFetch` dans les configurations sans découverte [#1143](https://github.com/proconnect-gouv/federation/pull/1143).

### Autres changements
- Ajout des variables `isEntraId` et `hyyyperbridge` à Grist pour faciliter le suivi et la configuration [#1115](https://github.com/proconnect-gouv/federation/pull/1115).
- Ajout de logs pour les valeurs `acr_values` [#1139](https://github.com/proconnect-gouv/federation/pull/1139).
- Suppression d'un test API de santé obsolète [#1120](https://github.com/proconnect-gouv/federation/pull/1120).
- Mises à jour de dépendances diverses (voir commits dependabot).
