## Changelog : domifa (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la sécurité de la plateforme, notamment avec l'ajout d'une authentification à deux facteurs (OTP) et des mécanismes de blocage des tentatives d'accès malveillantes. Des améliorations ont également été apportées à la journalisation et à la surveillance de l'application, ainsi qu'à l'interface d'administration pour faciliter la gestion des utilisateurs.

### Évolutions fonctionnelles
- Ajout de la possibilité de renvoyer le code OTP (One-Time Password) pour la connexion.
- Implémentation d'une authentification à deux facteurs (OTP) pour la connexion des utilisateurs.
- Ajout d'une liste d'utilisateurs dans l'interface d'administration.
- Ajout d'un statut pour bloquer les comptes utilisateurs dans l'interface d'administration.
- Ajout d'une page de témoignages.
- Amélioration de l'affichage des listes et des formulaires dans l'interface utilisateur.
- Ajout d'un détail réseau.

### Évolutions techniques
- Renforcement de la sécurité avec l'ajout de limites de tentatives de connexion (throttling) et l'accès restreint aux structures.
- Ajout de la journalisation (logs) plus détaillée pour faciliter le débogage et la surveillance.
- Mise à jour de la version d'Angular à la v19 dans l'interface d'administration.
- Amélioration des tests unitaires et d'intégration.
- Ajout d'un fingerprint dans les sessions pour améliorer la sécurité.
- Refactorisation de la récupération des statistiques pour Metabase.
- Ajout de la gestion des rôles et migration de la base de données.

### Autres changements
- Correction de divers bugs et améliorations de la stabilité de l'application.
- Correction de problèmes liés aux tests unitaires.
- Suppression de Bootstrap dans l'interface d'administration.
- Correction de problèmes d'affichage et de formulaires dans l'interface utilisateur.
- Ajout de tooltips dans l'interface de gestion.
- Correction de problèmes liés aux alertes email.
- Ajout de filtres et débogage de la recherche.
- Correction de problèmes de chargement des utilisateurs.
- Ajout de modèles d'emails pour l'envoi de codes OTP.
- Ajout de statistiques dans l'interface d'administration.
- Correction de problèmes de linting et de composants autonomes dans l'interface d'administration.
