## Changelog : francetransfert (30 derniers jours, au 23 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur le renforcement de la sécurité de la plateforme et l'optimisation de l'infrastructure technique. Des ajustements ont également été réalisés pour améliorer la compatibilité et l'expérience utilisateur sur les appareils mobiles (iOS).

### Évolutions fonctionnelles
- Amélioration de la détection et de la compatibilité avec les appareils mobiles (iOS/iPhone).
- Ajustement de la période de grâce lors des processus d'envoi de fichiers (upload grace period).

### Évolutions techniques
- **Sécurité** : Renforcement de la protection via l'implémentation de nouvelles règles de sécurité, la gestion de la liste blanche d'adresses IP (`ipallow`) et l'activation de la passerelle (gateway).
- **Infrastructure** : Optimisation et mise à jour des configurations liées à Redis.
- **Stabilité** : Ajustement des seuils de réussite (`successThreshold`), probablement pour les processus de déploiement ou de santé du système.
