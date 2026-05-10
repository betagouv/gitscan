## Changelog : meet (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'accessibilité, la sécurité et l'ajout de nouvelles fonctionnalités comme le support initial d'un add-in Microsoft Outlook et l'amélioration de la collecte de métadonnées pour l'analyse. Des corrections de bugs et des mises à jour de dépendances ont également été apportées pour améliorer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un sélecteur de police dans les paramètres d'accessibilité pour personnaliser la taille et le type de police. [#1270](https://github.com/suitenumerique/meet/issues/1270)
- Support initial d'un add-in Microsoft Outlook (en version alpha) pour intégrer Meet à l'environnement de messagerie. [#1265](https://github.com/suitenumerique/meet/issues/1265)
- Amélioration de la clarté du texte du lien de téléchargement des transcriptions audio en français. [#1299](https://github.com/suitenumerique/meet/issues/1299)
- Possibilité de configurer l'encodage des enregistrements LiveKit Egress. [#1288](https://github.com/suitenumerique/meet/issues/1288)
- Ajout de la prise en charge de formats de fichiers supplémentaires. [#1265](https://github.com/suitenumerique/meet/issues/1265)

### Évolutions techniques
- Refactorisation de la signature des tâches pour améliorer la gestion des fuseaux horaires.
- Validation de la configuration des salles avec un schéma Pydantic pour garantir la cohérence.
- Amélioration de l'atomicité et de la tolérance aux pannes lors du démarrage de l'enregistrement.
- Mise à jour de l'outil de publication pour supporter la gestion des dépendances basées sur uv.
- Ajout de la collecte de métadonnées sur les événements VAD, de connexion et de chat pour une meilleure analyse.
- Amélioration de la gestion des erreurs Twirp pour les opérations sur les participants.
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (PostCSS, Webpack-dev-server, Pytest, aiohttp, vite, django, Pillow).
- Amélioration de la configuration Nginx pour le frontend DINUM.
- Standardisation de la terminologie des rôles dans les localisations.
- Mise à jour des images Docker pour corriger des CVEs.

### Autres changements
- Documentation améliorée et corrections mineures dans le code.
- Correction de bugs mineurs dans l'add-in Outlook en phase alpha.
- Mise à jour de la version de la chart Helm pour le support de l'add-in Outlook.
- Correction d'un bug de boucle de reconnexion causée par les mises à jour de connectionObserverStore.
- Correction d'un problème de génération d'IDs de salles non cryptographiques.
- Amélioration de l'échelle de notation de la qualité audio.
- Ajout de suivi des candidats WebRTC dans les événements PostHog.
- Ajout d'un mécanisme de contrôle via un flag de fonctionnalité pour le lancement de l'agent de collecte de métadonnées.
- Mise à jour de la version de django-lasuite.
- Correction d'indentation dans le Makefile.
