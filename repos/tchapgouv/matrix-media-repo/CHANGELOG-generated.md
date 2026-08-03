## Changelog : matrix-media-repo (30 derniers jours, au 21 juillet 2026)

### Résumé
Ce dépôt multimédia Matrix a bénéficié d'améliorations récentes axées sur la limitation du débit (rate limiting) pour une meilleure gestion des ressources et une protection contre les abus. Des corrections ont également été apportées pour améliorer la stabilité et la gestion des erreurs, notamment lors de la génération de miniatures et de la gestion des limites de débit.

### Évolutions fonctionnelles
- Ajout d'un système de "leaky bucket" (seau qui fuit) spécifique à chaque utilisateur pour limiter le débit de téléchargement. [#2](https://github.com/tchapgouv/matrix-media-repo/pull/2)
- Correction de la génération de miniatures et renvoi d'un code d'erreur approprié en cas de dépassement de la limite de débit.
- Correction d'un problème où un revert avait été effectué sur l'ajout d'informations de développement dans la construction Docker.

### Évolutions techniques
- Construction des images Docker uniquement pour l'architecture amd64 afin de réduire la complexité et la taille des images.
- Ajout d'informations de développement dans l'image Docker pour faciliter le débogage.
- Revert d'un commit précédent pour éviter des problèmes potentiels.

### Autres changements
- Aucune documentation ou configuration n'a été modifiée dans cette version.
