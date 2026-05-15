## Changelog : meet (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la qualité de la transcription et du résumé des réunions, avec l'ajout de la prise en charge du format WebM et l'amélioration de l'attribution des intervenants. Des travaux importants ont également été réalisés pour préparer l'intégration d'add-ons, notamment un support initial pour Microsoft Outlook. Des corrections de bugs et des mises à jour de sécurité ont également été apportées pour améliorer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Amélioration de l'attribution des intervenants lors de la transcription des réunions.
- Ajout de la prise en charge du format WebM pour les transcriptions.
- Introduction d'un support initial (alpha) pour l'intégration avec Microsoft Outlook via un add-in.
- Amélioration de la clarté du texte du lien pour ouvrir les transcriptions audio en français.
- Possibilité de configurer l'encodage des enregistrements LiveKit Egress.
- Ajout de plusieurs options d'accessibilité, notamment la possibilité de personnaliser la police d'affichage.
- Ajout de la collecte de métadonnées sur les événements VAD, de connexion et de chat.

### Évolutions techniques
- Utilisation de `uv` pour la gestion des dépendances Python, améliorant la performance et la fiabilité.
- Refactorisation de la signature des tâches de transcription et de résumé pour une meilleure gestion des fuseaux horaires.
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (urllib3, Pillow, aiohttp, vite, pytest, postcss, webpack-dev-server).
- Amélioration de la configuration Nginx pour le frontend DINUM.
- Mise à jour de l'image frontend vers Alpine 3.23 pour corriger des CVE.
- Validation de la configuration des salles avec un schéma Pydantic.
- Amélioration de la gestion des erreurs Twirp pour les opérations sur les participants.
- Ajout de tests unitaires pour le service JwtTokenService.
- Mise à jour de l'outil de build pour la gestion des dépendances basées sur `uv`.
- Amélioration de l'atomicité et de la tolérance aux pannes du processus de démarrage de l'enregistrement.

### Autres changements
- Ajout de métriques de suivi des candidats WebRTC dans PostHog.
- Correction de bugs mineurs dans l'add-in Outlook (alpha).
- Amélioration de la journalisation de l'attribution des intervenants.
- Correction d'un bug de boucle de reconnexion causée par les mises à jour de connectionObserverStore.
- Correction d'un bug dans l'assign_user.
- Mise à jour de la documentation et des configurations pour supporter les nouvelles fonctionnalités.
- Mise à jour des charts Helm pour supporter les nouvelles fonctionnalités et les add-ins.
- Standardisation de la terminologie des rôles dans les localisations.
- Suppression d'un bug dans le webhook de notification.
- Correction de la configuration du chargement des nonces dans le frontend.
- Correction d'un problème de typographie dans les paramètres des add-ons.
- Ajout d'un ignore ruff pour le run ffprobe.
