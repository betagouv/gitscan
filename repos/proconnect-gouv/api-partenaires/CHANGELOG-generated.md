## Changelog : api-partenaires (30 derniers jours, au 22 septembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la sécurité et de la fiabilité de la validation des domaines autorisés. L'intégration des données de l'annuaire administratif de la DILA a été approfondie pour garantir que les domaines déclarés sont authentiques et correctement tracés, tout en automatisant les contrôles de cohérence pour prévenir les erreurs de configuration.

### Évolutions fonctionnelles
- **Renforcement de la validation des domaines :** Refus systématique des domaines de messagerie génériques dans la liste blanche ([#57](https://github.com/proconnect-gouv/api-partenaires/issues/57)).
- **Amélioration de la conformité DILA :** Meilleure gestion des domaines attestés par la DILA, incluant la validation des domaines déclarés sur un canal unique ([#64](https://github.com/proconnect-gouv/api-partenaires/issues/64), [#68](https://github.com/proconnect-gouv/api-partenaires/issues/68)).
- **Traçabilité accrue :** Chaque ligne de la liste blanche est désormais liée à sa fiche DILA correspondante, permettant de savoir précisément quelle source atteste quel domaine ([#69](https://github.com/proconnect-gouv/api-partenaires/issues/69), [#70](https://github.com/proconnect-gouv/api-partenaires/issues/70)).

### Évolutions techniques
- **Sécurité et Accès :**
  - Suppression des rôles des scopes par défaut pour limiter les privilèges accordés par défaut ([#52](https://github.com/proconnect-gouv/api-partenaires/issues/52)).
- **Automatisation et Fiabilité :**
  - Mise en place de vérifications automatiques de la liste blanche lors des Pull Requests ([#58](https://github.com/proconnect-gouv/api-partenaires/issues/58)) et via une tâche planifiée quotidienne ([#54](https://github.com/proconnect-gouv/api-partenaires/issues/54)).
  - Ajout d'un contrôle de syntaxe (parsing) pour la configuration de la liste blanche OIDC ([#53](https://github.com/proconnect-gouv/api-partenaires/issues/53)).
  - Vérification systématique de la cohérence entre la liste blanche et l'export de données de la DILA ([#65](https://github.com/proconnect-gouv/api-partenaires/issues/65)).
- **Optimisation des performances :**
  - Implémentation d'un système de mise en cache de l'export de la DILA pour accélérer les processus de vérification ([#59](https://github.com/proconnect-gouv/api-partenaires/issues/59), [#62](https://github.com/proconnect-gouv/api-partenaires/issues/62)).
  - Création d'un index pour identifier rapidement quelle fiche déclare chaque domaine ([#63](https://github.com/proconnect-gouv/api-partenaires/issues/63)).
  - Ajout de logs pour monitorer l'efficacité du cache (hits/misses).

### Autres changements
- **Maintenance et DevOps :**
  - Fixation de la version de Bun via le `packageManager` pour garantir la reproductibilité des environnements ([#55](https://github.com/proconnect-gouv/api-partenaires/issues/55)).
  - Refactoring des types de sources de la liste blanche pour utiliser les énumérations Zod ([#67](https://github.com/proconnect-gouv/api-partenaires/issues/67)).
