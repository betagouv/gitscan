## Changelog : find (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à find au cours des 30 derniers jours. Les principales évolutions concernent l'ajout de support pour l'architecture ARM64, des corrections de bugs et des ajustements de l'infrastructure CI/CD. Une fonctionnalité de filtrage par chemin de fichier a été implémentée puis temporairement annulée, et est en cours de stabilisation.

### Évolutions fonctionnelles
- Ajout du filtrage sur le chemin des fichiers [#53](https://github.com/suitenumerique/find/issues/53). *Note : cette fonctionnalité a été brièvement déployée puis rétractée pour correction.*
- Amélioration de la compatibilité en ajoutant le support de l'architecture ARM64 pour la construction des images Docker.

### Évolutions techniques
- Mise à jour de Django vers la version 5.2.11, incluant des correctifs de sécurité [#35e308f](https://github.com/suitenumerique/find/commit/35e308f).
- Suppression d'un workflow de déploiement obsolète [#195722b](https://github.com/suitenumerique/find/commit/195722b).
- Mise à jour des actions GitHub pour utiliser les dernières versions [#71744cc](https://github.com/suitenumerique/find/commit/71744cc).

### Autres changements
- Aucun autre changement significatif à signaler.
