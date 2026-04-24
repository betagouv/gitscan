## Changelog : drive (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur avec l'ajout d'un visualiseur PDF, de nouvelles fonctionnalités de duplication de fichiers, et des améliorations significatives de la gestion des fichiers et des permissions. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de la plateforme. Des améliorations de sécurité ont été intégrées, notamment la configuration de variables d'environnement et la mise à jour de dépendances.

### Évolutions fonctionnelles
- Ajout d'un visualiseur PDF intégré avec barre latérale de vignettes, zoom et navigation par pages. [#659]
- Possibilité de configurer la durée de validité des invitations de partage via une variable d'environnement.
- Ajout de la fonctionnalité de duplication de fichiers avec indication visuelle de l'état d'avancement.
- Ajout de la possibilité de trier les fichiers par date de création et par nom du créateur.
- Amélioration de l'expérience d'upload avec affichage de la progression, gestion des erreurs et possibilité d'annulation.
- Ajout de la possibilité de personnaliser les colonnes affichées dans l'explorateur de fichiers.
- Ajout d'un menu d'actions sur mobile pour faciliter la gestion des fichiers.
- Correction d'un bug empêchant l'affichage correct du menu "+ Nouveau" dans les dossiers en lecture seule.
- Correction d'un bug de blocage de la sélection de fichiers dans les dossiers volumineux.
- Correction d'un bug empêchant l'affichage correct des fichiers dans la corbeille après une suppression définitive.

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité (pytest, vite, next, requests).
- Amélioration de la configuration de l'infrastructure avec l'ajout d'une variable d'environnement pour l'URL de l'email.
- Refonte de la gestion des previews de fichiers pour une meilleure performance et maintenabilité.
- Amélioration de la configuration CI/CD pour des builds plus rapides et fiables.
- Mise en place de tests E2E plus robustes pour la fonctionnalité de duplication de fichiers et le visualiseur PDF.
- Pré-compilation du frontend et service via Nginx pour améliorer les performances des tests E2E.
- Restriction des permissions du token utilisé par le workflow frontend pour une meilleure sécurité.
- Utilisation de React Query pour la gestion des données du visualiseur PDF.
- Amélioration de la gestion des erreurs et des exceptions côté backend.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements de configuration.
- Ajout de tests unitaires et E2E pour les nouvelles fonctionnalités.
- Nettoyage du code et suppression de code obsolète.
- Mise à jour des traductions pour les nouvelles fonctionnalités.
- Ajout de la possibilité de configurer une période de grâce pour la suppression définitive des fichiers.
- Amélioration de la gestion des erreurs CSRF.
- Ajout de la possibilité de définir des origines CSRF supplémentaires via une variable d'environnement.
- Correction de problèmes de style et d'affichage dans l'interface utilisateur.
- Ajout de la prise en charge de l'indexation par les moteurs de recherche.
- Amélioration de la gestion des vignettes PDF.
- Ajout d'un mécanisme de purge des éléments supprimés.
