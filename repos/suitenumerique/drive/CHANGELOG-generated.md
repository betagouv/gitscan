## Changelog : drive (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur avec l'ajout d'un visualiseur PDF, la possibilité de dupliquer des fichiers, et des améliorations significatives de l'interface utilisateur, notamment dans l'explorateur de fichiers et la gestion des téléchargements. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un visualiseur PDF intégré avec barre latérale de vignettes, zoom et navigation par pages. [#659](https://github.com/suitenumerique/drive/issues/659)
- Possibilité de dupliquer des fichiers et dossiers avec une indication visuelle de l'état de la duplication.
- Amélioration de la gestion des téléchargements avec affichage de la progression, gestion des erreurs et possibilité d'annulation.
- Ajout de la configuration de la durée de validité des invitations de partage via une variable d'environnement.
- Possibilité de trier les éléments par date de création et par nom du créateur.
- Ajout de colonnes personnalisables dans l'explorateur de fichiers.
- Ajout d'un menu d'actions sur mobile.
- Amélioration de l'interface utilisateur pour la suppression d'éléments (corbeille).

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité (pytest, vite, next, requests).
- Amélioration de la configuration CI/CD avec la mise en cache des navigateurs Playwright et la pré-construction du frontend.
- Refactorisation du code du visualiseur de fichiers pour une meilleure maintenabilité.
- Utilisation de React Query pour la gestion des données du visualiseur PDF.
- Amélioration de la configuration Nginx pour servir correctement les fichiers .mjs.
- Ajout d'une variable d'environnement pour configurer l'URL des clés JWKS.
- Ajout d'une commande pour purger les éléments supprimés.
- Configuration d'une tâche cron quotidienne pour purger les éléments supprimés.

### Autres changements
- Mise à jour de la documentation et du changelog.
- Ajout de tests E2E pour les nouvelles fonctionnalités et corrections de bugs.
- Suppression de la fonctionnalité de mirroring.
- Nettoyage du code et suppression de fichiers inutiles.
- Amélioration des messages d'erreur et des traductions.
- Ajout de tests unitaires pour certaines fonctionnalités.
- Ajout de commentaires et documentation pour faciliter la compréhension du code.
- Correction de problèmes de style et d'accessibilité.
- Ajout de la prise en charge de l'indexation par les moteurs de recherche.
- Ajout de la configuration dynamique de PostgreSQL.
- Ajout de la configuration de l'URL de l'email via une variable d'environnement.
