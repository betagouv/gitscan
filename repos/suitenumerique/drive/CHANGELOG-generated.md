## Changelog : drive (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'exportation de dossiers, la réconciliation des comptes utilisateurs et l'amélioration de la prévisualisation des fichiers, notamment des PDF. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter des dossiers en tant qu'archives ZIP. [#1234](https://github.com/suitenumerique/drive/issues/1234)
- Implémentation d'un processus de réconciliation des comptes utilisateurs, incluant une confirmation par email.
- Amélioration de la prévisualisation des fichiers PDF avec affichage des miniatures et navigation par pages.
- Ajout d'un modal d'avertissement pour les conditions d'utilisation lors du partage de fichiers.
- Possibilité de configurer l'utilisation de PKCE pour l'authentification SSO.
- Ajout d'indicateurs de métriques d'organisation à l'API d'utilisation.

### Évolutions techniques
- Suppression des colonnes `numchild` obsolètes de la table `item`.
- Remplacement de `VersionId` par `Etag` pour la compatibilité WOPI.
- Refactorisation du code lié aux entitlements pour une meilleure organisation.
- Mise à jour de la bibliothèque Django en version 5.2.14 (correction de sécurité).
- Mise à jour de la bibliothèque urllib3 en version 2.7.0 (correction de sécurité).
- Migration des imports de types MIME vers la bibliothèque `ui-kit`.
- Amélioration de la gestion des transactions lors de la duplication de fichiers.
- Acceptation du type MIME CDFV2 provenant de libmagic plus récent.
- Refactorisation de la méthode d'envoi d'emails pour les utilisateurs.
- Amélioration de la gestion des erreurs et ajout de logs pour l'action `get_file_content` WOPI.

### Autres changements
- Documentation de la réconciliation des comptes utilisateurs.
- Mise à jour de la version de la bibliothèque `ui-kit`.
- Ajout de tests E2E pour les avertissements d'entitlement et les PDF multi-pages.
- Capture d'événements PostHog pour la duplication d'éléments et les changements de type de colonne.
- Bump de la version de release à 0.18.0.
