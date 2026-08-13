## Changelog : fisheries-and-environment-data-warehouse (30 derniers jours, au 12 août 2026)

### Résumé
Ce mois-ci, l'entrepôt de données s'enrichit de nouvelles sources statistiques (notamment via l'intégration de données Matomo) et de données relatives aux infractions environnementales. Les développements ont également permis de renforcer la fiabilité des indicateurs liés à l'environnement marin (AEM) et d'améliorer la robustesse des tests automatisés pour garantir la qualité des données intégrées.

### Évolutions fonctionnelles
- **Nouvelles données disponibles** : 
    - Intégration des statistiques Matomo, incluant les utilisateurs mensuels et le suivi quotidien des visiteurs uniques [#233](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/233).
    - Ajout de la table des infractions environnementales (`actions_infractions`) [#226](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/226).
    - Ajout de la table `eof`.
- **Indicateurs et rapports** : 
    - Rétablissement et amélioration des indicateurs pour l'AEM (Analytics Environnement Marin) via de nouvelles requêtes SQL dédiées [#224](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/224).
    - Ajout de nouvelles entrées de données pour la DGTM Guyane.

### Évolutions techniques
- **Pipelines de données** : 
    - Mise en place et enregistrement du nouveau flux de données `matomo_stats` [#220](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/220).
    - Optimisation du processus de synchronisation des tables depuis la base de données (mise à jour des configurations et des champs).
- **Architecture et organisation** : 
    - Réorganisation du stockage des requêtes avec le déplacement des fichiers SQL vers le répertoire `queries/data_warehouse`.
- **Qualité et Tests** : 
    - Refactorisation massive des jeux de données de test (fixtures SQL) pour les missions, les contrôles de pêche et les fichiers RPN.
    - Correction de plusieurs régressions dans les tests suite aux changements de structure de données.

### Autres changements
- **Maintenance et nettoyage** : 
    - Renommage systématique des fichiers de test SQL pour assurer une meilleure cohérence dans le projet.
    - Amélioration de la traçabilité grâce à l'ajout de logs de débogage pour les requêtes analytiques de mission.
    - Mise à jour de la configuration de sécurité (`trivyignore`).
