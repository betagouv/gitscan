## Changelog : dictaphone (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la robustesse et à la performance de l'application, tant sur le web que sur mobile. Des corrections de bugs ont été implémentées pour améliorer la stabilité de l'enregistrement et du traitement audio, notamment sur Android. De nouvelles fonctionnalités, comme l'estimation du temps de traitement et le contrôle de la vitesse de lecture, améliorent l'expérience utilisateur. La sécurité a également été renforcée avec une correction concernant l'authentification API.

### Évolutions fonctionnelles
- Ajout d'une estimation du temps de traitement des fichiers audio sur l'interface web.
- Implémentation d'un bouton de contrôle de la vitesse de lecture sur l'interface web.
- Affichage de la durée de traitement sur mobile.
- Amélioration de la gestion des fichiers audio corrompus sur le frontend.
- Ajout d'une alerte informative sur mobile concernant l'optimisation de la batterie.
- Possibilité de récupérer des fichiers audio perdus lors de l'enregistrement sur mobile.
- Affichage du nom du participant dans les transcriptions sur mobile.

### Évolutions techniques
- Refonte de la gestion des erreurs lors de la sauvegarde des chunks audio sur le frontend pour une meilleure robustesse.
- Correction d'un problème d'authentification API qui exposait l'API à un mode d'authentification non désiré [#5c635f6](https://github.com/suitenumerique/dictaphone/commit/5c635f6).
- Amélioration des performances d'upload audio sur Android.
- Configuration du système de retry Celery pour une meilleure résilience du backend.
- Amélioration de l'estimation du throughput et de la capacité de traitement sur le backend.
- Mise à jour de la librairie React Native Audio API sur mobile (version 0.13.1).
- Optimisation de la gestion des fichiers audio sur mobile pour éviter les pertes de données.
- Amélioration de la gestion des appels concurrents à l'API React Native Audio sur mobile.

### Autres changements
- Mise à jour des dépendances Python et JavaScript.
- Amélioration de la documentation et du code.
- Correction de problèmes de style sur le frontend.
- Suppression de logs de développement inutiles sur le frontend.
