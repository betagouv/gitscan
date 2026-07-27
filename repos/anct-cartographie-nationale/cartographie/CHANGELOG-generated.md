## Changelog : cartographie (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette version apporte des améliorations de la stabilité et de la performance, notamment au niveau de la gestion du cache des lieux. Des corrections ont été apportées à l'affichage des messages d'erreur et à la gestion des toasts. De plus, des optimisations ont été réalisées pour améliorer l'observabilité et le monitoring de l'application.

### Évolutions fonctionnelles
- Correction de l'affichage des toasts pour qu'ils restent visibles au-dessus du backdrop du modal de contact.
- Traduction des codes d'erreur de l'action serveur au lieu d'afficher les erreurs brutes, améliorant l'expérience utilisateur.
- Ajout d'un filtre par source de données pour affiner la recherche de lieux [#a4f4fd0](https://github.com/anct-cartographie-nationale/cartographie/commit/a4f4fd0662c3b76ef8563c42dfb092e52e307a16).

### Évolutions techniques
- Amélioration de la gestion du cache des lieux : partage du store entre les différentes couches du bundle via un singleton `globalThis`.
- Instrumentation du store des lieux pour diagnostiquer les fiches potentiellement obsolètes [#052847a](https://github.com/anct-cartographie-nationale/cartographie/commit/052847a3c47a96a4b40bc93fef7a57426026576d).
- Refactor de l'accès aux variables d'environnement pour utiliser la notation par points.
- Mise à jour des dépendances React Email pour une importation unifiée.
- Mise à jour des actions GitHub (checkout et cache) vers leurs dernières versions.
- Optimisation de la gestion du cache Nginx avec une réduction du TTL à 5 minutes pour une propagation plus rapide des mises à jour.
- Implémentation de la corrélation des logs Nginx et Sentry via un `request_id` pour faciliter le débogage.
- Émission des logs d'accès Nginx au format JSON pour une meilleure intégration avec Grafana.
- Capture des échecs de préchargement du cache au démarrage pour un monitoring plus précis.
- Ajout de logs structurés des requêtes serveur pour une meilleure analyse.
- Gestion des erreurs de chargement du cache : tentative de relance en cas d'échec au lieu de mettre en cache le rejet.

### Autres changements
- Mise à jour de la configuration de Biome pour s'adapter à la version 2.5.
- Mise à jour des dépendances du projet.
