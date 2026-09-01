## Changelog : autometa (30 derniers jours, au 30 août 2026)

### Résumé
Ce mois-ci, Autometa s'est enrichi de nouvelles capacités de personnalisation et d'outils de tri plus performants pour les utilisateurs. Parallèlement, un travail important a été réalisé sur la robustesse de l'infrastructure, notamment via l'optimisation des sauvegardes, le renforcement des tests automatisés et l'amélioration de la fiabilité des tâches de fond.

### Évolutions fonctionnelles
- Personnalisation de la page d'accueil [#199](https://github.com/gip-inclusion/autometa/issues/199).
- Intégration de Tally pour de nouvelles capacités de requêtage [#167](https://github.com/gip-inclusion/autometa/issues/167).
- Refonte du système de tags pour faciliter le tri des conversations et des tableaux de bord [#190](https://github.com/gip-inclusion/autometa/issues/190).
- Amélioration de la clarté des alertes en cas de dépassement des limites d'abonnement [#180](https://github.com/gip-inclusion/autometa/issues/180).
- Corrections d'interface : sélection multi-lignes dans le champ de conversation [#185](https://github.com/gip-inclusion/autometa/issues/185), correction des plantages de rendu Mermaid [#198](https://github.com/gip-inclusion/autometa/issues/198) et résolution d'un problème de création multiple de conversations lors de la navigation.

### Évolutions techniques
- Changement de la base de données source du projet [#168](https://github.com/gip-inclusion/autometa/issues/168).
- Optimisation et sécurisation des sauvegardes S3 (implémentation du versioning et compression des assets) [#186](https://github.com/gip-inclusion/autometa/issues/186), [#187](https://github.com/gip-inclusion/autometa/issues/187), [#197](https://github.com/gip-inclusion/autometa/issues/197).
- Refactorisation de la gestion des clients PostgreSQL pour simplifier l'accès aux données [#203](https://github.com/gip-inclusion/autometa/issues/203).
- Amélioration de la fiabilité des tâches planifiées (cron) et de la gestion des timeouts Metabase [#182](https://github.com/gip-inclusion/autometa/issues/182).
- Renforcement de la chaîne CI/CD : mise en place d'une suite de tests unitaires hermétiques [#181](https://github.com/gip-inclusion/autometa/issues/181) et déploiement de "review apps" sur Scalingo [#191](https://github.com/gip-inclusion/autometa/issues/191).
- Ajout d'une nouvelle source de données de test (Dora staging) pour les environnements de staging [#202](https://github.com/gip-inclusion/autometa/issues/202).
