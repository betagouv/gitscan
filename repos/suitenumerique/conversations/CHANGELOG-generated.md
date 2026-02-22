## Changelog : conversations (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur avec l'ajout d'un mode sombre persistant, une meilleure gestion des fichiers (notamment le support de S3 sans accès externe et un parseur PDF adaptatif) et des optimisations de performance, notamment pour le rendu du markdown en streaming. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de l'application.

### Évolutions fonctionnelles
- Ajout d'un mode sombre persistant, conservant le thème choisi par l'utilisateur.
- Amélioration de la gestion des fichiers : possibilité d'utiliser le stockage S3 sans accès externe (#849).
- Implémentation d'un parseur PDF adaptatif pour une meilleure extraction du texte et de l'OCR (#209).
- Ajout d'une interface utilisateur (UI Kit) avec support du mode sombre (#240).
- Amélioration de l'intégration de l'API Find avec les informations de l'utilisateur et les tags (#209).
- Possibilité de supprimer des collections temporaires (#209).
- Ajout d'un bouton de copie pour le code dans les messages.
- Amélioration de l'affichage des documents PDF et standardisation de l'internationalisation.

### Évolutions techniques
- Migration vers `uv` pour améliorer les performances du backend.
- Optimisation de la taille du bundle de surlignage de syntaxe.
- Refactorisation du service `AIAgentService` pour une meilleure lisibilité et maintenabilité.
- Mise à jour de Django.
- Mise à jour de Pydantic AI.
- Mise à jour de Next.js (version 5.3.9).
- Mise à jour de Protobuf (version 6.33.5).
- Refactorisation des parseurs de documents.
- Correction de problèmes de liveness et readiness pour le déploiement Helm.
- Utilisation d'un fichier `mime.types` vendorisé pour éviter les dépendances externes.

### Autres changements
- Mise à jour des chaînes de traduction (i18n).
- Bump de la version à 0.0.13.
- Suppression de l'exécution de Trivy sur `yarn.lock` pour la génération de mails.
- Correction de problèmes de compatibilité avec les prompts système auto-hébergés.
- Suppression de code mort et de fichiers inutilisés.
- Correction de timeouts lors des appels d'outils.
- Ajout de tests et corrections de bugs liés à l'internationalisation et au rendu des documents.
- Correction de problèmes liés à l'hydratation de React et aux erreurs de rendu.
- Passage de `UUID` à `str` pour l'identifiant utilisateur dans PostHog.
- Correction de problèmes liés à l'envoi de types de fichiers interdits.
- Correction de liens `target="_blank"` dans le chat.
- Activation du tracing Langfuse avec contenu masqué.
- Correction de l'envoi de messages longs.
- Correction de problèmes liés à l'affichage des formules mathématiques et des carrousels.
