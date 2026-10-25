## Changelog : starter-kit-opencode (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois-ci, le kit a franchi une étape majeure avec l'intégration de Claude Code via une marketplace de plugins, permettant d'utiliser les agents et les commandes du kit directement dans l'outil. Les processus de déploiement sur Cloud Pi Native (CPin) ont été considérablement renforcés par l'ajout d'un mode console, de mécanismes de sécurité pour la production et d'outils de diagnostic automatisés pour faciliter la résolution d'incidents.

### Évolutions fonctionnelles
- **Intégration Claude Code** : Installation du kit via une marketplace de plugins et mise à disposition d'agents, de commandes et de garde-fous spécifiques au sein de l'interface Claude Code. [#55](https://github.com/dnum-mi/starter-kit-opencode/issues/55)
- **Console CPin améliorée** : Introduction d'un mode de création via console, support des plateformes cibles (Scaleway/RIE) et mise en place d'un système d'avertissement et d'accord explicite avant tout déploiement en production. [#48](https://github.com/dnum-mi/starter-kit-opencode/issues/48) [#53](https://github.com/dnum-mi/starter-kit-opencode/issues/53)
- **Diagnostic et Santé du système** : Ajout de la commande `make doctor` pour vérifier les prérequis et création d'un outil de debug automatisé (via Playwright) pour tester les services CPin (ArgoCD, Harbor, GitLab, Console). [#43](https://github.com/dnum-mi/starter-kit-opencode/issues/43)
- **Automatisation des déploiements** : Automatisation de la première phase du runbook CPin via l'API de la console.

### Évolutions techniques
- **Sécurité et Gestion des secrets** : Centralisation des secrets dans `.cpin/.env.secrets`, masquage systématique des jetons (tokens) dans les sorties de la console et implémentation d'une API Vault pour sécuriser l'alimentation des données. [#44](https://github.com/dnum-mi/starter-kit-opencode/issues/44)
- **Refonte de la configuration** : Simplification de la gestion des URLs de service en utilisant `.cpin/instance.env` comme source de vérité unique pour l'orchestrateur et la console. [#58](https://github.com/dnum-mi/starter-kit-opencode/issues/58)
- **Fiabilité de l'orchestration** : Amélioration de la visibilité des phases de l'agent (via `todowrite`) et renforcement des règles de validation, notamment sur les chemins d'images. [#29](https://github.com/dnum-mi/starter-kit-opencode/issues/29)
- **Gestion des accès** : Unification de l'utilisation du jeton GitHub (GH_PAT) pour la console et les workflows.

### Autres changements
- **Documentation massive** : Mise à jour complète du README, des runbooks de déploiement, des spécifications de debug et des guides sur la gestion des jetons fine-grained. [#23](https://github.com/dnum-mi/starter-kit-opencode/issues/23) [#36](https://github.com/dnum-mi/starter-kit-opencode/issues/36)
- **Optimisation du développement** : Modification de la configuration pour permettre le chargement local du plugin pour les environnements de développement et de DSO. [#26](https://github.com/dnum-mi/starter-kit-opencode/issues/26)
