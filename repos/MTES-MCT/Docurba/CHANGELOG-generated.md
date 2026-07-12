## Changelog : Docurba (30 derniers jours, au 10 juillet 2026)

### Résumé
Les dernières mises à jour de Docurba se concentrent sur l'amélioration de la gestion des événements, l'enrichissement des données des collectivités et des procédures, ainsi que des optimisations de sécurité et de performance. Plusieurs composants inutilisés ont été supprimés de l'interface utilisateur, allégeant ainsi l'application. Des corrections et des améliorations ont également été apportées à l'API interne et à l'administration Django.

### Évolutions fonctionnelles
- Ajout de l'ID de la procédure dans l'onglet Procédures et Validations pour une meilleure identification.
- Possibilité de modifier les événements dans l'administration Django.
- Amélioration de la recherche d'utilisateurs dans l'administration Django par email.
- Ajout de la possibilité de modifier le mot de passe des utilisateurs dans l'administration Django.
- Les dates de procédures sont maintenant affichées sur les pages Procédures et Collectivités.
- Les événements les plus récents sont utilisés pour l'approbation, la prescription et l'arrêt des procédures.
- Ajout de la gestion des types de documents sectoriels et de leur affichage.
- Historisation de toutes les modifications d'événements grâce à l'intégration de `pg_history`.
- Possibilité de lister les procédures dont le périmètre inclut une commune dans l'administration Django.
- Ajout d'un champ "siren" à la collectivité dans l'API interne.
- Ajout de la gestion des adhésions et des groupes de collectivités dans l'API interne.

### Évolutions techniques
- Ajout de RLS (Row Level Security) sur les tables `core_eventtype`, `history_eventsnapshot` et `pghistory_context` pour renforcer la sécurité.
- Suppression de vues matérialisées obsolètes et de tests inutiles.
- Mise à jour de plusieurs dépendances : Django, Django Debug Toolbar, pytest, ruff, cryptography, pyjwt et supabase.
- Suppression de nombreux composants inutilisés de l'interface utilisateur Nuxt (charts, composants de statistiques, etc.).
- Amélioration de la configuration des templates.
- Correction de bugs et amélioration de la performance de l'API interne.
- Utilisation de `Syrupy` pour les tests de l'API interne.
- Ajout d'une variable d'environnement `DEBUG_SQL` pour faciliter le débogage des requêtes SQL.
- Refonte de la gestion des événements dans l'interface Nuxt.
- Amélioration de la gestion des erreurs et des annotations dans l'API.

### Autres changements
- Mise à jour des fichiers `event_types.json`.
- Suppression de fichiers d'assets inutilisés.
- Correction de bugs mineurs et amélioration de la lisibilité du code.
- Ajout de commentaires et de documentation.
- Suppression de commandes de gestion Django obsolètes.
- Correction d'un bug lié à l'affichage des dates dans l'interface Nuxt.
- Restriction de l'accès aux tables de versements aux utilisateurs vérifiés.
- Suppression d'une configuration Git incorrecte.
