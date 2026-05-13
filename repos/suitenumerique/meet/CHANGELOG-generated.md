## Changelog : meet (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la transcription des réunions, notamment en ajoutant la prise en charge de nouveaux formats de fichiers et en optimisant l'attribution des intervenants. Des améliorations significatives ont également été apportées à l'accessibilité de l'application, avec l'ajout d'options de personnalisation des polices. Enfin, les premières étapes de l'intégration d'un add-in pour Microsoft Outlook ont été réalisées.

### Évolutions fonctionnelles
- Ajout de la prise en charge du format WebM pour les transcriptions et enregistrements.
- Amélioration de l'attribution des intervenants lors de la transcription des réunions.
- Ajout d'options de personnalisation des polices pour améliorer l'accessibilité.
- Intégration initiale (alpha) d'un add-in pour Microsoft Outlook, permettant d'intégrer Meet directement dans l'environnement Outlook.
- Possibilité de configurer l'encodage utilisé pour les enregistrements LiveKit Egress.
- Ajout d'un lien direct vers l'enregistrement dans l'email de notification.
- Amélioration de la clarté du texte du lien vers le fichier audio de transcription en français.

### Évolutions techniques
- Refactorisation de la signature des tâches de transcription pour une meilleure gestion asynchrone.
- Utilisation de `uv` pour la gestion des dépendances des agents, améliorant la performance et la fiabilité.
- Validation de la configuration des salles de réunion avec un schéma Pydantic pour garantir la cohérence.
- Mise à jour des dépendances pour corriger des failles de sécurité (urllib3, django, postcss, webpack-dev-server, pytest).
- Amélioration de la gestion des erreurs Twirp pour les opérations sur les participants.
- Mise à jour de l'image frontend vers Alpine 3.23 pour corriger des vulnérabilités.
- Mise en place d'un mécanisme de contrôle via feature flag pour le lancement des agents de collecte de métadonnées.
- Standardisation de la terminologie des rôles dans les différentes langues.
- Amélioration de la gestion des jetons d'authentification LiveKit.
- Ajout de tests unitaires pour le service de jetons JWT.
- Amélioration de la configuration Nginx pour le frontend DINUM.
- Ajout de métriques de suivi des candidats WebRTC dans PostHog.
- Amélioration de la gestion des builds avec l'épinglage de l'image Docker.

### Autres changements
- Documentation mise à jour.
- Corrections mineures de l'interface utilisateur et du code.
- Amélioration de la gestion des builds et des releases.
- Ajout de règles d'ignore pour ruff dans le code de transcription.
- Mise à jour de la version de la chart Helm.
- Correction de l'indentation dans le Makefile.
