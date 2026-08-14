## Changelog : aides-agri (30 derniers jours, au 13 août 2026)

### Résumé
Ce mois-ci, les évolutions ont principalement porté sur l'amélioration des outils de gestion administrative pour les gestionnaires d'aides, l'automatisation de la diffusion des données vers data.gouv.fr et la fiabilisation de l'infrastructure technique.

### Évolutions fonctionnelles
- **Gestion des aides (Back-office)** :
  - Affichage du champ "Description" dans les fiches mères d'aides [#720](https://github.com/betagouv/aides-agri/pull/720).
  - Ajout d'un indicateur visuel pour identifier les aides clôturées dans la vue liste [#715](https://github.com/betagouv/aides-agri/pull/715).
  - Extension des droits de relecture pour les bureaux valideurs sur les aides déjà publiées [#700](https://github.com/betagouv/aides-agri/pull/700).
  - Disponibilité du lien de partage pour la relecture, même lorsque l'aide est publiée en mode minimal [#699](https://github.com/betagouv/aides-agri/pull/699).
- **Données et Exports** :
  - Mise en place d'un export hebdomadaire automatisé vers data.gouv.fr [#620](https://github.com/betagouv/aides-agri/pull/620).
  - Améliorations et correctifs sur le flux d'export vers data.gouv.fr [#716](https://github.com/betagouv/aides-agri/pull/716), [#714](https://github.com/betagouv/aides-agri/pull/714) et [#707](https://github.com/betagouv/aides-agri/pull/707).
- **Expérience utilisateur et Statistiques** :
  - Correction d'un bug empêchant l'ouverture des liens externes [#696](https://github.com/betagouv/aides-agri/pull/696).
  - Intégration des statistiques pour le mois de juillet 2026 [#697](https://github.com/betagouv/aides-agri/pull/697).

### Évolutions techniques
- **Infrastructure et CI/CD** :
  - Consolidation des workflows GitHub Actions et de la chaîne d'intégration continue [#702](https://github.com/betagouv/aides-agri/pull/702), [#706](https://github.com/betagouv/aides-agri/pull/706).
  - Optimisation de la gestion des dépendances via l'outil `uv` [#713](https://github.com/betagouv/aides-agri/pull/713), [#695](https://github.com/betagouv/aides-agri/pull/695).
  - Reversion de la mise à jour de `django-htmx` pour stabiliser l'environnement [#732](https://github.com/betagouv/aides-agri/pull/732).
- **Tests** :
  - Ajustement de la suite de tests pour assurer la compatibilité avec les récents changements de structure [#701](https://github.com/betagouv/aides-agri/pull/701).
