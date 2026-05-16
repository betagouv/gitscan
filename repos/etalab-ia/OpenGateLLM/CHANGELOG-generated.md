## Changelog : OpenGateLLM (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes de fonctionnalités audio, de sécurité et de gestion des documents. Des corrections de bugs et des refactorings ont également été effectués pour améliorer la stabilité et la maintenabilité du code. L'intégration avec Langfuse a été ajoutée pour le suivi de l'utilisation.

### Évolutions fonctionnelles
- **Audio :** Ajout de la prise en charge des formats SRT et VTT pour la transcription audio [#855].
- **Audio :** Prise en charge de la transcription audio diarizée [#832, #859].
- **Langfuse :** Intégration de Langfuse pour le suivi de l'utilisation des modèles [#812].
- **Playground :** Corrections de bugs et améliorations de l'interface utilisateur [#856, #860].
- **Sécurité :** Création d'une image de playground privée pour une sécurité accrue [#835].
- **Documents :** Correction d'un bug qui empêchait la fermeture correcte des fichiers PDF après lecture [#833].

### Évolutions techniques
- **Refactoring :** Refactorisation du code lié à la gestion des rôles pour une architecture plus propre [#817, #821].
- **Modèles :** Amélioration de la configuration des modèles pour un code plus propre [#823].
- **Documentation :** Mise à jour de la documentation et du workflow de déploiement [#836, #837, #838, #840, #862].
- **CI/CD :** Ajout d'un scan Trivy et déploiement de release via GitHub Actions [#857].
- **Elasticsearch :** Réduction du nombre de shards Elasticsearch par défaut pour optimiser les performances [#829].
- **Monitoring :** Correction des URLs dans les métriques Prometheus pour une meilleure lisibilité [#824].
- **Corrections :** Correction de plusieurs bugs mineurs et améliorations de la gestion des erreurs [#826, #827, #828].

### Autres changements
- Renommage de certains fichiers et répertoires pour une meilleure organisation du code [#864, #865].
- Correction de la base URL pour l'intégration avec Langfuse [#868].
- Suppression de préfixes inutiles dans les messages d'erreur [#826].
- Suppression d'imports inutiles dans les modèles [#822].
- Correction d'un problème lié à la longueur maximale du mot de passe dans le playground [#809].
- Correction d'un problème lié au langage par défaut envoyé au modèle Whisper [#819].
