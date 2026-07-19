## Changelog : dictaphone (30 derniers jours, au 17 juillet 2026)

### Résumé
Cette période a été marquée par une amélioration significative de la robustesse et de la performance de l'application, tant sur le backend que sur les applications mobile. Des corrections ont été apportées pour gérer les erreurs de traitement audio, améliorer la gestion des fichiers et optimiser l'expérience utilisateur, notamment en matière d'upload et de lecture. Plusieurs versions ont été publiées pour les applications mobile et le backend.

### Évolutions fonctionnelles
- Amélioration de la gestion des erreurs lors du traitement audio : l'erreur `no_audio` est désormais considérée comme un succès. [#issue à retrouver]
- Affichage du temps de traitement estimé pour les fichiers en cours de transcription.
- Ajout d'une information sur la durée du traitement dans l'application mobile.
- Possibilité de régler la vitesse de lecture dans l'application web.
- Affichage d'une alerte sur l'application mobile concernant l'optimisation de la batterie.
- Ajout d'une modal pour récupérer les fichiers en cas de problème lors de l'enregistrement sur mobile.
- Amélioration de la gestion des fichiers audio sur mobile, avec une division en segments pour éviter la perte de données.
- Correction de l'affichage des participants dans les transcriptions mobiles.
- Suppression de l'URL de prévisualisation dans l'interface d'administration pour plus de sécurité.
- Amélioration de la robustesse de la sauvegarde des données audio sur le frontend.
- Correction de l'affichage des styles des toasts sur le frontend.
- Amélioration de la gestion des erreurs lors du chargement de fichiers audio corrompus.
- Inclusion de l'adresse email de l'utilisateur dans les requêtes de résumé.

### Évolutions techniques
- Refonte de la gestion des jetons d'accès API pour corriger une vulnérabilité de sécurité. [#issue à retrouver]
- Optimisation des performances d'upload sur Android.
- Amélioration de l'estimation de la capacité de traitement du backend.
- Configuration du système de retry Celery pour une meilleure résilience.
- Mise à jour des dépendances Python et JavaScript.
- Amélioration de la gestion des appels concurrents à l'API React Native Audio.
- Correction de problèmes de concurrence lors du démarrage de l'enregistreur sur mobile.
- Utilisation d'une API React Native Audio mise à jour (v0.13.1).
- Amélioration de la gestion des erreurs et des logs sur le frontend.
- Correction de bugs liés à la persistance des données audio sur le frontend.
- Correction de problèmes de build liés aux tests frontend.

### Autres changements
- Publication des versions v0.11.3, v0.11.2, v0.11.1, v0.11.0 du backend et du frontend.
- Publication des versions v1.5.3, v1.5.2, v1.5.1, v1.5.0 et v1.4.0 de l'application mobile.
- Augmentation de la taille maximale des fichiers en développement local.
- Ajout de logs pour le suivi des erreurs dans les webhooks.
- Enregistrement des erreurs de console par défaut sur le frontend.
- Suppression des logs de développement.
- Mise à jour de la configuration Renovate.
- Amélioration de la documentation.
