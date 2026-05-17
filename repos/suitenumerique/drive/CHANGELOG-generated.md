## Changelog : drive (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience de visualisation et de manipulation des fichiers, notamment avec une refonte des prévisualisations et l'ajout de nouvelles fonctionnalités liées aux droits d'accès et à la gestion des fichiers. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité de configurer PKCE pour l'authentification SSO [#2345](https://github.com/suitenumerique/drive/issues/2345).
- Implémentation d'un modal d'avertissement concernant les droits d'accès (entitlement disclaimer) pour les utilisateurs.
- Amélioration de la prévisualisation des fichiers PDF avec affichage des miniatures, zoom et navigation par page.
- Ajout de la possibilité d'ouvrir les fichiers WOPI dans un nouvel onglet.
- Amélioration de la gestion des téléchargements avec la possibilité d'annuler les uploads en cas de suppression du dossier parent.
- Ajout d'indicateurs visuels pour les uploads en cours et gestion des erreurs.
- Ajout de métriques d'organisation à l'API d'utilisation.
- Ajout d'un événement de suivi (PostHog) pour la duplication d'éléments.
- Ajout d'un événement de suivi (PostHog) pour les modifications de type de colonne.

### Évolutions techniques
- Refactorisation du code des prévisualisations de fichiers pour utiliser les composants de l'UI Kit.
- Simplification et amélioration de la gestion des transactions lors de la duplication de fichiers.
- Amélioration de la gestion des types MIME pour une meilleure compatibilité avec les fichiers.
- Refactorisation du code des entitlements pour une meilleure organisation.
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité et améliorer la stabilité (Django, urllib3, pytest, vite, Next.js).
- Amélioration de la configuration de l'environnement pour l'envoi d'emails.
- Optimisation des tests E2E pour une meilleure stabilité et performance.
- Suppression de la fonctionnalité de mirroring.

### Autres changements
- Mise à jour de la documentation (changelog).
- Nettoyage du code et suppression de code inutilisé.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Mise à jour de la version de l'UI Kit.
- Ajout de tests E2E pour les nouvelles fonctionnalités et corrections de bugs.
- Localisation de l'étiquette de chargement du visualiseur d'images.
- Ajout de traductions pour les actions de téléchargement et d'impression.
- Amélioration de la gestion des erreurs dans les prévisualisations de fichiers.
