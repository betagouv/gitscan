## Changelog : meet (30 derniers jours, au 13 juillet 2026)

### Résumé
Cette version apporte des améliorations à l'expérience utilisateur, notamment au niveau de la mise en page en mode Picture-in-Picture, de l'accessibilité et de la gestion des noms d'utilisateur. Des corrections de bugs ont également été implémentées, ainsi que des optimisations techniques et des mises à jour de dépendances. L'intégration d'un système d'analytics plus flexible est également en cours.

### Évolutions fonctionnelles
- Amélioration de la gestion des noms d'utilisateur, avec la possibilité de forcer l'affichage du nom SSO pour les utilisateurs authentifiés.
- Ajout d'un gradient de couleur pour les participants dont la caméra est désactivée.
- Amélioration de la mise en page en mode Picture-in-Picture (PiP) : priorisation du partage d'écran, gestion du focus et pagination des vignettes.
- Correction d'un crash de l'info panel pour les salles non enregistrées.
- Possibilité de rechercher des enregistrements par adresse email du propriétaire.
- Ajout d'un indicateur visuel pour le bouton "Couper le son de tous" lorsque l'utilisateur a les droits d'administrateur ou de propriétaire.

### Évolutions techniques
- Refactorisation du code pour utiliser la nouvelle API de traitement en arrière-plan.
- Intégration des poids des modèles directement dans le code pour éviter les chargements distants.
- Mise en place d'un système d'analytics configurable basé sur PostHog.
- Refactorisation de l'authentification Bearer.
- Mise à jour de plusieurs dépendances : mjml, @html-to/text-cli, joserfc, cryptography, posthog-js, livekit-client, @tanstack/react-query, react-aria, react-stately, react-aria-components.
- Amélioration de la gestion des variables d'environnement.
- Mise à jour de l'image Docker de base pour les agents.
- Suppression du support de la version 1 de SUMMARY_SERVICE.

### Autres changements
- Ajout de badges DPG au README.
- Documentation améliorée pour la configuration du favicon.
- Clarification des guidelines de contribution.
- Ajout de Clever Cloud comme fournisseur SaaS La Suite Meet.
- Correction de la configuration du build frontend sur Scalingo.
- Ajout d'instrumentation Sentry pour les agents.
- Normalisation des clés d'objets S3 pour la compatibilité.
- Ajout de tests pour le parser S3.
- Correction d'un bug dans le Makefile.
- Mise à jour de l'image de base Alpine pour les résumés.
- Suppression du code lié à SUMMARY_SERVICE_VERSION=1.
- Ajout de documentation concernant la suppression de SUMMARY_SERVICE_VERSION=1.
- Mise à jour de la version de release à 1.23.0 et 1.22.0.
