## Changelog : aides-agri (30 derniers jours, au 26 août 2026)

### Résumé
Ce mois-ci, les développements se sont concentrés sur l'amélioration de l'outil d'administration (back-office) pour faciliter la gestion et la relecture des aides. Un effort majeur a été réalisé pour automatiser et fiabiliser la diffusion des données vers data.gouv.fr, tout en renforçant la stabilité de la chaîne de tests techniques.

### Évolutions fonctionnelles
- **Administration (Back-office) :**
    - Affichage du champ description dans les fiches mères d'aides [#720](https://github.com/betagouv/aides-agri/issues/720).
    - Ajout d'un indicateur visuel pour les aides clôturées dans la vue liste [#715](https://github.com/betagouv/aides-agri/issues/715).
    - Optimisation du processus de relecture : autorisation d'accès aux bureaux valideurs [#700](https://github.com/betagouv/aides-agri/issues/700) et affichage systématique du lien de partage, même pour les aides publiées en mode minimal [#699](https://github.com/betagouv/aides-agri/issues/699).
- **Données & Open Data :**
    - Mise en place de l'export hebdomadaire automatique vers data.gouv.fr [#620](https://github.com/betagouv/aides-agri/issues/620) et série de correctifs pour fiabiliser ces exports [#716](https://github.com/betagouv/aides-agri/issues/716), [#714](https://github.com/betagouv/aides-agri/issues/714), [#707](https://github.com/betagouv/aides-agri/issues/707).
- **Expérience utilisateur & Statistiques :**
    - Correction d'un bug empêchant l'ouverture des liens externes [#696](https://github.com/betagouv/aides-agri/issues/696).
    - Mise à jour des statistiques pour le mois de juillet 2026 [#697](https://github.com/betagouv/aides-agri/issues/697).

### Évolutions techniques
- **CI/CD :**
    - Consolidation de la chaîne d'intégration continue (CI) pour améliorer la stabilité des déploiements [#702](https://github.com/betagouv/aides-agri/issues/702).
