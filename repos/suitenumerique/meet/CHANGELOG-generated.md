## Changelog : meet (30 derniers jours, au 01 mai 2026)

### Résumé
Les dernières mises à jour de Meet se concentrent sur l'ajout de nouvelles fonctionnalités, notamment un support initial pour un add-in Microsoft Outlook, l'amélioration de l'authentification pour les add-ons et la collecte de métadonnées pour l'analyse. Des corrections de bugs et des améliorations de sécurité ont également été apportées, ainsi que des améliorations d'accessibilité.

### Évolutions fonctionnelles
- Ajout d'un support initial pour un add-in Microsoft Outlook (alpha) [#4548f69].
- Possibilité d'activer/désactiver l'échange de jetons d'application via un paramètre de configuration [#012857f].
- Amélioration de l'authentification pour les add-ons [#6f38d60, #ecb7106, #264f267].
- Clarification du texte du lien de téléchargement des transcriptions audio en français [#bb816eb].
- Ajout de la collecte de métadonnées sur l'activité des participants (VAD, connexions, chat) [#8507cdd, #73dd684].

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (Django, aiohttp, vite, pytest, Pillow) [#34f9dea, #d8ccd02, #08aa63e, #4d222e4, #b80c46d].
- Refactorisation de la gestion des erreurs Twirp dans le backend [#3ccb2d4, #6180ac4].
- Utilisation de l'en-tête `Authorization` pour l'authentification avec le jeton LiveKit [#5d7a54e].
- Amélioration des tests unitaires pour le service de jetons JWT [#6b656ee].
- Optimisation de l'utilisation de PostHog et enrichissement des métadonnées des événements [#170763a].
- Mise à jour de l'image frontend vers Alpine 3.23 pour corriger des CVE [#4d222e4].
- Configuration de la sécurité des pods et conteneurs dans le Helm chart [#264f267].
- Mise à jour des images Docker et des fichiers de configuration Helm pour le service de collecte de métadonnées [#73dd684, #3b474ba, #812d80c].
- Alignement du token CSRF avec les conventions Django [#181b97b].

### Autres changements
- Correction de problèmes mineurs dans l'add-in Outlook [#ac2eddc].
- Correction d'un bug de boucle de reconnexion causé par les mises à jour de `connectionObserverStore` [#dd3d47a].
- Correction d'un problème d'accès au contrôle de l'enregistrement d'écran [#35863ec].
- Amélioration de la configuration Nginx pour le frontend DINUM [#da1767c].
- Suppression de commandes obsolètes pour la récupération de secrets externes [#6374e13].
- Correction de l'indentation dans le Makefile [#52fbd56].
- Ajout d'une option pour ignorer Ruff sur l'exécution ffprobe [#c4fc467].
- Mise à jour du chart Helm pour supporter l'add-in Outlook [#6bb8084].
- Mise à jour du chart Helm [#df24aaa, #b80c46d, #6bb8084].
- Améliorations d'accessibilité (titres de documents explicites, navigation dans la barre latérale, étiquettes ARIA) [#f0fda14, #d12ced3, #497b45f].
