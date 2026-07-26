## Changelog : meet (30 derniers jours, au 24 juillet 2026)

### Résumé
Cette version apporte de nombreuses optimisations de performance, notamment au niveau de l'interface utilisateur et de la gestion des participants. Des améliorations ont également été apportées à la gestion des erreurs et à l'intégration d'outils d'analyse. Enfin, des corrections de bugs et des améliorations d'accessibilité ont été implémentées.

### Évolutions fonctionnelles
- Ajout d'une option pour configurer le lien vers la documentation dans l'interface.
- Possibilité de forcer l'affichage du nom d'utilisateur SSO pour les utilisateurs authentifiés.
- Intégration d'outils d'add-in lors de la création de réunions dans les calendriers partagés.
- Amélioration de la gestion des erreurs dans le service de résumé (summary).
- Ajout d'une coloration des participants en fonction de l'état de leur caméra.
- Possibilité de rechercher des enregistrements par email du propriétaire.

### Évolutions techniques
- Refactorisation importante du code de la chat, améliorant sa structure et ses performances.
- Optimisations de rendu des composants de l'interface utilisateur (participants, avatars, etc.) pour réduire la charge sur le navigateur.
- Utilisation de Valtio pour gérer le contexte des pistes vidéo.
- Refactorisation du code lié à la liste des participants et au focus.
- Amélioration de la gestion des événements et des abonnements pour réduire les re-rendus inutiles.
- Mise à jour des dépendances : LiveKit, React Query, PostHog, i18next, MediaPipe.
- Mise à jour de l'image de construction frontend vers Node 22.
- Amélioration de la gestion des variables d'environnement.
- Refactorisation du code lié à l'authentification Bearer.
- Intégration de PostHog pour l'analyse.
- Mise à jour de l'image Docker nginx.

### Autres changements
- Correction d'un bug d'alignement des initiales dans les avatars.
- Correction d'un bug lié à la réinitialisation de l'état du chat lors du montage du composant.
- Correction d'un bug lié à la référence `pinnedTrackRef`.
- Ajout de tests pour la transcription.
- Amélioration de l'accessibilité des contrôles de pagination.
- Mise à jour de la documentation et des exemples.
- Nettoyage du code et suppression de code obsolète.
- Correction de la gestion des erreurs dans les tâches asynchrones.
- Amélioration de la gestion des notifications S3.
- Mise à jour des images de base Alpine et FFMPEG.
- Ajout de documentation pour la personnalisation du favicon.
- Précision de la traduction française dans la documentation.
