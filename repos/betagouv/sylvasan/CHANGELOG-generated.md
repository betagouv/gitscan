## Changelog : sylvasan (30 derniers jours, au 15 juillet 2026)

### Résumé
Cette période a été marquée par une amélioration significative de l'application mobile et web, avec l'ajout de nouvelles fonctionnalités comme la duplication d'enquêtes, la gestion des follow-ups (suivis), et la suppression de réponses. De nombreuses corrections de bugs et mises à jour de dépendances ont également été intégrées pour améliorer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité de duplication d'une enquête existante [#452](https://github.com/betagouv/sylvasan/issues/452).
- Implémentation de la gestion des follow-ups (suivis) : création, modification, affichage sur le web et via l'API [#469](https://github.com/betagouv/sylvasan/issues/469).
- Possibilité de supprimer une réponse [#412](https://github.com/betagouv/sylvasan/issues/412).
- Ajout d'un indicateur visuel lors de la synchronisation des données sur les enquêtes [#388](https://github.com/betagouv/sylvasan/issues/388).
- Ajout d'un modal de confirmation pour la déconnexion.
- Amélioration de l'affichage de l'autocomplete et correction de son positionnement.
- Ajout d'une fonctionnalité de rafraîchissement automatique des données.
- Ajout de la possibilité de créer des follow-ups à partir de l'URL d'une réponse.
- Ajout de champs par défaut pour les types de champs select, radio et autocomplete.

### Évolutions techniques
- Mises à jour de nombreuses dépendances (Django, React, Node.js, PostgreSQL, Sentry, Ruff, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performance.
- Refactoring du code pour améliorer la maintenabilité et la lisibilité.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités et corrections de bugs.
- Amélioration de la gestion des erreurs et des exceptions.
- Mise à jour des versions iOS et Android de l'application mobile.
- Utilisation de PostGIS et PointField pour les réponses.
- Amélioration de la gestion des timezones.
- Ajout de documentation pour les permissions des rôles.

### Autres changements
- Correction de bugs mineurs dans l'interface utilisateur et le comportement de l'application.
- Amélioration de la documentation interne.
- Ajout d'un ADR (Architectural Decision Record) pour le prop-drilling.
- Suppression de code inutile et nettoyage du codebase.
- Correction de l'ordre de navigation après un suivi.
- Fix de la sauvegarde des brouillons.
- Correction du bug de modification des suivis.
- Ajout de messages d'erreur pour l'authentification.
- Mise à jour du pre-commit.
