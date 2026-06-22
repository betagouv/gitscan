## Changelog : proconnect-identite (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les évolutions de ProConnect Identité se concentrent sur l'amélioration de la sécurité, la correction de bugs et l'optimisation des performances. Des améliorations ont été apportées à la gestion des ACR (Advanced Consent Request), à la validation des utilisateurs et à la compatibilité avec les futures versions de PostgreSQL. Des mises à jour de la base de données et de l'algorithme de détermination du statut de service public ont également été implémentées.

### Évolutions fonctionnelles
- Amélioration de la gestion des niveaux ACR (Advanced Consent Request) pour une meilleure compatibilité et une gestion plus fine des certifications dirigeant [#1965](https://github.com/proconnect-gouv/proconnect-identite/issues/1965).
- Ajout d'une limite de tentatives pour la vérification par email afin de prévenir les abus [#2004](https://github.com/proconnect-gouv/proconnect-identite/issues/2004).
- Ajout de la catégorie juridique "Pôle d'équilibre territorial et rural" pour une meilleure classification des entités [#1982](https://github.com/proconnect-gouv/proconnect-identite/issues/1982).
- Amélioration de la validation automatique des utilisateurs disposant d'un domaine de contact officiel [#1934](https://github.com/proconnect-gouv/proconnect-identite/issues/1934).
- Ajout d'une raison d'utilisation pour les modérations, permettant un suivi plus précis des actions [#1931](https://github.com/proconnect-gouv/proconnect-identite/issues/1931).
- Simplification de l'adhésion pour les petites organisations civiles/agricoles avec une adresse email valide [#1972](https://github.com/proconnect-gouv/proconnect-identite/issues/1972).
- Mise à jour de l'algorithme de détermination du statut de service public pour une plus grande précision [#1957](https://github.com/proconnect-gouv/proconnect-identite/issues/1957).

### Évolutions techniques
- Préparation de la base de données pour la compatibilité avec PostgreSQL 17 [#1983](https://github.com/proconnect-gouv/proconnect-identite/issues/1983).
- Optimisation des performances de la requête des clients OIDC en ajoutant un index sur `user_id` et `created_at` [#1989](https://github.com/proconnect-gouv/proconnect-identite/issues/1989).
- Mise à jour de plusieurs dépendances, notamment `axios`, `tmp`, `postcss` et `proconnect-test-client`.
- Amélioration de la gestion des erreurs et de la robustesse du code.
- Ajout d'un workflow pour vérifier l'identité du token NPM utilisé pour les publications.
- Correction d'un bug lié à l'importation du type `pg` dans les contextes pour une meilleure compatibilité avec les bundlers.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.

### Autres changements
- Ajout d'un script pour administrer les données dans Grist, facilitant la gestion des informations sur les administrations [#1946](https://github.com/proconnect-gouv/proconnect-identite/issues/1946).
- Ajout d'un workflow pour exécuter le script de mise à jour de l'annuaire des entreprises localement [#1943](https://github.com/proconnect-gouv/proconnect-identite/issues/1943).
- Ajout de statistiques sur les authentificateurs à Metabase pour un meilleur suivi de l'utilisation [#1967](https://github.com/proconnect-gouv/proconnect-identite/issues/1967).
- Correction d'un bug d'encodage d'URL [#1966](https://github.com/proconnect-gouv/proconnect-identite/issues/1966).
- Amélioration de la gestion des ratios d'envoi d'emails alternatifs pour une meilleure délivrabilité [#1951](https://github.com/proconnect-gouv/proconnect-identite/issues/1951).
- Publication du package `rne` pour une utilisation publique [#1963](https://github.com/proconnect-gouv/proconnect-identite/issues/1963).
