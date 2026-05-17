## Changelog : meet (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la qualité des transcriptions et des résumés de réunions, notamment en ajoutant la prise en charge du format WebM et en améliorant l'attribution des locuteurs. Des efforts ont également été déployés pour renforcer la sécurité, notamment en validant la configuration des salles et en corrigeant des vulnérabilités dans les dépendances. Enfin, une première version de support pour l'intégration avec Microsoft Outlook a été introduite en phase alpha.

### Évolutions fonctionnelles
- Ajout de la prise en charge du format WebM pour les transcriptions et les résumés. [#1290]
- Amélioration de l'attribution des locuteurs lors de la transcription, utilisant la détection d'activité vocale (VAD).
- Introduction d'une version alpha du support pour l'intégration avec Microsoft Outlook, permettant l'authentification et l'accès aux fonctionnalités de Meet depuis Outlook. [#1299]
- Clarification du texte du lien de téléchargement de la transcription audio en français. [#1299]
- Configuration de l'encodage des enregistrements LiveKit Egress est maintenant configurable. [#1288]
- Ajout de routes v2 pour les tâches STT et de résumé asynchrones. [#1171]

### Évolutions techniques
- Utilisation de `uv` pour la gestion des dépendances, améliorant la performance et la reproductibilité des builds.
- Validation de la configuration des salles avec un schéma Pydantic pour renforcer la sécurité.
- Refactorisation de la signature des tâches de résumé.
- Amélioration de la gestion des erreurs Twirp pour les opérations sur les participants.
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (urllib3, django, postcss, webpack-dev-server, pytest, aiohttp, vite).
- Amélioration de la gestion des jetons JWT pour l'authentification.
- Ajout de tests unitaires pour le service JwtTokenService.
- Mise à jour de l'outil de build pour prendre en charge la gestion des dépendances basée sur `uv`.
- Ajout de la collecte de métadonnées sur les événements VAD, de connexion et de chat.
- Amélioration de la configuration Nginx pour le frontend DINUM.
- Mise à jour de la documentation et des outils de publication (helm chart).

### Autres changements
- Correction de bugs mineurs dans l'interface utilisateur (espacement, accessibilité, affichage des liens).
- Amélioration de la qualité de l'échelle de notation.
- Correction de problèmes liés à la boucle de reconnexion.
- Correction de problèmes liés à l'accès au contrôle de l'enregistrement d'écran.
- Correction de problèmes liés à la génération des ID de salle.
- Ajout d'un lien vers le fichier "Open" dans l'email de l'enregistrement.
- Amélioration de la journalisation de l'attribution des locuteurs.
- Suppression de certaines dépendances obsolètes.
- Amélioration de la configuration de Docker pour les agents.
- Standardisation de la terminologie des rôles dans les localisations.
