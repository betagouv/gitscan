## Changelog : drive (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec l'intégration de composants d'interface utilisateur plus modernes, l'amélioration de la prévisualisation des fichiers PDF et l'ajout d'un système de disclaimer pour les droits d'accès. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un modal de disclaimer pour les droits d'accès (entitlements) [#1234](https://github.com/suitenumerique/drive/issues/1234)
- Amélioration de la prévisualisation des fichiers PDF avec rendu à la dimension de chaque page et ajout de tests E2E associés.
- Capture d'événements Posthog pour le suivi de l'utilisation des colonnes personnalisées et de la duplication d'éléments.
- Possibilité de configurer l'utilisation de PKCE pour l'authentification SSO.
- Ajout de métriques d'organisation à l'API d'utilisation.
- Amélioration de la gestion des transactions lors de la duplication d'éléments.

### Évolutions techniques
- Remplacement de `VersionId` par `Etag` pour la compatibilité WOPI.
- Refactorisation des composants d'icônes et de prévisualisation de fichiers pour utiliser les composants de la librairie `ui-kit`.
- Refactorisation du code lié aux entitlements dans un nouveau package backend.
- Acceptation du type MIME CDFV2 provenant de versions récentes de `libmagic`.
- Modification de la signature de la fonction `compute_backend` pour accepter un queryset.
- Mise à jour de la librairie `ui-kit`.

### Autres changements
- Mise à jour de la documentation du changelog.
- Ajout de logs pour la taille maximale des fichiers attendue par WOPI.
- Suppression de la fonctionnalité de mirroring.
- Mise à jour des dépendances Python.
