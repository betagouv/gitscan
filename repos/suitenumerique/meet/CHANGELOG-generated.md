## Changelog : meet (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de fonctionnalités d'intégration avec des add-ons comme Microsoft Outlook (en phase alpha), l'amélioration de la sécurité avec des mises à jour de dépendances, et l'ajout de capacités de collecte de métadonnées pour une meilleure analyse et optimisation de la plateforme. Des corrections de bugs et des améliorations d'accessibilité ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un support initial (alpha) pour l'intégration avec Microsoft Outlook via un add-in [#4548f69].
- Possibilité d'activer ou non l'authentification des add-ons via un paramètre de configuration [#012857f, #6f38d60].
- Amélioration du texte du lien de téléchargement de la transcription audio en français [#bb816eb].
- Ajout de la prise en charge de nouveaux formats de fichiers pour la transcription [#28acbb5].
- Introduction d'une nouvelle version de l'API pour les tâches asynchrones de transcription et de résumé [#5a70604].

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (Pillow, aiohttp, vite, django, pytest) [#34f9dea, #d8ccd02, #08aa63e, #b80c46d, #4d222e4].
- Refactorisation de l'authentification LiveKit pour utiliser l'en-tête `Authorization` [#5d7a54e].
- Amélioration de la gestion des erreurs Twirp [#3ccb2d4].
- Ajout de tests unitaires pour le service de gestion des jetons JWT [#6b656ee].
- Mise à jour de l'image Docker pour inclure le support multi-utilisateur pour le transcripteur [#812d80c].
- Amélioration de la collecte de métadonnées avec l'ajout de la collecte d'événements VAD, de connexion et de chat [#8507cdd, #73dd684].
- Contrôle du lancement de l'agent de collecte de métadonnées via un indicateur de fonctionnalité [#3b474ba].
- Optimisation de l'utilisation de PostHog et enrichissement des métadonnées des événements [#170763a].
- Suppression d'une commande obsolète pour la récupération de secrets externes [#6374e13].
- Mise à jour de la configuration Nginx pour permettre la surcharge de la configuration par défaut [#3d125e9].
- Alignement du token CSRF avec les conventions Django [#181b97b].

### Autres changements
- Mise à jour de la documentation pour la méthode `summary` [#4fdc2ee].
- Amélioration de l'accessibilité de la page de téléchargement des enregistrements et de la barre d'outils de réactions [#f0fda14, #d12ced3].
- Correction d'une indentation dans le Makefile [#52fbd56].
- Publication de nouvelles versions des charts Helm [#6bb8084, #df24aaa, #bb8f61, #4bf3ba4].
- Epinglage de l'image Docker à une version spécifique pour des builds reproductibles [#5a81e2b].
- Mise à jour du Makefile pour metadata-collector-dev [#fc4b6d6].
