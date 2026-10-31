## Changelog : iterion (30 derniers jours, au 31 octobre 2026)

### Résumé
Ce mois a été marqué par un effort massif de sécurisation des environnements d'exécution (sandboxes) et de gestion des secrets. L'expérience utilisateur a été enrichie par l'introduction de commandes "slash" pour l'outil CLI `claw`, une meilleure observabilité via le mode `prod-watch`, et une mise en conformité accrue de l'interface Studio avec les standards d'accessibilité (RGAA/WCAG).

### Évolutions fonctionnelles
- **Outils IA & CLI (`claw`)** : Introduction des "slash commands", permettant d'invoquer des commandes de workspace directement via le modèle d'IA [#1716](https://github.com/SocialGouv/iterion/issues/1716).
- **Interface Studio** :
    - Ajout d'écrans d'administration pour la gestion des rôles de bots, des sandboxes et des identifiants de plateforme [#1443](https://github.com/SocialGouv/iterion/issues/1443).
    - Nouvel éditeur pour la gestion des overrides de credentials dans les webhooks.
    - Améliorations significatives de l'accessibilité (focus visuels, labels de formulaires, gestion des zones de drop) pour respecter les normes RGAA/WCAG [#2556](https://github.com/SocialGouv/iterion/issues/2556).
- **Observabilité & Monitoring** :
    - Lancement de `prod-watch` : système de rapports et d'alertes (digest Mattermost, intégration Grafana/Loki) pour le suivi des sessions [#1701](https://github.com/SocialGouv/iterion/issues/1701).
    - Exposition d'une surface de métriques `/metrics` pour le monitoring système [#2295](https://github.com/SocialGouv/iterion/issues/2295).
- **Routage LLM** : Mise en place d'une politique de routage adaptative permettant de définir des règles au niveau de l'organisation ou de l'équipe [#2217](https://github.com/SocialGouv/iterion/issues/2217).
- **Gestion des connexions** : Support du remplacement de tokens PAT et gestion des connexions par tenant via l'API.

### Évolutions techniques
- **Sécurité & Isolation (Sandbox/Runtime)** :
    - Renforcement de l'isolation des sandboxes : filtrage strict des variables d'environnement, protection contre les fuites de secrets et contrôle des règles réseau.
    - Implémentation du "Secret Guard" pour assurer que les secrets ne sont accessibles qu'aux composants autorisés et avec une traçabilité complète.
    - Sécurisation des processus d'exécution via un système de "Authoring Lock" pour protéger l'intégrité des fichiers modifiés par les agents.
- **Infrastructure & CI/CD** :
    - Intégration de SeaweedFS comme magasin d'objets pour le stack de développement [#1943](https://github.com/SocialGouv/iterion/issues/1943).
    - Optimisation des pipelines CI avec l'ajout de tests E2E Playwright et une meilleure gestion du parallélisme des tests.
    - Amélioration de la résilience de la file d'attente (NATS) et de la gestion des brokers.
- **Architecture** :
    - Refactorisation de la gestion du YAML pour une lecture plus robuste et standardisée.
    - Mise en place d'une gestion fine des quotas par dépôt (repo quota) pour limiter l'usage des ressources.

### Autres changements
- **Documentation** : Mise à jour majeure incluant de nouveaux diagrammes de flux, un schéma de base de données (ERD) zoomable et une documentation enrichie des décisions d'architecture (ADR) [#2579](https://github.com/SocialGouv/iterion/issues/2579).
- **Nettoyage** : Suppression de code obsolète et optimisation des processus de génération d'artefacts.
