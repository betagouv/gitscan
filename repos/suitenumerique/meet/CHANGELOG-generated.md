## Changelog : meet (30 derniers jours, au 17 avril 2026)

### Résumé
Les dernières mises à jour de Meet se concentrent sur l'amélioration de la sécurité, l'ajout de nouvelles fonctionnalités pour la transcription et la gestion des tâches, ainsi que des améliorations d'accessibilité et de performance. Des corrections de bugs ont également été apportées pour assurer une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de la collecte de métadonnées sur l'activité des utilisateurs (VAD, connexions, chat) pour une meilleure analyse et optimisation. [#82]
- Amélioration du système de transcription avec la prise en charge de plus d'extensions de fichiers et d'une nouvelle version de l'API pour les tâches asynchrones. [#1171, #1265]
- Ajout de la possibilité de définir un arrière-plan personnalisé.
- Amélioration de l'interface utilisateur pour le téléchargement des enregistrements, avec un titre de document explicite pour une meilleure accessibilité. [#1261]
- Ajout d'un indicateur de chargement avec prévisualisation lors du téléchargement d'un arrière-plan personnalisé.
- Prise en charge de raccourcis clavier pour la barre d'outils de réactions. [#1262]

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (Pillow, aiohttp, vite, django, pytest).
- Amélioration de l'authentification LiveKit en utilisant l'en-tête `Authorization`.
- Refactorisation du système de réactions pour unifier l'état et le rendu.
- Amélioration de la gestion des erreurs Twirp.
- Mise à jour de l'image frontend pour utiliser Alpine 3.23 afin de corriger des CVE.
- Ajout de la configuration de l'engine de session via une variable d'environnement.
- Fix d'un problème d'inclusion de module avec uv-build.
- Pin de l'image Docker pour des builds reproductibles.
- Mise à jour du chart Helm vers la version 0.0.20.
- Ajout de support compose pour multi-user-transcriber.
- Suppression d'outils de développement Tilt obsolètes.

### Autres changements
- Ajout de tests unitaires pour le service JwtTokenService.
- Amélioration de la documentation Swagger pour clarifier les exigences de la barre oblique de fin.
- Amélioration de la journalisation pour éviter la divulgation d'adresses e-mail sensibles.
- Mise à jour des logos.
- Corrections de l'indentation dans le Makefile.
- Optimisation de l'utilisation de PostHog pour les sondages et enrichissement des métadonnées des événements.
- Suppression de la commande obsolète de récupération de secrets externes.
- Initialisation des secrets Kubernetes pour la pile Tilt.
- Amélioration de la sécurité des pods et conteneurs via Helm.
- Mise à jour des dépendances Python.
- Suppression de valeurs Helm inutilisées.
