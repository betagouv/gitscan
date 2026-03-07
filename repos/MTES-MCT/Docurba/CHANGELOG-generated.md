## Changelog : Docurba (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par d'importantes améliorations de l'administration de l'application, notamment au niveau de la gestion des procédures et des événements. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des mises à jour de dépendances pour assurer la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Amélioration de l'affichage des informations relatives aux procédures dans l'interface d'administration (commentaire, périmètre actuel, statut).
- Affichage des événements liés à une procédure dans la page de modification de cette dernière.
- Correction d'un bug empêchant l'ouverture de la vue de modification d'une procédure.
- Recherche de procédures par identifiant dans l'interface d'administration.
- Affichage du code de la collectivité porteuse dans l'administration des procédures.
- Les événements de caducité d'un POS donnent le statut "Caduc".
- Désactivation des enquêtes pour les DDT non incluses dans la liste `DDT_ENQUETE_ENABLED`.
- Désactivation de la modification de l'adresse email dans l'administration.
- Harmonisation de la description de la liste des DU (Droits Unifiés) sur les pages collectivité.

### Évolutions techniques
- Mise à jour de Django de la version 5.2.11 à la version 6.0.
- Refonte de l'architecture Django avec séparation des configurations et des applications.
- Utilisation de Rclone pour synchroniser le dossier d'export.
- Ajout de tests unitaires pour les modules Django.
- Amélioration des performances du modèle Event.
- Correction de problèmes de N+1 queries sur l'API.
- Ajout de la fonctionnalité de profiling Sentry.
- Transformation des logs en format JSON pour Datadog.
- Spécification de la version de Pytest.
- Mise à jour de plusieurs dépendances : `ruff`, `django-environ`, `pytest-django`, `sqlparse`.

### Autres changements
- Ajout d'usines pour générer de faux objets pour les tests.
- Réusinage du code avec l'utilisation des usines.
- Ajout d'un "cooldown" de 7 jours pour Dependabot.
- Documentation de l'API avec des exemples utilisant `avant=2026-01-01`.
- Plusieurs reverts de modifications récentes suite à des problèmes détectés.
