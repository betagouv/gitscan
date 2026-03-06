## Changelog : rapportnav2 (30 derniers jours)

### Résumé
Cette version apporte des améliorations à l'interface d'administration, notamment la pagination et la recherche dans la liste des informations générales, ainsi que la possibilité de supprimer ces informations. Des corrections de bugs ont été implémentées pour améliorer la stabilité et la fiabilité de l'application, en particulier concernant la gestion des ressources et des coordonnées GPS. Des mises à jour de sécurité et des améliorations de la journalisation ont également été effectuées.

### Évolutions fonctionnelles
- Ajout de la pagination et de la recherche sur la page d'administration des informations générales.
- Possibilité de supprimer des informations générales depuis l'interface d'administration.
- Correction de l'affichage du nombre de cibles sur le titre.
- Correction du formulaire de coordonnées GPS dans l'interface utilisateur.

### Évolutions techniques
- Mise à jour de la version de Gradle vers la version 9.
- Mise à jour de plusieurs dépendances frontend, notamment Vitest.
- Amélioration de la gestion des erreurs et implémentation des réponses RFC 7807 Problem Detail.
- Ajout de la journalisation des événements d'authentification et d'audit des clés API.
- Amélioration de la configuration de la sécurité (CORS et CSRF).
- Correction d'un problème lié à la gestion des ressources et de leur statut "complété" pour les statistiques.
- Correction d'un problème lié à l'utilisation de l'ID de l'unité de contrôle lors de la mise à jour des ressources.
- Amélioration de la gestion des sessions Sentry.
- Correction de problèmes liés à la configuration de Sentry.

### Autres changements
- Mise à jour des dépendances de sécurité (npm audit fix).
- Correction de bugs mineurs et améliorations de la qualité du code.
- Suppression de code inutile et nettoyage du code.
- Mise à jour de la documentation.
- Correction de problèmes de build et de packaging.
- Correction de tests unitaires.
