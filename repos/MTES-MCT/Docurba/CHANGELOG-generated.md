## Changelog : Docurba (30 derniers jours)

### Résumé
Les dernières mises à jour de Docurba se concentrent sur l'amélioration de la gestion des procédures et des événements, ainsi que sur la correction de bugs et l'optimisation des performances, notamment au niveau de l'administration Django et de l'interface utilisateur Nuxt. Des efforts ont également été faits pour améliorer la robustesse et la sécurité de l'application.

### Évolutions fonctionnelles
- Amélioration de l'affichage des informations de périmètre dans l'administration Django.
- Ajout de la possibilité de rechercher les procédures par leur ID dans l'administration Django.
- Affichage du code de la collectivité porteuse dans l'administration des procédures [#1234](https://github.com/MTES-MCT/Docurba/issues/1234).
- Correction d'un bug empêchant l'ouverture de la vue de modification des procédures dans l'administration Django.
- Correction d'un bug d'affichage du statut de la procédure dans l'administration Django.
- L'événement de caducité d'un POS lui donne le statut Caduc.
- Désactivation des enquêtes pour les DDT absentes de la liste `DDT_ENQUETE_ENABLED`.
- Désactivation de l'édition de l'email dans l'administration.
- Correction des tris de la page "Mes procédures" dans l'interface Nuxt.
- Correction d'un bug lié au snackbar de réinitialisation du mot de passe dans Nuxt.
- Redirection vers la page collectivité après une connexion réussie dans Nuxt.

### Évolutions techniques
- Mise à jour de Django de la version 5.2.10 à la version 6.0.2.
- Refactorisation du code Django pour améliorer les performances et corriger des problèmes de N+1 queries.
- Amélioration de la gestion des logs avec l'ajout de la transformation en JSON pour Datadog.
- Ajout d'usines pour la génération de faux objets pour les tests.
- Spécification de la version de Pytest dans les dépendances Django.
- Mise à jour de plusieurs dépendances Django (django-environ, pytest-django, ruff, sqlparse, django-browser-reload).
- Amélioration de la gestion des variables d'environnement pour l'URL d'autorisation Supabase.

### Autres changements
- Ajout d'un cooldown de 7 jours pour Dependabot.
- Documentation de l'API avec des exemples utilisant `avant=2026-01-01`.
- Ajout de tests pour toutes les Pull Requests.
- Harmonisation de la description de la liste des DU sur les pages Collectivité.
- Correction de problèmes de linter dans Nuxt.
- Plusieurs reverts de commits suite à des problèmes rencontrés.
