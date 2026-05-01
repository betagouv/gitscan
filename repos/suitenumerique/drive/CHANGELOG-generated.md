## Changelog : drive (30 derniers jours, au 2026-04-30)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur avec l'ajout de fonctionnalités comme la duplication d'éléments, l'affichage des miniatures PDF, et la gestion des droits d'accès. Des corrections de bugs et des optimisations de performance ont également été apportées, notamment au niveau de la gestion des téléchargements et de la sécurité.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité de duplication d'éléments avec indication visuelle de l'état d'avancement. [#659]
- Amélioration de la gestion des téléchargements avec affichage de la progression, des erreurs et la possibilité d'annulation.
- Ajout d'un modal d'avertissement concernant les conditions d'utilisation des données.
- Possibilité de configurer la durée de validité des invitations via une variable d'environnement.
- Affichage des miniatures PDF avec une barre latérale de navigation et des options de zoom.
- Ajout de la possibilité de trier les éléments par date de création et par nom du créateur.
- Ajout de colonnes personnalisables dans l'explorateur de fichiers.
- Correction : Affichage correct des fichiers dans les dossiers en lecture seule.
- Correction : Correction d'un bug empêchant l'annulation des téléchargements après la suppression du dossier parent.
- Correction : Correction d'un problème de blocage de la sélection lors de la sélection de nombreux éléments.
- Correction : Correction d'un problème d'affichage des éléments dans la corbeille après une suppression définitive.

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité (Django, pytest, vite, next).
- Refactorisation du code lié à la gestion des droits d'accès.
- Amélioration de la gestion des transactions en cas d'actions dupliquées.
- Ajout de tests E2E pour les nouvelles fonctionnalités et corrections de bugs.
- Optimisation des performances des tests E2E avec mise en cache des navigateurs et parallélisation.
- Amélioration de la configuration de l'environnement de déploiement (Scalingo).
- Ajout d'une commande pour purger les éléments supprimés.
- Configuration d'une tâche cron quotidienne pour la purge des éléments supprimés.
- Mise en place d'une configuration dynamique de PostgreSQL.
- Amélioration de la gestion des jetons d'authentification (PKCE).

### Autres changements
- Mise à jour de la documentation.
- Suppression de la fonctionnalité de mirroring.
- Suppression de la fonctionnalité d'affichage des miniatures PDF en cas d'erreur.
- Correction de la configuration du type MIME pour les fichiers .mjs.
- Ajout de variables d'environnement pour la configuration de l'application.
- Mise à jour des notes de version.
- Amélioration de la gestion des erreurs et des messages d'information.
- Correction de problèmes de style et d'affichage.
