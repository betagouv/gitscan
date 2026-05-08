## Changelog : meet (30 derniers jours, au 7 mai 2026)

### Résumé
Les dernières mises à jour de Meet se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de nouvelles options d'accessibilité (taille de police personnalisable), l'amélioration de la sécurité (génération d'IDs de salle plus robustes), et l'introduction d'un support préliminaire pour un add-in Microsoft Outlook. Des optimisations techniques ont également été apportées, notamment pour la collecte de métadonnées et la gestion des enregistrements.

### Évolutions fonctionnelles
- Ajout d'un sélecteur de police dans les paramètres d'accessibilité pour personnaliser la taille de la police d'affichage. [#1270](https://github.com/suitenumerique/meet/issues/1270)
- Support initial (alpha) d'un add-in pour Microsoft Outlook, permettant une intégration plus poussée avec l'outil de visioconférence. [#1265](https://github.com/suitenumerique/meet/issues/1265)
- Amélioration de la clarté du texte du lien de téléchargement des transcriptions audio en français. [#1299](https://github.com/suitenumerique/meet/issues/1299)
- Possibilité de configurer l'encodage utilisé pour les enregistrements LiveKit Egress. [#1288](https://github.com/suitenumerique/meet/issues/1288)
- Ajout de la prise en charge de l'extension de fichier WebM pour les enregistrements. [#1290](https://github.com/suitenumerique/meet/issues/1290)
- Amélioration de l'affectation des participants aux résultats de la diarisation audio.

### Évolutions techniques
- Refactorisation de la signature des tâches pour une meilleure gestion des fuseaux horaires.
- Validation de la configuration des salles avec un schéma Pydantic pour garantir la cohérence des données.
- Mise à jour de l'infrastructure pour supporter plusieurs workers de transcription. [#1247](https://github.com/suitenumerique/meet/issues/1247)
- Amélioration de la robustesse du processus de démarrage de l'enregistrement pour éviter les erreurs.
- Utilisation de l'en-tête `Authorization` pour l'authentification des tokens LiveKit.
- Collecte de métadonnées sur les événements VAD, de connexion et de chat pour une analyse plus approfondie.
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité (PostCSS, Webpack-dev-server, Pytest, Django).
- Amélioration de la gestion des erreurs Twirp pour les opérations sur les participants.
- Standardisation de la terminologie des rôles dans les différentes langues.
- Mise à jour de l'image frontend vers Alpine 3.23 pour corriger des CVEs.
- Amélioration de la configuration Nginx pour le frontend DINUM.

### Autres changements
- Mise à jour de la documentation et des outils de publication pour supporter la gestion des dépendances basées sur UV.
- Suppression d'une commande obsolète pour la récupération de secrets externes.
- Amélioration du suivi des candidats WebRTC dans PostHog pour une meilleure analyse des performances.
- Correction de problèmes mineurs dans l'add-in Outlook en phase alpha.
- Correction de bugs liés à la boucle de reconnexion et à l'accès aux fonctionnalités.
- Mise à jour de la version de `django-lasuite`.
- Amélioration des tests unitaires pour le service de gestion des tokens JWT.
- Mise à jour de la version du changelog.
