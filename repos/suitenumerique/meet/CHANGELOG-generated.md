## Changelog : meet (30 derniers jours, au 2026-07-30)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur, notamment en optimisant les performances de l'interface, en ajoutant des fonctionnalités de gestion des participants (rôles, promotion) et en améliorant la robustesse du système, en particulier pour la transcription et l'analyse. Des mises à jour de sécurité et de dépendances ont également été intégrées.

### Évolutions fonctionnelles
- Ajout de la possibilité de modifier le rôle d'un participant pendant une réunion. [#1510](https://github.com/suitenumerique/meet/issues/1510)
- Affichage d'un badge indiquant si un participant est authentifié.
- Possibilité de promouvoir des participants authentifiés en administrateurs.
- Amélioration de l'affichage du nom des participants dans la liste.
- Ajout d'un gradient de couleur pour les participants avec la caméra désactivée.
- Ajout d'un lien configurable vers la documentation.
- Possibilité de forcer l'affichage du nom SSO pour les utilisateurs authentifiés.
- Affichage des initiales en majuscules dans les avatars.
- Ajout d'outils d'add-in lors de la création de réunions dans les calendriers partagés.

### Évolutions techniques
- Refactorisation importante du code du chat pour améliorer les performances et la maintenabilité.
- Optimisations significatives des performances du frontend, notamment en virtualisant les messages du chat, en optimisant le rendu des métadonnées des participants et en réduisant les re-renders inutiles.
- Refactorisation du code lié à la liste des participants et au panneau latéral.
- Amélioration de la gestion des permissions et de l'authentification.
- Mise à jour de plusieurs dépendances (LiveKit, React Query, PostHog, etc.).
- Mise à jour de l'image Docker pour utiliser nginx-unprivileged:1.30.3-alpine3.23.
- Mise à jour de la version de Python utilisée pour les agents.
- Refactorisation de l'authentification basée sur Bearer Token.
- Amélioration de la gestion des erreurs et de la résilience du système, notamment pour la transcription et l'analyse.
- Ajout d'instrumentation Sentry pour les agents.

### Autres changements
- Mise à jour des conditions d'utilisation.
- Ajout d'un fichier `publiccode.yml`.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Suppression de code obsolète lié à l'ancienne version de l'API de résumé.
- Correction de la gestion des erreurs dans l'analyse.
- Amélioration de la gestion des erreurs de transcription.
- Correction de la gestion des webhooks de défaillance.
- Mise à jour de la version du chart Helm.
- Ajout de tests unitaires pour la transcription.
