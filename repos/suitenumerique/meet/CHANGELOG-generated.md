## Changelog : meet (30 derniers jours, au 13 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la stabilité et à l'expérience utilisateur, notamment dans la gestion des enregistrements, l'intégration SSO, et l'accessibilité. Des optimisations ont également été apportées à l'infrastructure et aux outils de développement.

### Évolutions fonctionnelles
- Amélioration de l'affichage des vignettes en mode Picture-in-Picture, avec pagination et limitation du nombre d'éléments affichés.
- Possibilité de forcer l'affichage du nom d'utilisateur SSO pour les utilisateurs authentifiés.
- Ajout d'un gradient de couleur pour les participants dont la caméra est désactivée.
- Amélioration de l'accessibilité du panneau latéral, notamment la gestion du focus.
- Correction d'un crash du panneau d'informations pour les salles non enregistrées.
- Possibilité de rechercher les enregistrements par adresse email du propriétaire.
- Prise en charge de fichiers média avec des flux corrompus lors de la transcription.
- Amélioration de l'intégration de LiveKit pour la sauvegarde des enregistrements.

### Évolutions techniques
- Refactorisation du code pour utiliser la nouvelle API de traitement en arrière-plan.
- Intégration du SDK PostHog dans le backend pour un suivi analytique plus précis.
- Mise à jour de plusieurs dépendances : mjml, @html-to/text-cli, joserfc, cryptography, posthog-js, livekit-client, @tanstack/react-query, react-aria, react-stately, react-aria-components.
- Mise à jour de l'image de base Alpine pour les services de résumé.
- Refactorisation du code d'authentification Bearer.
- Amélioration de la gestion des variables d'environnement.
- Mise à jour de l'image Docker nginx.
- Suppression du support de la version 1 de SUMMARY_SERVICE.
- Amélioration de la gestion des erreurs et de l'instrumentation avec Sentry pour les agents.

### Autres changements
- Documentation mise à jour avec des informations sur Clever Cloud et les contributions.
- Ajout d'un badge DPG au README.
- Clarification des consignes de contribution dans la documentation.
- Correction de la configuration Helm pour le rendu des hôtes multiples.
- Ajout de tests pour la normalisation des clés S3.
- Correction de la configuration de l'environnement pour les collecteurs de métadonnées.
- Mise à jour de la version du release à 1.23.0 puis 1.22.0.
- Ajout de notes concernant la suppression de la version v1 de summary.
