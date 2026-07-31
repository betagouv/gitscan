## Changelog : buildkit-operator (30 derniers jours, au 29 juillet 2026)

### Résumé
Les dernières mises à jour de buildkit-operator améliorent la gestion des daemons de construction, notamment en introduisant un mécanisme de drainage avant les déploiements, une meilleure gestion des builds en cours et des configurations plus flexibles pour l'environnement cloud. Des améliorations de la sécurité et de la robustesse ont également été apportées.

### Évolutions fonctionnelles
- Possibilité de configurer des sélecteurs de nœuds spécifiques à l'architecture pour les daemons de construction, permettant un contrôle plus précis de leur placement. ([#2](https://github.com/SocialGouv/buildkit-operator/issues/2))
- Configuration des stratégies de cache S3, avec une importation toujours active et une exportation périodique.
- Exposition d'un paramètre `maxBuildSeconds` dans le chart Helm pour limiter la durée maximale d'exécution des builds.
- Amélioration de la gestion des builds en cours pour éviter les problèmes lors des mises à jour et des déploiements.
- Possibilité de configurer des defaults par projet au moment de la création du BuildProject.
- Adaptation du keep-warm pour qu'il s'adapte au rythme des builds.

### Évolutions techniques
- Refactorisation de la gestion des tokens de build pour stocker uniquement leur hash et centraliser la création des identités OIDC.
- Suppression de la compatibilité avec les tokens en clair, privilégiant l'authentification OIDC.
- Amélioration de la gestion des erreurs lors de l'exportation du cache S3 (passage en mode "best-effort").
- Mise à jour des actions GitHub vers Node 24 pour une meilleure sécurité et performance.
- Publication d'images pour l'architecture ARM64 en plus d'AMD64.
- Amélioration de la robustesse du controller et du buildd face à des scénarios d'adversité.
- Mise en place d'un système de drainage des daemons avant leur remplacement lors des déploiements.

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités et configurations.
- Corrections de bugs mineurs et améliorations de la qualité du code.
- Renouvellement de Renovate pour la gestion des dépendances.
- Amélioration de la couverture des tests unitaires.
