## Changelog : iterion (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois a été marqué par une montée en puissance de l'infrastructure "Souveraine" et de l'intelligence du routage. Iterion renforce son contrôle sur l'orchestration d'agents avec l'introduction de politiques de routage adaptatif (Adaptive Routing) et une isolation accrue des ressources via des pools de runners dédiés. L'expérience utilisateur a également été nettement améliorée, notamment grâce à une refonte de l'accessibilité du Studio et une meilleure visibilité sur les livrables des workflows.

### Évolutions fonctionnelles

**Interface Studio & Expérience Utilisateur**
- **Visibilité des livrables :** Les résultats des runs (rendus Markdown) sont désormais consultables directement dans le résumé du run et via le tiroir "Artifacts" [#2700].
- **Accessibilité (WCAG) :** Améliorations majeures pour l'accessibilité, incluant la visibilité du focus clavier, le nommage correct des contrôles de formulaire et une meilleure gestion des contrastes [#2622, #2638, #2556].
- **Navigation :** Introduction d'une nouvelle structure de navigation pour les bots (spine à 6 verbes) pour faciliter l'exploration du catalogue [#1520].

**Intelligence & Routage LLM**
- **Routage Adaptatif :** Mise en place de politiques de routage complexes permettant des règles spécifiques par organisation, équipe ou run, incluant des listes d'autorisation de fournisseurs (allowlists) [#2217, #2210, #2159].
- **Nouveaux Modèles :** Support natif des derniers modèles (Opus 5.5, GPT-6) et intégration de Kimi comme fournisseur de premier rang [#1835, #1744].
- **Gestion des passerelles :** Les passerelles compatibles OpenAI peuvent désormais être gérées comme des enregistrements de credentials sécurisés [#2671].

**Automatisation & Audit**
- **Audit RGAA :** Ajout d'une commande permettant de générer automatiquement des rapports d'audit d'accessibilité RGAA [#2593].
- **Gestion des budgets :** Possibilité de réserver de la capacité pour des charges de travail spécifiques [#1099] et mise en pause automatique des exécutions en cas de dépassement de plafond [#2263].
- **GitOps :** Amélioration des outils "GitOps-warden" pour la gestion des merges et des verdicts, avec support du français [#2389, #2235].

### Évolutions techniques

**Infrastructure Souveraine & Sécurité**
- **Isolation des Runners :** Déploiement de "Sovereign Runner Pools", permettant d'isoler chaque pool dans son propre déploiement de runner avec une identité propre [#2273, #2182].
- **Sécurité des Secrets :** Renforcement de la liaison entre les bundles de run, les tenants, les pools et les identifiants de clés pour garantir une isolation stricte [#2225].
- **Stockage :** Intégration de SeaweedFS comme magasin d'objets pour l'environnement de développement [#1943].

**Observabilité & Monitoring**
- **Système Prod-watch (Argus) :** Déploiement d'un monitoring déterministe sans recours aux LLM, avec des canaux de surveillance dédiés pour Sentry, Loki et Grafana [#1869, #1702, #2057, #2138].

**Core & DSL**
- **Refonte du DSL :** Amélioration massive de l'outil d'auteur (YAML twin) pour la validation, le formatage et la conversion des documents de configuration [#1720, #1664].
- **Optimisation du Runtime :** Correction de la gestion des unités de consommation (usage park) et de la synchronisation des réplicas lors des opérations de nettoyage (sweeps) [#2708, #2686].

### Autres changements

**Documentation**
- **Diagrammes techniques :** Ajout de diagrammes ERD (modèle de données) interactifs et zoomables en SVG pour une meilleure compréhension de la base de données [#2582, #2545].
- **Cartographie :** Mise à jour de la documentation des agents et de la structure des domaines [#2106, #2561].

**CI/CD & Tests**
- **Fiabilité des tests :** Optimisation des pipelines de tests par un partitionnement déterministe des shards et réduction des tests non déterministes (deflaking) [#2203, #2144, #2156].
- **Maintenance :** Automatisation de la mise à jour quotidienne du dépôt Homebrew (tap) [#2308].
