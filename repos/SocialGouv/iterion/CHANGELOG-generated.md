## Changelog : iterion (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois a été marqué par une montée en maturité majeure de la plateforme, notamment avec l'intégration du backend d'exécution "Pi" et le renforcement de la sécurité des environnements isolés (sandboxes). L'accent a été mis sur l'automatisation de la qualité via de nouveaux agents spécialisés (vulnérabilités, couverture de tests) et sur une meilleure visibilité des ressources et des coûts pour les utilisateurs.

### Évolutions fonctionnelles
- **Nouveaux agents (Bots) :**
    - Introduction de **Senti**, un agent de surveillance des vulnérabilités basé sur l'inventaire [#515](https://github.com/SocialGouv/iterion/issues/515).
    - Déploiement d'**Endy**, un bot dédié à la mesure et à la complétion de la couverture de tests de bout en bout (e2e) [#fa20fe0](https://github.com/SocialGouv/iterion/issues/fa20fe0).
    - Amélioration des capacités des bots **Golden-Master** et **Modernize** pour inclure des audits d'accessibilité (a11y) et l'inventaire des assets.
- **Backend d'exécution :** Le backend **Pi** est désormais supporté comme une solution d'exécution de premier rang [#308](https://github.com/SocialGouv/iterion/issues/308).
- **Interface Studio :**
    - Amélioration de la visibilité lors des étapes de validation humaine (prévisualisation du JSON, Markdown et texte) [#425](https://github.com/SocialGouv/iterion/issues/425).
    - Ajout de fonctionnalités d'ergonomie : tiroirs de cartes redimensionnables [#335](https://github.com/SocialGouv/iterion/issues/335) et affichage des changements de fichiers directement dans la console de run [#352](https://github.com/SocialGouv/iterion/issues/352).
- **Connectivité :** Mise à disposition d'un serveur **MCP (Model Context Protocol)** pour exposer Iterion localement ou à distance [#0727783](https://github.com/SocialGouv/iterion/issues/0727783).
- **Gestion des ressources :** Mise en place d'une gestion plus fine des quotas et des budgets via une API et une interface CLI dédiée.

### Évolutions techniques
- **Sécurité et Isolation :**
    - Renforcement de la sécurité des sandboxes : protection accrue contre les liens symboliques, isolation stricte des identités Git et gestion sécurisée des secrets.
    - Durcissement de l'implémentation du serveur MCP pour l'opérateur.
- **Observabilité :**
    - Intégration de **Sentry/GlitchTip** pour le suivi des erreurs et la standardisation des logs [#463](https://github.com/SocialGouv/iterion/issues/463).
    - Amélioration du suivi des coûts et de l'utilisation des modèles.
- **Fiabilité du Runtime :**
    - Implémentation d'un mode "lame-duck" permettant de terminer proprement les exécutions en cours lors des déploiements.
    - Amélioration de la gestion des interruptions et de la reprise (resume) des exécutions.
    - Optimisation de la gestion des worktrees et du nettoyage automatique des ressources après exécution.
- **DSL et Backends :**
    - Ajout de chaînes de repli (fallbacks) entre différents modèles au sein du DSL [#365](https://github.com/SocialGouv/iterion/issues/365).
    - Support de la recherche web native via les outils du DSL [#550](https://github.com/SocialGouv/iterion/issues/550).

### Autres changements
- **Documentation :** Mise à jour massive de la documentation technique pour aligner les guides (notamment sur le backend Pi, les processus de revue et les capacités des agents) avec les dernières évolutions du code.
- **CI/CD :** Migration de la gestion des dépendances vers une application Renovate interne pour un meilleur contrôle [#509](https://github.com/SocialGouv/iterion/issues/509).
- **Infrastructure :** Mise à jour des images de base Docker.
