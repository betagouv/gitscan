## Changelog : iterion (30 derniers jours, au 2026-11-20)

### Résumé
Ce mois a été marqué par une expansion majeure des capacités d'intégration et un renforcement drastique de la sécurité. Le projet a introduit de nouveaux modes de connexion (connecteurs) et enrichi l'interface Studio pour faciliter la création d'agents. Parallèlement, un travail de fond important a été réalisé sur l'isolation des exécutions (sandboxing) et la documentation des choix architecturaux pour garantir une plateforme robuste et sécurisée.

### Évolutions fonctionnelles
- **Connecteurs et Intégrations** : Introduction de nouveaux mécanismes de "polling" (RSS, Jira JQL) permettant de déclencher des workflows basés sur des flux de données externes ([#3396](https://github.com/SocialGouv/iterion/issues/3396), [#3369](https://github.com/SocialGouv/iterion/issues/3369)).
- **Interface Studio** : Amélioration de l'expérience d'édition avec l'affichage des sources des bots, de nouveaux formulaires de lancement incluant la gestion des modes de code (codemode), et une meilleure gestion visuelle des connexions ([#3397](https://github.com/SocialGouv/iterion/issues/3397), [#3346](https://github.com/SocialGouv/iterion/issues/3346), [#3348](https://github.com/SocialGouv/iterion/issues/3348)).
- **Revue et Collaboration** : Optimisation du processus de revue de code par les agents (Revi) et amélioration de la fluidité des conversations ([#3352](https://github.com/SocialGouv/iterion/issues/3352), [#3344](https://github.com/SocialGouv/iterion/issues/3344)).
- **Gestion des accès** : Mise en place de pools de clés API configurables et d'une gestion plus fine des crédentials par scope ([#3367](https://github.com/SocialGouv/iterion/issues/3367), [#3317](https://github.com/SocialGouv/iterion/issues/3317)).
- **Fiabilité des Bots** : Amélioration de la fiabilité du bot de vérification Vetty et introduction de modes de surveillance de production (prod-watch) ([#3328](https://github.com/SocialGouv/iterion/issues/3328), [#1701](https://github.com/SocialGouv/iterion/issues/1701)).

### Évolutions techniques
- **Sécurité et Isolation** : Renforcement massif du sandboxing pour les exécutions non approuvées, incluant le contrôle strict des variables d'environnement, la limitation des accès réseau (protection SSRF) et l'utilisation de gVisor ([#3371](https://github.com/SocialGouv/iterion/issues/3371), [#2848](https://github.com/SocialGouv/iterion/issues/2848), [#3189](https://github.com/SocialGouv/iterion/issues/3189)).
- **DSL et Runtime** : Évolution du langage de définition (DSL) pour intégrer des capacités de ressources plus précises et une gestion optimisée des limites de mémoire (scripthost) ([#3301](https://github.com/SocialGouv/iterion/issues/3301), [#3383](https://github.com/SocialGouv/iterion/issues/3383)).
- **Refactoring majeur** : Restructuration profonde du module `claw` pour une meilleure intégration au cœur du système ([#3248](https://github.com/SocialGouv/iterion/issues/3248)).
- **CI/CD et Tests** : Optimisation des pipelines de tests via le partitionnement (sharding) et ajustement des budgets de ressources pour les tests de conformité MongoDB ([#3402](https://github.com/SocialGouv/iterion/issues/3402), [#3390](https://github.com/SocialGouv/iterion/issues/3390)).

### Autres changements
- **Documentation** : Mise à jour massive de la documentation technique et publication de nombreuses décisions d'architecture (ADR) pour clarifier les choix de conception (Secret Boundary, Connectors, etc.).
- **Maintenance** : Régénération régulière des inventaires API et des cartes de dépendances du dépôt.
