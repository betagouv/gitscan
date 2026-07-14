## Changelog : device-management (30 derniers jours, au 14 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des configurations, à la sécurité et à l'observabilité du système. L'introduction de feature flags permet une plus grande flexibilité et un déploiement progressif des nouvelles fonctionnalités. Des améliorations ont également été apportées au dashboard pour une meilleure visualisation de l'adoption et des données d'utilisation.

### Évolutions fonctionnelles
- Ajout d'un toggle sur le dashboard pour basculer entre les vues "Appareils" et "Utilisateurs" pour l'adoption des plugins [#21](https://github.com/IA-Generative/device-management/pull/21).
- Amélioration du dashboard avec des courbes par plugin et des légendes plus cohérentes [#29](https://github.com/IA-Generative/device-management/pull/29).
- Possibilité d'éditer les credentials (Keycloak, relais) et de gérer les surcharges de configuration runtime via une nouvelle page d'administration.
- Ajout d'une page de débogage avec édition inline, diff, reset et rechargement des configurations.
- Implémentation d'un proxy LLM compatible OpenAI avec un endpoint `/llm/v1` et la possibilité de surcharger l'endpoint LLM.
- Redirections automatiques de la racine `/` vers `/catalog/` et de `/admin` vers `/admin/`.
- Amélioration du logout Keycloak pour passer le `client_id` et éviter les erreurs.

### Évolutions techniques
- Implémentation d'un système de feature flags avec catalogue scopé par plugin et réconciliation à l'import [#28](https://github.com/IA-Generative/device-management/pull/28).
- Refonte de la gestion des configurations runtime avec un module cœur dédié et un chiffrement réversible des secrets.
- Amélioration de la sécurité avec l'utilisation d'images non-root pour les conteneurs et l'ajout de gardes-fous.
- Ajout de la vérification de la validité des chemins de fichiers pour renforcer la sécurité.
- Amélioration de la robustesse du système avec l'ajout de verrous consultatifs pour la gestion du schéma de base de données.
- Amélioration de la télémétrie avec la préservation du préfixe de chemin `PUBLIC_BASE_URL`.
- Mise à jour de la version à 0.9.3.
- Amélioration de la gestion des logs avec filtrage des sondes et des requêtes.

### Autres changements
- Documentation de l'embedder RAG et des champs de configuration associés.
- Ajout de tests unitaires et d'intégration pour les nouveaux features.
- Amélioration de la qualité du code avec des corrections de linting et de style.
- Mise à jour des dépendances et des outils de CI/CD.
- Ajout de documentation sur l'architecture et les principes de conception du système (ADR-0002).
- Amélioration de l'observabilité avec l'ajout de métriques et de logs.
- Correction de bugs mineurs et améliorations de la performance.
