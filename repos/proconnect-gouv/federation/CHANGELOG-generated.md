## Changelog : federation (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse et de l'observabilité de la plateforme, notamment en ajoutant des logs plus détaillés pour faciliter le débogage et le suivi des erreurs. Des améliorations ont également été apportées à la gestion de la santé des services et à la configuration de l'environnement. Enfin, des corrections ont été apportées pour améliorer la fiabilité et la sécurité.

### Évolutions fonctionnelles
- Ajout d'un indicateur de maintenance visible pour les utilisateurs. [#1091](https://github.com/proconnect-gouv/federation/pull/1091)
- Amélioration des messages d'erreur liés à l'authentification OIDC et aux emails. [#1064](https://github.com/proconnect-gouv/federation/pull/1064)
- Mise à jour de la charge utile `userinfo` pour une meilleure compatibilité. [#1041](https://github.com/proconnect-gouv/federation/pull/1041)
- Possibilité d'utiliser HTTPS pour récupérer le core-FCA, corrigeant un problème potentiel. [#1118](https://github.com/proconnect-gouv/federation/pull/1118)

### Évolutions techniques
- Implémentation d'un système de *ping/pong* pour la vérification de l'état du broker, améliorant la fiabilité des microservices. [#1117](https://github.com/proconnect-gouv/federation/pull/1117)
- Ajout de routes `/livez` et `/readyz` pour les contrôles de santé, facilitant le monitoring et l'orchestration des conteneurs. [#1111](https://github.com/proconnect-gouv/federation/pull/1111) et [#1032](https://github.com/proconnect-gouv/federation/pull/1032)
- Suppression des tests de santé dans le Dockerfile, simplifiant le processus de construction des images. [#1119](https://github.com/proconnect-gouv/federation/pull/1119) et [#1120](https://github.com/proconnect-gouv/federation/pull/1120)
- Refactorisation de l'appel à l'API Entreprise pour une meilleure modularité et testabilité. [#1088](https://github.com/proconnect-gouv/federation/pull/1088)
- Suppression de l'utilisation d'Axios au profit de `fetch` dans certaines parties du code. [#1018](https://github.com/proconnect-gouv/federation/pull/1018)
- Remplacement des cookies par des cookies de session pour une meilleure sécurité. [#1042](https://github.com/proconnect-gouv/federation/pull/1042)
- Correction de tests ChangeStream de Mongoose qui étaient parfois instables. [#1096](https://github.com/proconnect-gouv/federation/pull/1096)
- Possibilité de désactiver le proxy Axios pour le CSM RIE. [#1125](https://github.com/proconnect-gouv/federation/pull/1125)
- Configuration plus proche de l'environnement de production. [#1139](https://github.com/proconnect-gouv/federation/pull/1139)

### Autres changements
- Ajout de logs plus détaillés pour faciliter le débogage des erreurs liées à l'authentification, aux rôles et à l'API Entreprise. [#1115](https://github.com/proconnect-gouv/federation/pull/1115), [#1070](https://github.com/proconnect-gouv/federation/pull/1070), [#1063](https://github.com/proconnect-gouv/federation/pull/1063), [#1039](https://github.com/proconnect-gouv/federation/pull/1039)
- Ajout des traces de pile d'erreur pour faciliter le diagnostic des problèmes. [#1111](https://github.com/proconnect-gouv/federation/pull/1111)
- Mise à jour de diverses dépendances.
- Correction de l'utilisation de la variable d'environnement `trust-proxy` pour le core. [#1067](https://github.com/proconnect-gouv/federation/pull/1067)
- Suppression d'un test API santé inutile. [#1120](https://github.com/proconnect-gouv/federation/pull/1120)
