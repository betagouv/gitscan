## Changelog : meet (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'accessibilité, la sécurité et l'ajout de nouvelles fonctionnalités comme le support de plusieurs locataires et les arrière-plans personnalisés. Des corrections de bugs et des optimisations de performance ont également été apportées pour améliorer l'expérience utilisateur globale.

### Évolutions fonctionnelles
- Ajout de la possibilité d'utiliser des arrière-plans personnalisés lors des visioconférences. [#1183](https://github.com/suitenumerique/meet/issues/1183)
- Introduction du support multi-tenant avec une nouvelle API v2 pour les tâches asynchrones de transcription et de résumé. [#1171](https://github.com/suitenumerique/meet/issues/1171)
- Ajout d'options de personnalisation de la couleur et de l'arrière-plan des sous-titres pour une meilleure lisibilité. [#1197](https://github.com/suitenumerique/meet/issues/1197)
- Amélioration de l'accessibilité de la barre d'outils de réactions avec un raccourci clavier dédié. [#1262](https://github.com/suitenumerique/meet/issues/1262)
- Amélioration de l'accessibilité de la page de téléchargement des enregistrements avec un titre de document explicite. [#1261](https://github.com/suitenumerique/meet/issues/1261)
- Extension des types de fichiers autorisés. [#1265](https://github.com/suitenumerique/meet/issues/1265)

### Évolutions techniques
- Refactorisation du système de réactions pour unifier l'état et le rendu.
- Utilisation de l'en-tête `Authorization` pour l'authentification des jetons LiveKit.
- Amélioration de la gestion des erreurs Twirp pour les opérations sur les participants.
- Ajout de tests unitaires pour le service de jetons JWT et l'endpoint de santé.
- Suppression de l'outil de récupération des secrets externes obsolète.
- Initialisation des secrets Kubernetes pour l'environnement Tilt.
- Optimisation de l'utilisation de PostHog et enrichissement des métadonnées des événements.
- Correction de la gestion des erreurs dans les tests Twirp.
- Correction d'un warning concernant la longueur des clés dans les tests.
- Mise à jour de plusieurs dépendances (Django, PyJWT, aiohttp, vite, etc.) pour corriger des failles de sécurité et améliorer la stabilité.
- Ajout de support pour Docker Compose pour le transcripteur multi-utilisateur.
- Amélioration de la configuration de Helm pour la sécurité des pods et conteneurs.

### Autres changements
- Correction de l'indentation dans le Makefile.
- Ajout de documentation et correction de typos.
- Suppression d'anciens outils de développement Tilt.
- Suppression de valeurs Helm inutilisées.
- Correction de problèmes de linting dans le changelog.
- Mise à jour du logo.
- Correction de problèmes d'incompatibilité de dimensions dans le processeur d'arrière-plan personnalisé.
