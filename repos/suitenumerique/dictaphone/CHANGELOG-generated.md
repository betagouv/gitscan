## Changelog : dictaphone (30 derniers jours, au 7 juillet 2026)

### Résumé
Les dernières mises à jour de dictaphone apportent des améliorations significatives à la robustesse et à la performance, notamment sur l'application mobile. Des corrections de bugs ont été implémentées pour améliorer la stabilité de l'enregistrement et du traitement des fichiers audio. De nouvelles fonctionnalités ont été ajoutées pour faciliter la gestion des données et la conformité aux politiques de confidentialité.

### Évolutions fonctionnelles
- Amélioration de l'expérience utilisateur mobile : affichage des participants, gestion des erreurs d'enregistrement et récupération de fichiers en cas de problème.
- Ajout d'une sélection anticipée de la langue de transcription sur mobile et web.
- Affichage de l'estimation de la durée de traitement de la transcription.
- Affichage de l'état de la transcription sous forme de badge sur l'interface web.
- Information sur la politique de confidentialité des données accessible directement depuis l'interface.
- Possibilité de régler la vitesse de lecture des transcriptions.
- Amélioration de l'interface pour la sélection de la source audio.
- Ajout d'une alerte informant l'utilisateur de l'enregistrement en cours depuis l'application mobile sur le web.

### Évolutions techniques
- Correction d'un problème d'authentification API qui exposait l'application à un mode d'authentification non désiré.
- Amélioration de la gestion des erreurs et de la robustesse du code frontend, notamment lors de la sauvegarde des données d'enregistrement.
- Refonte de la gestion des fichiers audio sur mobile pour éviter la perte de données.
- Optimisation des performances de l'upload audio sur Android.
- Amélioration de l'estimation du temps de traitement des transcriptions.
- Mise à jour des dépendances (Django, React Native, etc.).
- Amélioration de la gestion des jobs Celery avec une configuration de nouvelle tentative automatique.
- Utilisation de Node 24 pour le frontend.
- Ajout de jobs cron pour la suppression des fichiers originaux et la suppression définitive des fichiers.

### Autres changements
- Correction de problèmes de style sur l'interface utilisateur (toaster, etc.).
- Suppression de logs de développement inutiles.
- Mise à jour de la documentation.
- Correction de vulnérabilités Dockerfile identifiées par Snyk.
- Amélioration des tests pour éviter les erreurs de build.
- Mise à jour des mocks pour les tests mobiles.
