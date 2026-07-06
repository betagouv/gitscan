## Changelog : device-management (30 derniers jours, au 05 juillet 2026)

### Résumé
Ce mois-ci, le projet a connu une évolution majeure avec l'introduction de la gestion des configurations runtime, permettant une personnalisation et une adaptation plus fines du système. Des améliorations significatives ont également été apportées à la sécurité, à l'observabilité et à la gestion des dépendances. L'interface d'administration a été enrichie avec de nouvelles fonctionnalités de débogage et de configuration.

### Évolutions fonctionnelles
- Ajout de la possibilité de rediriger les accès racine (`/`) vers le catalogue (`/catalog/`) et l'administration (`/admin/`) pour une meilleure compatibilité avec les proxys inversés. [#21](https://github.com/IA-Generative/device-management/pull/21)
- L'interface d'administration permet désormais d'éditer les informations d'identification (Keycloak, relais) et d'importer des surcharges de configuration au démarrage. [#20](https://github.com/IA-Generative/device-management/pull/20)
- Ajout d'une page de débogage dans l'interface d'administration permettant l'édition, la comparaison, la réinitialisation et le rechargement de la configuration. [#17](https://github.com/IA-Generative/device-management/pull/17)
- Implémentation d'un système de "reaper" pour la suppression automatique des pods Kubernetes obsolètes et d'un heartbeat résilient.
- Intégration de l'observabilité avec Tempo et Grafana, avec authentification SSO Keycloak.
- Ajout d'un script de test pour valider les clés API Scaleway (LLM).
- Amélioration de la gestion des déconnexions Keycloak dans l'interface d'administration.

### Évolutions techniques
- Introduction d'un module de gestion de configuration runtime avec registre, résolution, rechargement et génération de configuration.
- Implémentation du chiffrement réversible Fernet pour les secrets de surcharge runtime.
- Refonte de la validation des chemins de fichiers pour une sécurité accrue.
- Mise à jour des images Docker pour inclure nginx 1.29-alpine (correction d'une vulnérabilité openssl) et les dernières versions des dépendances Python.
- Amélioration de la robustesse des tests CI/CD et correction de problèmes liés à l'environnement d'exécution.
- Suppression de dépendances obsolètes (Adminer, filebrowser) et renforcement de la sécurité des images Docker.
- Utilisation de Ruff pour le linting et Bandit pour l'analyse de sécurité, avec correction des problèmes détectés.
- Amélioration de la gestion des logs avec filtrage des sondes et des accès Nginx.

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités et les changements de configuration.
- Amélioration du quickstart Docker local.
- Suppression des fichiers de sécurité du dépôt.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajustement du port hôte du DM en développement local pour éviter les conflits.
- Suppression du relais `/llm` devenu inutile.
