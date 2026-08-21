## Changelog : infra-apps (30 derniers jours, au 20/08/2026)

### Résumé
Ce mois-ci a été marqué par une consolidation majeure de l'infrastructure et un renforcement de la sécurité. Les efforts se sont concentrés sur la migration des services de build vers une architecture centralisée (Buildkit-operator), l'amélioration de l'isolation et de l'observabilité du service Iterion, ainsi que la correction de vulnérabilités critiques sur Metabase.

### Évolutions fonctionnelles
- **Token-Bureau** : Amélioration de la gestion des permissions (application des overrides par dépôt) et extension des droits pour la CI egapro [#49](https://github.com/SocialGouv/infra-apps/issues/49).
- **Metabase** : Fiabilisation du processus d'authentification OAuth pour les sessions utilisateurs.
- **Iterion** : Autorisation de l'utilisation de l'OAuth pour les SDK tiers en environnement de production.

### Évolutions techniques
- **Iterion** : 
    - Mise en place de l'observabilité via le traçage et le suivi d'erreurs (Sentry).
    - Déploiement de l'isolation par pods (sandboxing) pour les runners en production (ADR-082).
    - Optimisation de la gestion des ressources et des forfaits [#51](https://github.com/SocialGouv/infra-apps/issues/51).
- **Metabase** : 
    - Correction de vulnérabilités de sécurité critiques (injection SQL non authentifiée et contournement OAuth).
    - Mise à jour de la gestion des certificats SSL.
- **Buildkit-Operator** : 
    - Migration complète des services de build vers l'opérateur et décommissionnement du service buildkit indépendant.
    - Gestion automatisée du cycle de vie du cache S3 et durcissement de la sécurité post-revue.
    - Configuration explicite des spécificités de stockage et de Load Balancing sur OVH.
- **Architecture** : 
    - Migration de la veille (Huginn) vers Iterion.
    - Décommissionnement de plusieurs composants obsolètes (buildkit-service, huginn).

### Autres changements
- **Documentation** : Mise à jour des guides concernant l'utilisation des tokens pour le Buildkit-operator.
- **Nettoyage** : Suppression de fonctionnalités et de configurations obsolètes (IA Metabase, variables de déploiement dépréciées) et optimisation des charts Helm.
