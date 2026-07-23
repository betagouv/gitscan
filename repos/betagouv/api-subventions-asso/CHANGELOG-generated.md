## Changelog : api-subventions-asso (30 derniers jours, au 20 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'importation et du traitement des données de subventions, notamment via l'intégration de nouvelles sources de données (RNA Waldec, Sirene) et la correction de bugs liés à la gestion des documents et des associations. Des améliorations techniques ont également été apportées pour la gestion des erreurs et la stabilité de l'API.

### Évolutions fonctionnelles
- Intégration de l'importation des fichiers parquet RNA Waldec pour enrichir les données de subventions. [#3984](https://github.com/betagouv/api-subventions-asso/issues/3984)
- Intégration de la source de données Sirene-Etablissements pour améliorer la recherche et la validation des informations sur les établissements. [#3986](https://github.com/betagouv/api-subventions-asso/issues/3986)
- Amélioration des notifications concernant l'importation des données des fournisseurs. [#3933](https://github.com/betagouv/api-subventions-asso/issues/3933)
- Correction d'un bug empêchant la récupération correcte des documents associés aux associations. [#0000](https://github.com/betagouv/api-subventions-asso/issues/0000)
- Correction d'un problème d'affichage d'alertes de doublons SIREN sur le front-end. [#3964](https://github.com/betagouv/api-subventions-asso/issues/3964)
- Correction d'un bug lié à la gestion des erreurs 404 lors de la récupération des données de l'API asso. [#3980](https://github.com/betagouv/api-subventions-asso/issues/3980)
- Amélioration de la gestion des identifiants uniques Chorus, en passant à un index composite. [#3942](https://github.com/betagouv/api-subventions-asso/issues/3942)

### Évolutions techniques
- Refactorisation du service de gestion des droits (grant service) pour une meilleure maintenabilité. [#3527](https://github.com/betagouv/api-subventions-asso/issues/3527)
- Suppression des codes d'erreur HTTP personnalisés au profit de codes standards. [#3945](https://github.com/betagouv/api-subventions-asso/issues/3945)
- Refactorisation du code pour utiliser l'entité `UserEntity` au lieu de `_id` pour une meilleure cohérence. [#3971](https://github.com/betagouv/api-subventions-asso/issues/3971)
- Mise à jour de la version de pnpm vers la version 11. [#3897](https://github.com/betagouv/api-subventions-asso/issues/3897)
- Mise à jour de l'URL de la source de données Sirene pour utiliser un lien stable. [#3982](https://github.com/betagouv/api-subventions-asso/issues/3982)

### Autres changements
- Mise à jour des scripts de publication pour inclure tous les packages, y compris le package racine.
- Régénération du fichier changelog.
- Suppression d'un ancien nom de connexion Pro Connect. [#3972](https://github.com/betagouv/api-subventions-asso/issues/3972)
