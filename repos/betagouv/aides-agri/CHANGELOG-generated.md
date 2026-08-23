## Changelog : aides-agri (30 derniers jours, au 21 août 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'automatisation de la diffusion des données vers data.gouv.fr et l'amélioration des outils de gestion pour les administrateurs. Les fonctionnalités de relecture et de suivi des aides dans l'interface d'administration ont été renforcées pour offrir une meilleure visibilité sur le cycle de vie des dispositifs.

### Évolutions fonctionnelles
- **Administration (Back-office) :**
    - Affichage du champ "Description" dans les fiches mères d'aides [#720](https://github.com/betagouv/aides-agri/pull/720).
    - Ajout d'un indicateur visuel pour les aides clôturées dans la vue liste [#715](https://github.com/betagouv/aides-agri/pull/715).
    - Amélioration du processus de relecture : les bureaux valideurs peuvent désormais consulter les aides publiées [#700](https://github.com/betagouv/aides-agri/pull/700) et le lien de partage reste accessible même en mode minimal [#699](https://github.com/betagouv/aides-agri/pull/699).
- **Données et Exports :**
    - Mise en place d'un export hebdomadaire automatique vers data.gouv.fr [#620](https://github.com/betagouv/aides-agri/pull/620).
    - Plusieurs améliorations et correctifs apportés au processus d'export vers data.gouv.fr [#716](https://github.com/betagouv/aides-agri/pull/716), [#714](https://github.com/betagouv/aides-agri/pull/714), [#707](https://github.com/betagouv/aides-agri/pull/707).
- **Expérience utilisateur et Statistiques :**
    - Correction d'un bug empêchant l'ouverture des liens externes [#696](https://github.com/betagouv/aides-agri/pull/696).
    - Publication des statistiques pour le mois de juillet 2026 [#697](https://github.com/betagouv/aides-agri/pull/697).

### Évolutions techniques
- **CI/CD :** Consolidation et optimisation des workflows GitHub Actions et de la chaîne d'intégration continue [#702](https://github.com/betagouv/aides-agri/pull/702), [#706](https://github.com/betagouv/aides-agri/pull/706).
- **Maintenance :** Mise à jour de la gestion des dépendances via l'outil `uv` [#695](https://github.com/betagouv/aides-agri/pull/695).
