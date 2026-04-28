## Changelog : domifa (30 derniers jours, au 27 avril 2026)

### Résumé
Les dernières mises à jour de DomiFa se concentrent sur l'amélioration de la sécurité, la correction de bugs et l'intégration de la nouvelle bibliothèque de composants DSFR pour une interface utilisateur plus moderne et accessible. Des optimisations ont également été apportées pour améliorer la performance et la robustesse de l'application.

### Évolutions fonctionnelles
- Intégration de la bibliothèque de composants DSFR sur le frontend, améliorant l'accessibilité et l'expérience utilisateur.
- Ajout d'un mécanisme de limitation de débit (throttling) pour protéger l'API contre les requêtes abusives.
- Correction de bugs concernant l'édition du numéro SIRET et l'assignation des référents.
- Ajout d'une bannière DSFR sur le frontend.

### Évolutions techniques
- Amélioration de la sécurité en renforçant les règles de validation et en ajoutant des logs pour le suivi des activités.
- Ajout de tests unitaires et correction de tests existants.
- Refonte des DTO (Data Transfer Objects) pour une meilleure cohérence et validation des données.
- Optimisation des performances en désactivant le throttling pour les vérifications de santé (health check).
- Mise en place d'un mécanisme pour éviter les commits déclenchant des CI inutiles.

### Autres changements
- Ajout d'un fichier `claude.md`.
- Amélioration du changelog et correction des liens vers les commits.
- Ajout de logs pour faciliter le débogage.
