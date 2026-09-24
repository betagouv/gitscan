## Changelog : api-partenaires (30 derniers jours, au 22 septembre 2026)

### Résumé
Ce mois a été marqué par un renforcement significatif de la sécurité et de la fiabilité de la liste blanche (allowlist) des domaines. Grâce à l'intégration automatisée des données de l'annuaire administratif de la DILA, le système peut désormais vérifier et tracer avec précision l'origine de chaque domaine autorisé, tout en bloquant les domaines de messagerie génériques pour limiter les risques.

### Évolutions fonctionnelles
- Sécurisation de la liste blanche par le refus automatique des domaines de messagerie génériques (ex: gmail.com) [#57](https://github.com/proconnect-gouv/api-partenaires/issues/57).

### Évolutions techniques
- **Intégration et automatisation DILA** :
  - Mise en place de la récupération et de la mise en cache automatique de l'export de l'annuaire administratif de la DILA via un processus quotidien [#59](https://github.com/proconnect-gouv/api-partenaires/issues/59), [#62](https://github.com/proconnect-gouv/api-partenaires/issues/62).
  - Amélioration de la traçabilité en liant chaque domaine autorisé à sa fiche DILA d'origine [#69](https://github.com/proconnect-gouv/api-partenaires/issues/69), [#70](https://github.com/proconnect-gouv/api-partenaires/issues/70).
  - Automatisation des contrôles de cohérence de la liste blanche lors des Pull Requests et de manière quotidienne [#54](https://github.com/proconnect-gouv/api-partenaires/issues/54), [#58](https://github.com/proconnect-gouv/api-partenaires/issues/58).
  - Ajout d'un index pour identifier précisément quelle fiche déclare chaque domaine [#63](https://github.com/proconnect-gouv/api-partenaires/issues/63).
- **Sécurité et gestion des accès** :
  - Renforcement du contrôle d'accès par la suppression des scopes de rôles des scopes par défaut [#52](https://github.com/proconnect-gouv/api-partenaires/issues/52).
- **Maintenance et structure de données** :
  - Refactorisation du modèle MongoDB pour renommer le champ `fqdns` en `attached_email_domains` [#31](https://github.com/proconnect-gouv/api-partenaires/issues/31), [#36](https://github.com/proconnect-gouv/api-partenaires/issues/36).
  - Fixation de la version de Bun via le gestionnaire de paquets pour garantir la stabilité de l'environnement [#55](https://github.com/proconnect-gouv/api-partenaires/issues/55).
