## Changelog : Docurba (30 derniers jours, au 10 juillet 2026)

### Résumé
Les dernières mises à jour de Docurba apportent des améliorations significatives à la gestion des événements, des collectivités et des données associées. L'interface utilisateur a été enrichie avec des informations sur les dates de procédures et les types d'événements. Des optimisations ont également été réalisées sur la performance et la sécurité de l'application, notamment au niveau de l'historisation des données et de l'accès aux informations.

### Évolutions fonctionnelles
- Ajout de l'ID de la procédure dans l'onglet Procédures et Validations.
- Possibilité de lister les procédures dont le périmètre inclut une commune dans l'administration Django.
- Amélioration de l'affichage des dates de procédures et des collectivités dans l'interface utilisateur Nuxt.
- Intégration des types d'événements pour le lancement de la détection d'événements.
- Ajout de la possibilité de modifier les événements dans l'administration Django.
- Ajout d'un gestionnaire "Adhesion" pour les collectivités.
- Ajout des champs `siren` à la collectivite via l'API interne.
- Ajout de la possibilité de filtrer les adhésions (flat et one-level) via l'API interne.
- Historisation de toutes les modifications d'événements.
- Amélioration de l'affichage des événements (prescription, approbation, arrêt) en utilisant le dernier événement associé.
- Ajout de la possibilité de rechercher des utilisateurs par email dans l'administration Django.
- Ajout de la possibilité de modifier le mot de passe des utilisateurs dans l'administration Django.

### Évolutions techniques
- Ajout de RLS (Row Level Security) sur les tables `core_eventtype`, `history_eventsnapshot` et `pghistory_context`.
- Refonte de l'intégration de `pg_history` pour récupérer l'utilisateur dans le contexte.
- Suppression de vues matérialisées obsolètes et de tests inutiles.
- Mise à jour de plusieurs dépendances : `ruff`, `pytest`, `django-debug-toolbar`, `django-environ`, `cryptography`, `pyjwt`.
- Suppression de composants et d'assets inutilisés dans l'interface utilisateur Nuxt.
- Amélioration de la configuration des templates.
- Limitation des champs envoyés dans les payloads des webhooks.
- Ajout d'une variable d'environnement `DEBUG_SQL` pour activer le logging SQL.
- Utilisation de `Syrupy` pour les tests de l'API interne.
- Correction de bugs et amélioration de la sécurité (utilisation de `format_html` dans l'administration Django).
- Optimisation des requêtes et ajout d'index pour remplacer une vue matérialisée.

### Autres changements
- Mise à jour des types de documents sectoriels.
- Ajout d'une factory `EventTypeFactory`.
- Mise à jour des fichiers `event_types.json`.
- Suppression de commandes de gestion obsolètes.
- Ajout d'une factory `ProjectFactory`.
- Suppression de fichiers de configuration Django sensibles du dépôt.
- Correction de bugs mineurs et amélioration de la lisibilité du code.
- Correction d'un bug empêchant l'affichage correct des procédures sur les écrans étroits.
- Correction d'un bug lié à l'utilisation de variables incorrectes dans une boucle de l'API Django.
