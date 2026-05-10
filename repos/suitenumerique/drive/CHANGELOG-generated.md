## Changelog : drive (30 derniers jours, au 4 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur avec l'ajout de fonctionnalités comme les entités légales, l'affichage des PDF, et l'amélioration des previews de fichiers. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de la plateforme, notamment concernant les uploads, les permissions et les previews. Des améliorations techniques ont été réalisées pour la gestion des événements, la configuration SSO et la purge des éléments supprimés.

### Évolutions fonctionnelles
- Ajout d'une modal d'acceptation des conditions d'utilisation (entitlement disclaimer) pour l'utilisation de certaines fonctionnalités.
- Amélioration de l'affichage des fichiers PDF avec un rendu page par page et des dimensions adaptées.
- Ajout de la possibilité de dupliquer des éléments avec un suivi visuel de l'état de l'opération.
- Amélioration du toast d'upload avec affichage de la progression, des erreurs et la possibilité d'annuler.
- Ajout d'une nouvelle icône d'erreur et support de différentes tailles.
- Possibilité de rendre les uploads annulables.
- Ajout de la possibilité de configurer la durée de validité des invitations via une variable d'environnement.
- Ajout de métriques d'organisation à l'API d'utilisation.
- Ajout d'une commande pour purger les éléments supprimés.
- Configuration d'une tâche cron quotidienne pour purger les éléments supprimés.

### Évolutions techniques
- Refactorisation des entitlements dans un package backend dédié.
- Amélioration de la gestion des transactions lors de la duplication d'éléments.
- Acceptation du type MIME CDFV2 provenant de libmagic plus récent.
- Modification de la route `/wopi/<uuid>` pour rediriger vers la page de l'élément WOPI.
- Refactorisation des viewers de preview et de `FilesPreview`.
- Amélioration de la gestion des erreurs et des tests E2E pour les previews de fichiers.
- Mise à jour des dépendances : Pillow (v12.2.0), pytest (v9.0.3), vite (v6.4.2), next (v15.5.15).
- Ajout d'une variable d'environnement pour configurer l'URL de l'email.
- Possibilité de configurer PKCE pour l'authentification SSO.
- Amélioration de la gestion des tests E2E pour les previews et les uploads.
- Suppression de la fonctionnalité de mirroring.

### Autres changements
- Mise à jour de la documentation du changelog.
- Ajout de documentation sur la configuration en réseau local.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout d'événements PostHog pour le suivi des colonnes personnalisées et de la duplication d'éléments.
- Journalisation de la taille maximale de fichier attendue par WOPI.
- Suppression de la prise en charge des fichiers .mjs par Nginx.
- Amélioration des tests unitaires et E2E.
