## Changelog : meet (30 derniers jours, au 2026-04-24)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité, l'ajout de nouvelles fonctionnalités pour la transcription et la gestion des tâches, ainsi que des corrections de bugs et des optimisations de performance. Des améliorations d'accessibilité ont également été apportées à l'interface utilisateur.

### Évolutions fonctionnelles
- Ajout de l'authentification pour les add-ons, permettant une plus grande flexibilité et sécurité dans l'extension des fonctionnalités.
- Amélioration de la gestion des fichiers supportés, avec l'ajout du format WebM [#1290].
- Introduction d'une nouvelle version de l'API pour les tâches de transcription et de résumé, se rapprochant d'une intégration avec une passerelle API.
- Ajout de la collecte de métadonnées concernant l'activité des utilisateurs (VAD, connexions, chat) pour une meilleure analyse et optimisation.
- Amélioration de l'échelle de notation de la qualité vidéo.
- Possibilité de télécharger les enregistrements avec un titre de document explicite pour une meilleure accessibilité.

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (Pillow, aiohttp, vite, django, pytest).
- Mise à jour de l'image frontend vers Alpine 3.23 pour corriger des CVEs.
- Refonte de la gestion des erreurs Twirp pour les opérations sur les participants.
- Utilisation de l'en-tête `Authorization` pour l'authentification des tokens LiveKit.
- Ajout de contextes de sécurité (Pod et Container) au Helm chart pour une meilleure sécurité.
- Amélioration de la gestion des secrets Kubernetes pour l'environnement de développement.
- Optimisation de l'utilisation des sondages PostHog et enrichissement des métadonnées des événements.
- Fixation de l'image Docker pour des builds reproductibles.
- Mise à jour du chart Helm vers la version 0.0.20.
- Ajout du support Compose pour le service multi-user-transcriber.

### Autres changements
- Ajout d'un fichier `.ruffignore` pour ignorer certains avertissements lors de l'exécution de `ffprobe`.
- Correction d'une indentation dans le Makefile.
- Amélioration de la documentation des méthodes de résumé.
- Ajout de tests unitaires pour le service de gestion des tokens JWT.
- Suppression d'une commande obsolète pour la récupération des secrets externes.
- Mise à jour de la version de release à 1.14.0 et 1.13.0.
