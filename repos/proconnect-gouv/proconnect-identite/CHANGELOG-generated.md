## Changelog : proconnect-identite (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des informations sur les services publics, la préparation à la migration des emails MonComptePro, et des mises à jour de sécurité et de dépendances. Des améliorations ont également été apportées aux tests et à la gestion des rejets de certifications.

### Évolutions fonctionnelles
- Ajout d'une description d'erreur OIDC pour faciliter le diagnostic des problèmes avec PCF. [#1926](https://github.com/proconnect-gouv/proconnect-identite/pull/1926)
- Modification du message de rejet de certification pour orienter l'utilisateur vers l'email reçu. [#1927](https://github.com/proconnect-gouv/proconnect-identite/pull/1927)
- Début de la migration des emails en provenance de MonComptePro, avec ajout du nom de l'expéditeur. [#1930](https://github.com/proconnect-gouv/proconnect-identite/pull/1930)
- Nouvelle fonction `computeIsServicePublic` pour déterminer si un service est public, utilisant un nouvel algorithme. [#1946](https://github.com/proconnect-gouv/proconnect-identite/pull/1946)

### Évolutions techniques
- Création d'un client dédié pour l'environnement de pré-production de la fédération. [#1937](https://github.com/proconnect-gouv/proconnect-identite/pull/1937)
- Mise à jour des identifiants et secrets du client PCF en pré-production. [#1938](https://github.com/proconnect-gouv/proconnect-identite/pull/1938), [#1939](https://github.com/proconnect-gouv/proconnect-identite/pull/1939)
- Refactorisation de la graine de base de données pour les tests E2E, utilisant un hook `before`. [#1925](https://github.com/proconnect-gouv/proconnect-identite/pull/1925)
- Correction de l'importation du type `pg` pour une meilleure compatibilité avec les bundlers navigateurs. [#1947](https://github.com/proconnect-gouv/proconnect-identite/pull/1947)
- Mise à jour de la version de Node.js dans les conteneurs Docker (revert d'une mise à jour précédente). [#1921](https://github.com/proconnect-gouv/proconnect-identite/pull/1921), [#1924](https://github.com/proconnect-gouv/proconnect-identite/pull/1924)

### Autres changements
- Ajout d'un workflow pour exécuter le script de mise à jour de l'annuaire des entreprises localement. [#1943](https://github.com/proconnect-gouv/proconnect-identite/pull/1943)
- Ajout d'un workflow dispatch pour lancer le script de mise à jour de l'annuaire des entreprises. [#1945](https://github.com/proconnect-gouv/proconnect-identite/pull/1945)
- Mise à jour du script pour utiliser les nouveaux fichiers de l'annuaire des entreprises. [#1941](https://github.com/proconnect-gouv/proconnect-identite/pull/1941)
- Amélioration du formatage des données après l'écriture du script Grist. [#1950](https://github.com/proconnect-gouv/proconnect-identite/pull/1950)
- Ajout d'un debug pour vérifier la variable d'environnement NPM_TOKEN. [#1949](https://github.com/proconnect-gouv/proconnect-identite/issues/1949)
- Documentation de la correction de l'importation du type `pg`. [#1947](https://github.com/proconnect-gouv/proconnect-identite/pull/1947)
- Mises à jour de dépendances : axios, tmp, postcss, uuid, cypress, actions/labeler, redis, hono, sentry.
