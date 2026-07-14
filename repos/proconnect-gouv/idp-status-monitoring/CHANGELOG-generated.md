## Changelog : idp-status-monitoring (30 derniers jours, au 4 juillet 2026)

### Résumé
Ce mois-ci, les mises à jour se concentrent principalement sur la maintenance et la correction de bugs. Une correction importante a été apportée au producteur pour éviter des problèmes de communication entre les différentes instances de l'application. De plus, les dépendances ont été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Correction d'un bug dans le producteur qui causait un "vol" de réponses entre les différentes instances concurrentes. [#123](https://github.com/proconnect-gouv/idp-status-monitoring/issues/123)

### Évolutions techniques
- Mise à jour des actions Docker utilisées pour le build et le push des images.
- Mise à jour de l'action Docker pour la gestion de Docker Compose.
- Mise à jour de l'action Docker pour la configuration de Buildx.
- Mise à jour de l'action Docker pour la gestion des métadonnées.

### Autres changements
- Mise à jour de Prettier (outil de formatage de code) vers la version 3.9.4.
- Mise à jour de la bibliothèque `uuid` vers la version 14.0.1.
- Mise à jour de la bibliothèque `hono` vers les versions 4.12.26 et 4.12.27.
- Mise à jour de l'action `actions/checkout`.
