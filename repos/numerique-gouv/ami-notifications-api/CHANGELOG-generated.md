## Changelog : ami-notifications-api (30 derniers jours, au 13 juillet 2026)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à l'interface utilisateur, notamment concernant la gestion des suivis (followup) et des requêtes, avec l'ajout de fonctionnalités d'archivage et une refonte de l'affichage. Des améliorations de sécurité et d'authentification, notamment avec l'intégration de FranceConnect, ont également été implémentées. Enfin, des corrections d'accessibilité (RGAA) et des optimisations de performance ont été réalisées.

### Évolutions fonctionnelles
- **Gestion des suivis (followup) :**
    - Ajout de la possibilité d'archiver les suivis.
    - Refonte de l'affichage des suivis, simplification de l'interface et suppression des onglets.
    - Ajout d'une page dédiée aux suivis archivés.
    - Ajout d'un bouton "procédure" pour les suivis.
- **Authentification :**
    - Intégration d'un nouveau processus de connexion via FranceConnect, incluant une page dédiée et une gestion des providers.
    - Amélioration de la gestion des sessions et de la déconnexion pour éviter les erreurs d'intégrité.
- **Notifications :**
    - Amélioration de l'affichage des icônes de notification, avec une déduction automatique à partir des informations de l'élément associé.
    - Ajout du champ `item_is_archived` aux notifications.
- **API :**
    - Ajout d'un endpoint PUT pour les événements v2.
    - Expose les champs `external_item_type` et `external_item_id` dans l'API followup.
    - Modification de l'API pour gérer l'archivage des éléments.

### Évolutions techniques
- **Infrastructure :**
    - Mise à jour de plusieurs dépendances (ujson, msgpack, pyjwt, webob, etc.).
    - Utilisation de `django-tasks-db` par défaut pour la gestion des tâches asynchrones.
    - Configuration de Vite pour LightningCSS.
- **Code :**
    - Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
    - Renommage de certaines librairies et routes pour une meilleure cohérence (catalog -> agenda, inventory -> followup, requests -> followup).
    - Suppression de code obsolète.
    - Ajout de tests unitaires pour certaines fonctionnalités.
- **Sécurité :**
    - Amélioration de la gestion des cookies pour la connexion via FranceConnect.

### Autres changements
- Corrections d'accessibilité (RGAA) concernant les boutons, les titres et les champs de formulaire.
- Amélioration de la gestion des logs et des erreurs.
- Mise à jour de la documentation.
- Correction de bugs mineurs et amélioration de la stabilité de l'application.
- Suppression de l'affichage de la description des pull requests de Dependabot dans les logs.
