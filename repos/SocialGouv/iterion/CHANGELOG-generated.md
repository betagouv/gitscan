## Changelog : iterion (30 derniers jours, au 25 octobre 2026)

### Résumé
Ce mois a été marqué par une consolidation majeure de la plateforme, avec un accent particulier sur la sécurité des environnements d'exécution et l'accessibilité de l'interface. Iterion renforce sa capacité à orchestrer des agents de manière isolée et contrôlée grâce à un sandboxing plus strict et une gestion fine des budgets de consommation (tokens). L'expérience utilisateur est également améliorée avec une interface Studio plus accessible et de nouveaux outils de surveillance de production pour garantir la stabilité des workflows.

### Évolutions fonctionnelles
- **Interface Studio & Accessibilité** : Amélioration significative de l'accessibilité (normes WCAG) incluant la gestion du focus clavier, les rôles d'icônes et les régions de texte en direct [#2638, #2622, #2556, #2527]. Ajout de nouveaux écrans d'administration pour la gestion des rôles, de la sandbox et des identifiants de plateforme [#1443, #1461].
- **Nouveaux outils d'agents (Bots)** : 
    - Introduction de **GitOps-warden** pour automatiser et sécuriser les processus de fusion (merge gates) [#2480, #2389].
    - Déploiement de **Argus (prod-watch)** pour une surveillance proactive de la production via Grafana et Loki [#2138, #1869].
    - Amélioration de l'audit d'accessibilité via le bot **Acci** [#2387].
- **Rédaction de workflows (DSL)** : Amélioration de la clarté des erreurs lors de la rédaction de fichiers YAML, avec des messages d'erreur plus explicites indiquant la cause exacte des échecs de validation [#2405, #2604].

### Évolutions techniques
- **Sécurité et Isolation** : 
    - Renforcement du sandboxing pour empêcher les agents d'accéder aux variables d'environnement ou aux fichiers sensibles de l'hôte [#2310, #2321, #2063].
    - Sécurisation des secrets et des credentials par tenant et par pool, limitant l'accès aux ressources strictement nécessaires [#2671, #2236].
- **Gestion des ressources et Budgets** : Mise en place de mécanismes de contrôle des coûts permettant de définir des plafonds de consommation de tokens et de mettre en pause automatiquement les exécutions en cas de dépassement [#2263, #2028].
- **Infrastructure et Observabilité** : 
    - Exposition de nouvelles métriques via un endpoint `/metrics` pour une intégration native avec Prometheus [#9174dd9].
    - Intégration de **SeaweedFS** comme système de stockage d'objets pour la stack de développement [#1943].
    - Optimisation de la CI/CD avec l'ajout de tests de bout en bout (E2E) via Playwright et un meilleur partitionnement des tests par shards [#9c0d139c, #2213].
- **Routage et Cloud** : Introduction de politiques de routage adaptatives au niveau de l'organisation et de l'équipe pour la sélection des modèles LLM [#2217, #2126]. Mise en place de "Sovereign Runner Pools" pour une isolation physique des ressources de calcul [#2273].

### Autres changements
- **Documentation** : Refonte de la documentation technique incluant de nouveaux diagrammes de flux de fonctionnalités et un schéma complet du modèle de données (ERD) en format SVG zoomable [#2582, #2561, #2545].
- **Nettoyage** : Suppression de plusieurs composants et fonctions obsolètes (legacy) pour simplifier le code source.
