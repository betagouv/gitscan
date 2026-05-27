## Changelog : meet (30 derniers jours, au 26 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment l'introduction d'une fonctionnalité "image dans l'image" (PiP) pour les réunions, des améliorations de l'accessibilité (notamment pour les réactions et les polices d'écran), et des avancées dans la gestion des autorisations et de la configuration des salles de réunion. Des efforts ont également été déployés pour améliorer la sécurité et la robustesse de la plateforme, ainsi que pour préparer l'intégration d'un add-in Microsoft Outlook.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité "image dans l'image" (PiP) pour les réunions, incluant une barre de contrôle, un indicateur d'état de connexion et un menu d'options.
- Amélioration de l'accessibilité de la barre d'outils de réactions, notamment pour la navigation au clavier et sur les appareils mobiles.
- Possibilité de configurer les salles de réunion pour autoriser tous les participants à se mettre en sourdine mutuellement.
- Ajout d'un synchroniseur pour les mises à jour de la configuration des salles de réunion.
- Amélioration de l'assignation des intervenants pour la transcription automatique.
- Ajout d'un sélecteur de police dans les paramètres d'accessibilité pour personnaliser la taille et le style du texte.
- Clarification du texte du lien de téléchargement de la transcription audio en français.

### Évolutions techniques
- Refactorisation de composants frontend (strip, réaction toolbar) pour une meilleure clarté et maintenabilité.
- Mise à jour de la gestion des dépendances avec l'utilisation de `uv` pour une meilleure performance et sécurité.
- Amélioration de la gestion des erreurs et de la robustesse du processus d'enregistrement des réunions.
- Refactorisation du code backend pour simplifier la sérialisation des sources et améliorer la gestion de l'identité de l'appelant.
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité et améliorer la stabilité (Django, webpack-dev-server, pytest, postcss, urllib3).
- Amélioration de la configuration Nginx pour le frontend DINUM.
- Ajout de tests unitaires pour le service de jetons JWT.
- Mise en place d'un mécanisme de synchronisation pour les mises à jour de la configuration des salles de réunion.

### Autres changements
- Mise à jour de la documentation et du changelog.
- Corrections mineures de l'interface utilisateur et de la mise en page.
- Préparation de l'intégration d'un add-in Microsoft Outlook (alpha).
- Amélioration des logs pour le suivi de l'assignation des intervenants.
- Correction de bugs mineurs liés à la position des tooltips et au recentrage de la barre de réactions.
- Suppression des exigences de `requirements.txt` au profit de `uv.lock`.
- Correction d'un bug empêchant le téléchargement des transcriptions audio.
- Ajout de contextes de sécurité aux pods et conteneurs Helm.
- Amélioration de la gestion des CSRF tokens.
- Ajout de routes V2 pour la transcription asynchrone et les tâches de résumé.
