## Changelog : verseau2 (30 derniers jours, au 07 mai 2026)

### Résumé
Les dernières mises à jour de Verseau2 se concentrent sur l'amélioration de la stabilité, la correction de bugs et l'optimisation de l'expérience utilisateur, notamment au niveau de l'authentification et de la gestion des requêtes. Des améliorations ont également été apportées à la configuration pour le déploiement en production et à la documentation interne.

### Évolutions fonctionnelles
- Mise à jour du titre de l'application et ajout de la gestion de l'environnement. [#74](https://github.com/MTES-MCT/verseau2/issues/74)
- Ajout de la configuration pour le reverse proxy, facilitant le déploiement et la configuration du serveur. [#73](https://github.com/MTES-MCT/verseau2/issues/73)
- Correction d'un bug empêchant l'affichage correct de la liste des ouvrages RMC. [#69](https://github.com/MTES-MCT/verseau2/issues/69)
- Ajout d'un nouvel endpoint MASA. [#68](https://github.com/MTES-MCT/verseau2/issues/68)
- Correction d'un problème de redirection de l'URL `https://www.saineau.beta.gouv.fr/verseau` vers une URL reconstruite par Nginx. [#80](https://github.com/MTES-MCT/verseau2/issues/80)
- Correction d'un bug lié à la gestion des erreurs lors de la récupération des informations utilisateur. [#61](https://github.com/MTES-MCT/verseau2/issues/61)

### Évolutions techniques
- Refactoring de la gestion des requêtes pour les API REST MASA, améliorant la performance et la maintenabilité.
- Amélioration de la documentation et des commandes dans le fichier `AGENTS.md`.
- Suppression de propriétés inutilisées dans les filtres backend, simplifiant le code et améliorant la performance. [#67](https://github.com/MTES-MCT/verseau2/issues/67)
- Renommage des propriétés en utilisant la convention de domaine, améliorant la cohérence du code. [#65](https://github.com/MTES-MCT/verseau2/issues/65)
- Augmentation de la durée de vie du cookie `access_token` et suppression de `idToken` dans les réponses, optimisant la gestion des sessions. [#64](https://github.com/MTES-MCT/verseau2/issues/64)
- Suppression de `skipSubjectCheck` et ajustement des appels, améliorant la sécurité et la performance. [#62](https://github.com/MTES-MCT/verseau2/issues/62)
- Correction du type de réponse pour le refresh token. [#61](https://github.com/MTES-MCT/verseau2/issues/61)
- Amélioration du formatage des requêtes SQL dans les logs pour une meilleure lisibilité.
- Limitation de la longueur des paramètres dans les logs de requête pour éviter les problèmes de performance.
- Correction des règles ESLint et gestion des erreurs. [#75](https://github.com/MTES-MCT/verseau2/issues/75)

### Autres changements
- Désactivation temporaire de la synchronisation de la base de données pour maintenance. [#78](https://github.com/MTES-MCT/verseau2/issues/78)
- Ajout de la configuration du serveur pour Docker.
- Correction de tests en erreur liés au rafraîchissement des tokens. [#61](https://github.com/MTES-MCT/verseau2/issues/61)
- Correction d'un correctif de recette. [#71](https://github.com/MTES-MCT/verseau2/issues/71)
