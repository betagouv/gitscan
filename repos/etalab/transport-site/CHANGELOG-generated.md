## Changelog : transport-site (30 derniers jours, au 02/09/2026)

### Résumé
Les récentes évolutions se concentrent sur la fiabilisation du traitement des données NeTEx et l'amélioration de la précision des rapports de consolidation (notamment pour l'IRVE). L'interface utilisateur a également été enrichie et optimisée pour offrir une meilleure visibilité lors de la gestion des données.

### Évolutions fonctionnelles
- **Amélioration des rapports IRVE** : ajout du statut des ressources dans les rapports de consolidation [#5565](https://github.com/etalab/transport-site/issues/5565).
- **Correction de données** : rectification du mapping des données GBFS pour Leo&Go [#5593](https://github.com/etalab/transport-site/issues/5593).
- **Interface utilisateur** : 
    - Ajout de nouvelles variantes pour les boutons colorés [#5603](https://github.com/etalab/transport-site/issues/5603).
    - Amélioration de l'affichage de l'interface en cas d'invalidité des données NeTEx [#5606](https://github.com/etalab/transport-site/issues/5606).
- **Extraction de données** : mise en place de l'extraction des téléchargements pour l'ART [#5590](https://github.com/etalab/transport-site/issues/5590).

### Évolutions techniques
- **Optimisation du moteur NeTEx** : 
    - Automatisation du choix de la version XSD en fonction de la date de publication des données [#5602](https://github.com/etalab/transport-site/issues/5602), [#5600](https://github.com/etalab/transport-site/issues/5600).
    - Amélioration des performances via le stockage direct des validations en DataFrame [#5577](https://github.com/etalab/transport-site/issues/5577).
    - Uniformisation du stockage et des versions du validateur [#5576](https://github.com/etalab/transport-site/issues/5576).
    - Extraction optimisée de la date de publication dans les métadonnées [#5599](https://github.com/etalab/transport-site/issues/5599).
- **Optimisation de traitement** : réduction du nombre de passes pour la correction des coordonnées lors de la consolidation IRVE [#5560](https://github.com/etalab/transport-site/issues/5560).
- **Maintenance et sécurité** : 
    - Application de mises à jour de sécurité [#5581](https://github.com/etalab/transport-site/issues/5581).
    - Stabilisation de la suite de tests [#5587](https://github.com/etalab/transport-site/issues/5587).
    - Correction de remontées d'erreurs via Sentry [#5610](https://github.com/etalab/transport-site/issues/5610).
