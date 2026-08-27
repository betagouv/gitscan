## Changelog : aides-agri (30 derniers jours, au 26 août 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'automatisation de la diffusion des données vers data.gouv.fr, l'amélioration des outils de gestion pour les administrateurs (back-office) et le renforcement de la fiabilité de la chaîne de déploiement technique.

### Évolutions fonctionnelles
- **Diffusion des données (Open Data) :**
    - Mise en place de l'export hebdomadaire automatique vers data.gouv.fr ([#620](https://github.com/betagouv/aides-agri/issues/620)).
    - Améliorations et corrections de la fiabilité des exports vers data.gouv.fr ([#716](https://github.com/betagouv/aides-agri/issues/716), [#714](https://github.com/betagouv/aides-agri/issues/714), [#707](https://github.com/betagouv/aides-agri/issues/707)).
- **Améliorations du Back-office :**
    - Meilleure visibilité sur le cycle de vie des aides avec l'affichage du statut "clôturé" dans la vue liste ([#715](https://github.com/betagouv/aides-agri/issues/715)).
    - Ajout du champ "Description" dans la gestion des fiches mères d'aides ([#720](https://github.com/betagouv/aides-agri/issues/720)).
    - Optimisation du processus de relecture : autorisation pour les bureaux valideurs de consulter les aides publiées ([#700](https://github.com/betagouv/aides-agri/issues/700)) et maintien de la visibilité du lien de partage même en mode de publication minimal ([#699](https://github.com/betagouv/aides-agri/issues/699)).
- **Expérience utilisateur et statistiques :**
    - Correction d'un bug empêchant l'ouverture de certains liens externes ([#696](https://github.com/betagouv/aides-agri/issues/696)).
    - Publication des statistiques d'utilisation pour le mois de juillet 2026 ([#697](https://github.com/betagouv/aides-agri/issues/697)).

### Évolutions techniques
- **CI/CD :** Consolidation et optimisation de la chaîne d'intégration continue ([#702](https://github.com/betagouv/aides-agri/issues/702)).
- **Maintenance :** Reversion d'une mise à jour de la dépendance `django-htmx` pour garantir la stabilité du projet ([#732](https://github.com/betagouv/aides-agri/issues/732)).
