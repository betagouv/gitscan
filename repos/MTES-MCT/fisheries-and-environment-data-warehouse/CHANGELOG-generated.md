## Changelog : fisheries-and-environment-data-warehouse (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à l'entrepôt de données dédié aux pêches et à l'environnement marin. Les modifications récentes se concentrent sur l'enrichissement des données, notamment concernant les unités de contrôle et les missions, ainsi que sur des corrections et des optimisations internes pour améliorer la qualité et la fiabilité des données. Des mises à jour de sécurité et de dépendances ont également été effectuées.

### Évolutions fonctionnelles
- Ajout de données relatives aux unités de contrôle dans les requêtes, enrichissant ainsi les informations disponibles pour l'analyse. [#159](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/159)
- Les missions interservices sont désormais divisées en plusieurs lignes pour une meilleure granularité des données. [#158](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/158)
- Ajout de filtres pour les missions complètes et terminées, permettant une analyse plus ciblée. [#154](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/154)
- Ajout des tables `threats` et `threat_characterizations` pour intégrer des informations sur les menaces. [#153](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/153)
- Mise à jour des données `analytics_actions` et `monitorfish` pour améliorer la précision des analyses. [#156](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/156) et [#147](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/147)

### Évolutions techniques
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Ajout de facades pour une meilleure organisation du code. [#165](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/165)
- Suppression de colonnes inutiles (Facade et Mission Type). [#155](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/155)
- Mise à jour du workflow Dependabot pour une gestion plus efficace des dépendances.
- Mise à jour de la configuration de Trivy pour améliorer la sécurité. [#151](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/151)

### Autres changements
- Mise à jour des dépendances de sécurité et des versions des librairies utilisées. [#150](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/150) et [#148](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/148)
- Correction de tests suite à des modifications de code.
- Ajout de valeurs par défaut pour certaines colonnes. [#166](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/166)
