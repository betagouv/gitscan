## Changelog : aides-agri (30 derniers jours, au 18 août 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de l'outil d'administration (back-office) pour offrir une meilleure visibilité sur le statut des aides, l'automatisation de l'export des données vers data.gouv.fr et le renforcement de la fiabilité de la chaîne de déploiement (CI/CD).

### Évolutions fonctionnelles
- **Administration (Back-office) :**
    - Affichage du champ "Description" dans les fiches mères des aides [#720](https://github.com/betagouv/aides-agri/issues/720).
    - Ajout d'un indicateur visuel pour les aides clôturées dans la vue liste [#715](https://github.com/betagouv/aides-agri/issues/715).
    - Autorisation pour les bureaux valideurs de consulter les aides publiées pour relecture [#700](https://github.com/betagouv/aides-agri/issues/700).
    - Affichage du lien de partage pour la relecture, même lorsque l'aide est publiée en mode minimal [#699](https://github.com/betagouv/aides-agri/issues/699).
- **Données & Statistiques :**
    - Mise en place de l'export hebdomadaire automatique vers data.gouv.fr [#620](https://github.com/betagouv/aides-agri/issues/620) et optimisations successives du processus d'export [#716](https://github.com/betagouv/aides-agri/issues/716), [#714](https://github.com/betagouv/aides-agri/issues/714), [#707](https://github.com/betagouv/aides-agri/issues/707).
    - Publication des statistiques d'utilisation pour le mois de juillet 2026 [#697](https://github.com/betagouv/aides-agri/issues/697).
- **Expérience utilisateur :**
    - Correction d'un bug empêchant l'ouverture des liens externes [#696](https://github.com/betagouv/aides-agri/issues/696).

### Évolutions techniques
- **CI/CD & Infrastructure :**
    - Consolidation et optimisation des workflows GitHub Actions et de la chaîne d'intégration continue (CI) [#702](https://github.com/betagouv/aides-agri/issues/702), [#706](https://github.com/betagouv/aides-agri/issues/706).
- **Tests & Qualité :**
    - Ajustements de la suite de tests pour garantir la stabilité des fonctionnalités [#701](https://github.com/betagouv/aides-agri/issues/701).
- **Gestion des dépendances :**
    - Optimisation de la gestion des dépendances via l'outil `uv lock` pour assurer des environnements plus stables [#695](https://github.com/betagouv/aides-agri/issues/695), [#713](https://github.com/betagouv/aides-agri/issues/713).
