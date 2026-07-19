## Changelog : Docurba (30 derniers jours, au 17 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de la qualité du code et des tests, des corrections de bugs sur l'interface utilisateur et l'API, ainsi que par des évolutions de la gestion des événements et des types de documents. Des optimisations de performance ont également été apportées à l'API.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la gestion correcte des emails en minuscules lors du partage de procédures [#385056d](https://github.com/MTES-MCT/Docurba/commit/385056d).
- Amélioration de l'affichage des dates de procédures sur les pages "Procédures" et "Collectivités" [#0954b31](https://github.com/MTES-MCT/Docurba/commit/0954b31).
- Ajout de l'ID de la procédure dans l'onglet "Procédures et Validations" [#53de844](https://github.com/MTES-MCT/Docurba/commit/53de844).
- Correction de l'affichage des images en ligne dans les PACs [#4a63a08](https://github.com/MTES-MCT/Docurba/commit/4a63a08).
- Adaptation du lien vers les collectivités en fonction des droits de l'utilisateur [#4790c2c](https://github.com/MTES-MCT/Docurba/commit/4790c2c).
- Ajout des types d'événements à la détection d'événements [#e0a4a68](https://github.com/MTES-MCT/Docurba/commit/e0a4a68).
- Application de la loi Huwart à toutes les procédures [#bcac074](https://github.com/MTES-MCT/Docurba/commit/bcac074).

### Évolutions techniques
- Refactorisation et renforcement de la suite de tests de l'API Django [#8828b9d](https://github.com/MTES-MCT/Docurba/commit/8828b9d).
- Ajout de `freezegun` pour figer le temps dans les tests Django [#20df824](https://github.com/MTES-MCT/Docurba/commit/20df824).
- Amélioration des performances de l'API Django [#b941aca](https://github.com/MTES-MCT/Docurba/commit/b941aca).
- Ajout de relations manquantes entre les événements et leurs snapshots dans l'historique PostgreSQL [#1b86501](https://github.com/MTES-MCT/Docurba/commit/1b86501).
- Ajout de RLS (Row Level Security) sur plusieurs tables pour améliorer la sécurité [#0d549a8](https://github.com/MTES-MCT/Docurba/commit/0d549a8).
- Ajout de champs `archived_at` et `archived_by` à la table des événements [#b1613bc](https://github.com/MTES-MCT/Docurba/commit/b1613bc).
- Mise à jour de Node.js en version 26 [#0f3d354](https://github.com/MTES-MCT/Docurba/commit/0f3d354).
- Suppression d'une vue matérialisée obsolète et d'un test inutile [#cca93c3](https://github.com/MTES-MCT/Docurba/commit/cca93c3).
- Suppression de nombreux composants et assets inutilisés dans l'interface utilisateur Nuxt.js [#ea814f5](https://github.com/MTES-MCT/Docurba/commit/ea814f5) et suivants.
- Ajout de la gestion des événements via l'API interne [#f1044dd](https://github.com/MTES-MCT/Docurba/commit/f1044dd) et suivants.

### Autres changements
- Ajout de `Collectivite.siren` et refactorisation de `Collectivite.code_insee` [#d947e06](https://github.com/MTES-MCT/Docurba/commit/d947e06) et suivants.
- Ajout d'un gestionnaire "Adhesion" [#ab5add6](https://github.com/MTES-MCT/Docurba/commit/ab5add6).
- Ajout de la possibilité d'exposer les groupes et membres de la collectivité via l'API interne [#91ee156](https://github.com/MTES-MCT/Docurba/commit/91ee156).
- Mise à jour des dépendances : `syrupy`, `django-datadog-logger`, `django`, `pytest`, `ruff`, `django-debug-toolbar`, `django-environ`.
- Ajout de la configuration DEBUG_SQL pour faciliter le débogage des requêtes SQL [#9a1f36a](https://github.com/MTES-MCT/Docurba/commit/9a1f36a).
- Ajout de Traits spécifiques pour les snapshots dans les tests Django [#d45c4a6](https://github.com/MTES-MCT/Docurba/commit/d45c4a6).
- Correction de l'utilisation d'une variable incorrecte dans une boucle Django API [#1a57d0f](https://github.com/MTES-MCT/Docurba/commit/1a57d0f).
- Amélioration de la gestion des paramètres de requête dupliqués dans l'API interne [#d9e61fe](https://github.com/MTES-MCT/Docurba/commit/d9e61fe).
