## Changelog : prelevements-deau-api (30 derniers jours)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'API de gestion des prélèvements d'eau, notamment l'ajout de la surveillance des erreurs via Sentry, l'amélioration de la gestion des exploitations liées, et la correction de bugs concernant l'édition du SIRET et le fonctionnement de Bullboard. La stratégie d'authentification a également été modifiée.

### Évolutions fonctionnelles
- Les exploitations liées sont maintenant exposées via l'API (#172).
- Correction d'un bug empêchant l'édition correcte du SIRET dans le formulaire de prélèveur (#171).
- Amélioration du texte des emails envoyés (#172).

### Évolutions techniques
- Intégration de Sentry pour la surveillance des erreurs et la collecte de traces (#168, #169). Cela permettra d'identifier et de corriger plus rapidement les problèmes en production.
- Modification de la stratégie d'authentification (#172).
- Ajout d'une stratégie de reconnexion pour Redis afin d'améliorer la résilience de l'application.
- Correction de l'utilisation du routeur dans Bullboard (#169).
- Initialisation corrigée de S3.
- Ajout d'une variable d'environnement manquante pour S3.
- Correction de tests liés à S3.
- Ajout d'un service manquant.
- Mise à jour du fichier openapi.yml.

### Autres changements
- Améliorations du linting du code.
- Ajout de logs pour faciliter le débogage.
