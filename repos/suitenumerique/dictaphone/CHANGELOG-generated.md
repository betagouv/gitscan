## Changelog : dictaphone (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la stabilité et à la performance de l'application, tant sur le backend que sur les applications mobile. Des corrections de bugs ont été implémentées pour améliorer l'expérience utilisateur, notamment en matière de gestion des fichiers audio et de l'estimation du temps de traitement. L'authentification API a été sécurisée.

### Évolutions fonctionnelles
- Amélioration de la robustesse de la sauvegarde des données audio sur le frontend. [#issue à retrouver]
- Ajout d'une estimation de la durée de traitement des fichiers audio, visible sur le frontend. [#issue à retrouver]
- Possibilité de modifier la vitesse de lecture des fichiers audio sur le frontend. [#issue à retrouver]
- Sur mobile, ajout d'une modale pour récupérer les fichiers audio en cas de problème lors de l'enregistrement.
- Sur mobile, implémentation d'un système de découpage des fichiers pour éviter la perte de données.
- Sur mobile, affichage de la durée de traitement des fichiers.
- Sur mobile, ajout d'une alerte informant l'utilisateur de l'impact potentiel de l'optimisation de la batterie sur l'application.
- Correction d'un bug qui empêchait l'affichage correct des participants dans les transcriptions sur mobile.
- Amélioration de la gestion des erreurs lors de la lecture de fichiers audio corrompus sur le frontend.
- L'email de l'utilisateur est maintenant inclus dans les requêtes de résumé.

### Évolutions techniques
- Sécurisation de l'authentification API : rejet des tokens d'accès utilisateur incorrects. [#issue à retrouver]
- Refonte de la gestion des erreurs et des retries pour les tâches Celery sur le backend.
- Amélioration des performances de l'upload audio sur mobile.
- Mise à jour de la librairie React Native Audio API sur mobile (v0.13.1).
- Amélioration de l'estimation de la capacité de traitement du backend.
- Mise à jour des dépendances Python et JavaScript.
- Amélioration de la robustesse de la gestion des fichiers audio sur mobile, notamment en cas de conditions de course.
- Correction de plusieurs bugs et améliorations de la stabilité sur mobile et frontend.

### Autres changements
- Mise à jour de la documentation.
- Nettoyage du code et suppression des logs de développement.
- Correction de problèmes de style sur le frontend.
- Mise à jour des dépendances du projet.
