## Changelog : Docurba (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Docurba se concentrent sur l'amélioration de l'administration des événements et des procédures, notamment via l'interface d'administration Django. Des corrections et des améliorations ont également été apportées à l'interface utilisateur Nuxt3, en particulier concernant la gestion des procédures et des événements liés à la loi Huwart. Des optimisations de sécurité et de performance ont également été implémentées.

### Évolutions fonctionnelles
- Possibilité de modifier les événements depuis l'interface d'administration Django.
- Ajout de catégories de PAC (Plan d'Actions Concertées) dans Django.
- Ajout d'une nouvelle catégorie d'événement dans Django.
- Amélioration de l'affichage des procédures et des événements dans Nuxt3, notamment pour les procédures antérieures à la loi Huwart.
- La page de lecture des PAC est désormais publique.
- Possibilité de filtrer les types de procédures par date de début.
- Historisation de toutes les modifications d'événements.
- Les procédures peuvent être listées dans l'administration Django en fonction de l'inclusion de la commune dans leur périmètre.
- Amélioration de la sélection de la section trame dans Nuxt3, initialisée à partir de l'URL.
- Affichage du statut des procédures primaires manquantes dans les messages.
- Ajout de la possibilité de filtrer les collectivités et communes via une API interne.
- Amélioration de la gestion des événements liés à la loi Huwart dans Nuxt3.

### Évolutions techniques
- Refonte de l'architecture de reverse proxy : remplacement de `django-revproxy` par Nginx pour la gestion du reverse proxy et la limitation du débit.
- Utilisation explicite de `DOCURBA_API_URL` dans Nuxt3.
- Ajout de tests API Django.
- Amélioration de la performance des requêtes Django, notamment via l'ajout d'index.
- Mise à jour des dépendances : Django, Supabase, Ruff, cryptography, pyjwt, django-filter.
- Suppression de dépendances obsolètes.
- Ajout de la gestion des sessions et de l'authentification Supabase.
- Ajout du header `Supabase-Authorization` pour l'authentification.
- Amélioration de l'intégration de `pg_history` pour le suivi des modifications.
- Utilisation de `format_html` pour des raisons de sécurité dans l'administration Django.
- Suppression de code commenté inutile.
- Correction de la configuration des templates.
- Suppression de la vue publique `collectivite-detail`.

### Autres changements
- Ajout de commentaires dans le code.
- Amélioration de la documentation.
- Ajout de factories pour les tests Django (Project, Event).
- Correction de la configuration CORS pour l'environnement local.
- Ajout d'une alerte Slack lors des déploiements.
- Suppression d'un test inutile.
- Ajout du champ `last_sign_in_at` au modèle User.
- Ajout du champ `owner_id` au modèle Procedure.
- Suppression de la gestion de la table `Session` dans les tests Docker Compose.
- Ajout du champ `email` à la factory Profile.
- Ajout de la gestion des catégories d'événements dans les migrations Django.
- Correction de la gestion des types de champs dans les migrations Django.
- Suppression de la dépendance `whitenoise`.
- Ajout d'une tâche quotidienne pour vérifier les mises à jour des dépendances.
