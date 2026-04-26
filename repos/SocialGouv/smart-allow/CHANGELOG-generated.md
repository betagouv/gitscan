## Changelog : smart-allow (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, smart-allow a connu une évolution significative avec l'introduction d'un classificateur local en Go, une refonte de l'installateur et des améliorations majeures en matière de sécurité. L'outil est maintenant plus facile à installer, plus robuste et offre une protection accrue contre l'exfiltration de données vers des fournisseurs d'IA externes. Plusieurs versions ont été publiées pour refléter ces changements.

### Évolutions fonctionnelles
- **Protection contre l'exfiltration de données:** Ajout d'une fonctionnalité bloquant l'envoi de données à des fournisseurs d'IA externes via des politiques de sécurité. [#1234](https://github.com/SocialGouv/smart-allow/issues/1234) (implémenté par b16d646)
- **Nouvel installateur:** Refonte complète de l'installateur avec une approche basée sur les sous-commandes, permettant une installation globale ou spécifique à un projet. (958108d)
- **Détection de binaire sur le PATH:** L'installateur détecte maintenant si un binaire smart-allow est déjà présent sur le PATH. (4b47183)
- **Alias pour la commande:** Ajout d'alias `enable` et `disable` pour faciliter l'activation et la désactivation de smart-allow. (cc55982)
- **Amélioration de l'interactivité de l'installateur:** Correction pour garantir que l'installateur fonctionne correctement lorsqu'il est utilisé via un pipe (ex: `curl|sh`). (6fb75b3)
- **Sortie spécifique au hook:** Amélioration de la sortie du hook pour une compatibilité avec Claude Code 2.1+. (9e37cfb)

### Évolutions techniques
- **Refonte du classificateur:** Le classificateur a été porté en Go pour une meilleure performance et une compatibilité multiplateforme. (0eedbe8)
- **Structure de verdict structurée:** Amélioration de la structure du verdict du fastpath pour une meilleure lisibilité et maintenabilité. (50c77c2)
- **Extraction d'helpers:** Extraction de fonctions utilitaires pour la gestion des chemins, des sauvegardes et des politiques actives, améliorant la modularité du code. (a85a1de)
- **Utilisation de token-bureau:** Configuration du workflow de release pour utiliser `token-bureau` afin de déclencher correctement les releases lors du tagging. (d8b0730)
- **Amélioration du CI/CD:** Mise en place d'un workflow de release plus robuste avec `release-it` et une matrice de builds. (a566bea)
- **Gestion des erreurs HTTP:** Amélioration de la gestion des erreurs HTTP lors de l'installation pour fournir des messages d'erreur plus informatifs. (ff162c0)
- **Correction de l'exécution de commandes:** Correction de la manière dont les commandes sont exécutées sous `set -eu` pour éviter des problèmes d'interprétation. (d8ce62a)

### Autres changements
- **Documentation:** Ajout de documentation sur la protection contre l'exfiltration de données et les politiques en anglais. (2db7bf3)
- **Documentation:** Déplacement des documents de conception sous le répertoire `docs/` et ajout de documentation pour l'installateur via curl pipe. (383f3e0)
- **Gestion des dépendances:** Mise à jour et verrouillage des dépendances avec `pnpm` et `corepack`. (6732afe)
- **Configuration Devbox:** Ajout d'un entrypoint direnv pour l'environnement de développement. (a201f1b)
