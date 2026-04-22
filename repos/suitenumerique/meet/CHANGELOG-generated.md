## Changelog : meet (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité, l'accessibilité et l'ajout de nouvelles fonctionnalités pour la transcription et la collecte de métadonnées. Des corrections de bugs et des mises à jour de dépendances ont également été apportées pour améliorer la stabilité et la sécurité de la plateforme. L'équipe a également travaillé sur l'amélioration de l'expérience développeur et de l'infrastructure.

### Évolutions fonctionnelles
- Ajout du support multi-tenant et d'une nouvelle API pour les tâches de transcription asynchrone et de résumé (#1171).
- Possibilité de télécharger les enregistrements avec un titre de document explicite pour une meilleure accessibilité (#1261).
- Amélioration de l'accessibilité de la barre d'outils de réactions, avec un raccourci clavier pour l'ouvrir (#1262).
- Extension des types de fichiers autorisés pour le partage (#1265).
- Amélioration de l'affichage du raccourci clavier spécifique au système d'exploitation pour les participants (#1193).

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (Pillow, aiohttp, vite, django, pytest).
- Utilisation de l'en-tête `Authorization` pour l'authentification avec le token LiveKit.
- Refactorisation du système de réactions pour unifier l'état et le rendu.
- Amélioration de la gestion des erreurs Twirp pour les opérations sur les participants.
- Ajout de la collecte de métadonnées sur l'activité VAD (Voice Activity Detection), les connexions et le chat.
- Fixation de l'image Docker pour des builds reproductibles.
- Configuration de l'engine de session via une variable d'environnement.
- Suppression d'outils de développement obsolètes (Tilt).
- Amélioration de la documentation Swagger pour clarifier l'exigence d'un slash final dans les URLs.

### Autres changements
- Ajout de tests unitaires pour le service de token JWT.
- Amélioration de l'accessibilité de la navigation dans la barre latérale.
- Optimisation de l'utilisation des sondages PostHog et enrichissement des métadonnées des événements.
- Suppression de l'affichage des adresses e-mail dans les logs d'échec d'invitation.
- Correction d'un bug empêchant la sélection correcte du périphérique lors d'une conférence.
- Ajout de contexte de sécurité pour les pods et conteneurs dans le Helm chart.
- Mise à jour du chart Helm vers la version 0.0.20.
- Correction d'un bug dans l'endpoint de mise à jour des participants.
- Suppression de la récupération d'informations secrètes externes obsolètes.
- Ajout du support pour Docker Compose pour le service multi-user-transcriber.
- Correction d'indentations dans le Makefile.
- Amélioration de la gestion des erreurs de module avec uv-build.
- Ajout de commentaires et amélioration de la documentation pour la méthode de résumé.
- Suppression de valeurs Helm de développement inutilisées.
- Ajout de la possibilité de configurer les secrets Kubernetes pour l'environnement Tilt.
- Correction d'un warning concernant la longueur de la clé dans les tests.
