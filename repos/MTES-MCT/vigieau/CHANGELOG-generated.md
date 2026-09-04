## Changelog : vigieau (30 derniers jours, au 3 septembre 2026)

### Résumé
Ce mois-ci, les développements ont porté sur la mise en conformité de l'accessibilité numérique (RGAA), la fiabilisation de la reconstitution des données historiques et l'amélioration de la précision des données géographiques issues du SANDRE.

### Évolutions fonctionnelles
- **Accessibilité** : corrections majeures pour améliorer la navigation, l'utilisation des formulaires, la recherche d'adresse et la hiérarchie des contenus pour les utilisateurs.
- **Continuité de service** : les restrictions d'eau restent consultables par le public même durant les phases de mise à jour des données.
- **Export de données** : fiabilisation et amélioration du téléchargement des données au format GeoJSON.
- **Interface** : mise à jour des dénominations des ministères.

### Évolutions techniques
- **Gestion de l'historique** : mise en place d'un système de reconstitution de données (*backfill*) avec des workers distribués et un plan de contrôle dédié [#44](https://github.com/MTES-MCT/vigieau/pull/44).
- **Précision géographique** : amélioration de la gestion de la précision géométrique des données SANDRE [#46](https://github.com/MTES-MCT/vigieau/pull/46).
- **Performance** : optimisation de la base de données via l'indexation des communes par département et réduction de la taille des échanges de données (*payloads*).
- **Robustesse et CI/CD** : renforcement de la surveillance en production (*smoke tests*) et stabilisation des pipelines de publication [#33](https://github.com/MTES-MCT/vigieau/pull/33) [#35](https://github.com/MTES-MCT/vigieau/pull/35).
- **Sécurité des données** : sécurisation des processus de remplacement et de restauration des certifications historiques.

### Autres changements
- **Documentation** : ajout du plan de remédiation RGAA et de la documentation relative aux opérations de reconstitution historique.
- **Sécurité** : résolution de vulnérabilités identifiées dans les dépendances npm.
