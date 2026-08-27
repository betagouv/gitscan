## Changelog : autometa (30 derniers jours, au 27 août 2026)

### Résumé
Les dernières évolutions renforcent les capacités d'analyse de l'assistant avec l'ajout de nouveaux outils de requêtage et une interface plus flexible. En parallèle, la stabilité et la fiabilité du système ont été nettement améliorées grâce à une optimisation des sauvegardes, une meilleure gestion des erreurs et une automatisation accrue des tests et du déploiement.

### Évolutions fonctionnelles
- Ajout d'une nouvelle capacité de requêtage via l'intégration Tally [#167](https://github.com/gip-inclusion/autometa/issues/167).
- Personnalisation de la page d'accueil [#199](https://github.com/gip-inclusion/autometa/issues/199).
- Corrections d'interface : sélection multi-lignes dans le champ de nouvelle conversation [#185](https://github.com/gip-inclusion/autometa/issues/185), erreurs de rendu Mermaid [#198](https://github.com/gip-inclusion/autometa/issues/198) et correction des doublons de création de conversation lors de la navigation.

### Évolutions techniques
- **Infrastructure & CI/CD** : Amélioration de la suite de tests (tests unitaires et intégration) [#181](https://github.com/gip-inclusion/autometa/issues/181), mise en place de "review apps" sur Scalingo pilotées par la CI [#191](https://github.com/gip-inclusion/autometa/issues/191) et optimisation de la compression des assets lors de la synchronisation vers les buckets publics [#197](https://github.com/gip-inclusion/autometa/issues/197).
- **Données & Stockage** : Optimisation et sécurisation des sauvegardes S3 via l'activation du versioning [#186](https://github.com/gip-inclusion/autometa/issues/186) [#187](https://github.com/gip-inclusion/autometa/issues/187) et ajout d'une nouvelle source de données de test (Dora staging) [#202](https://github.com/gip-inclusion/autometa/issues/202).
- **Fiabilité & Code** : Refactorisation des clients PostgreSQL pour simplifier l'accès aux données [#203](https://github.com/gip-inclusion/autometa/issues/203) et amélioration de la résilience des tâches planifiées (gestion des timeouts Metabase) [#182](https://github.com/gip-inclusion/autometa/issues/182).
