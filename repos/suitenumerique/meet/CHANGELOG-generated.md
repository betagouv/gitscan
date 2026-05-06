## Changelog : meet (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, l'ajout de support pour de nouveaux add-ons (notamment Microsoft Outlook), l'optimisation des performances et la correction de plusieurs bugs. Des améliorations ont également été apportées à la transcription et à la gestion des enregistrements.

### Évolutions fonctionnelles
- Ajout du support initial pour un add-in Microsoft Outlook (en alpha) permettant d'intégrer Meet à l'environnement Outlook.
- Amélioration de la clarté du texte du lien de téléchargement des transcriptions audio en français.
- Possibilité de configurer l'encodage utilisé pour les enregistrements LiveKit Egress.
- Support de plusieurs workers/endpoints pour la transcription.
- Ajout de la prise en charge de formats de fichiers supplémentaires pour la transcription.
- Amélioration de l'échelle de notation de la qualité vidéo.

### Évolutions techniques
- Validation de la configuration des salles avec un schéma Pydantic pour une meilleure robustesse.
- Refonte de la gestion des erreurs Twirp pour les opérations sur les participants.
- Utilisation de l'en-tête `Authorization` pour l'authentification des tokens LiveKit.
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (PostCSS, Webpack-dev-server, Pytest, Django, Aiohttp, Vite).
- Mise à jour de l'image frontend vers Alpine 3.23 pour corriger des CVEs.
- Amélioration de la gestion des secrets Kubernetes pour l'environnement de développement.
- Ajout de métriques pour le suivi des candidats WebRTC.
- Collecte de métadonnées sur les événements VAD, de connexion et de chat.
- Amélioration de la gestion des dépendances avec `uv`.
- Génération des IDs de salle avec un générateur non cryptographique pour éviter les problèmes de prédictibilité.

### Autres changements
- Documentation : Clarification du texte du lien de téléchargement des transcriptions audio.
- Correction de bugs mineurs dans l'add-in Outlook (alpha).
- Amélioration de l'optimisation de l'utilisation des sondages PostHog et enrichissement des métadonnées des événements.
- Suppression de commandes obsolètes pour la récupération de secrets externes.
- Mise à jour de la documentation et des exemples pour le nouveau support d'add-ons.
- Correction de problèmes de boucle de reconnexion causés par les mises à jour de `connectionObserverStore`.
- Correction de problèmes d'accès au flag de fonctionnalité d'enregistrement d'écran.
- Correction de typos dans les paramètres des add-ons.
- Mise à jour de la configuration Nginx pour l'interface utilisateur DINUM.
- Mise à jour des images Docker et des fichiers Helm.
- Ajout de tests unitaires pour le service JwtTokenService.
- Suppression d'une dépendance obsolète.
- Mise à jour de la version de release à 1.15.0.
- Publication d'une nouvelle version du chart Helm.
