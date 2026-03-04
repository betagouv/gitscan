## Changelog : find (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à find au cours des 30 derniers jours. Les principales évolutions concernent l'ajout de support pour l'architecture ARM64, des corrections de bugs et des améliorations de l'infrastructure CI/CD. Une fonctionnalité de filtrage par chemin de fichier a été introduite puis temporairement annulée, et est maintenant de nouveau disponible.

### Évolutions fonctionnelles
- Ajout d'un filtre sur le chemin des fichiers pour affiner les recherches. [#53](https://github.com/suitenumerique/find/issues/53)
- Prise en charge de l'architecture ARM64 pour les images Docker, permettant une plus grande compatibilité avec différents environnements.

### Évolutions techniques
- Mise à jour de Django vers la version 5.2.11, incluant des correctifs de sécurité.
- Amélioration de l'infrastructure CI/CD avec la mise à jour des actions GitHub vers leurs dernières versions.
- Suppression d'un workflow de déploiement inutilisé.
- Ajout du support pour la construction d'images Docker pour l'architecture ARM64.

### Autres changements
- Correction d'une réversion temporaire de l'implémentation du filtre de chemin, qui est maintenant de nouveau activée.
