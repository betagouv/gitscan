## Changelog : prelevements-deau-api (30 derniers jours)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'API de gestion des prélèvements d'eau. Les principales évolutions concernent l'ajout d'une intégration Sentry pour une meilleure surveillance des erreurs, l'amélioration de l'édition des informations sur les préleveurs, et l'exposition d'informations supplémentaires sur les exploitations liées aux prélèvements. De plus, la stratégie d'authentification a été modifiée.

### Évolutions fonctionnelles
- Amélioration de l'édition du SIRET dans le formulaire de préleveur (#171)
- Exposition des exploitations liées aux prélèvements (#172)
- Modification de la stratégie d'authentification (#172)
- Amélioration du texte des emails envoyés (#172)

### Évolutions techniques
- Intégration de Sentry pour la surveillance des erreurs et la collecte de traces (#168, #169)
- Ajout d'une stratégie de reconnexion pour Redis afin d'améliorer la résilience de l'application.
- Correction de l'initialisation de S3 et ajout de la variable d'environnement manquante pour sa configuration.
- Correction du routage de Bullboard (#169)
- Mise à jour de la documentation OpenAPI (openapi.yml)

### Autres changements
- Amélioration du linting du code.
- Corrections de tests unitaires et d'intégration.
- Ajout de logs pour faciliter le débogage et le suivi des performances.
