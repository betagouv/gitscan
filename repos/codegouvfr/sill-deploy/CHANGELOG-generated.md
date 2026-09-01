## Changelog : sill-deploy (30 derniers jours, au 30 août 2026)

### Résumé
Cette période a été marquée par un renforcement des capacités d'administration, avec notamment la mise en place d'un outil permettant de configurer l'interface utilisateur directement depuis l'application. Les processus d'importation de données ont également été optimisés et fiabilisés pour garantir une meilleure qualité des catalogues de logiciels.

### Évolutions fonctionnelles
- **Administration de l'interface** : Ajout d'un éditeur de configuration de l'interface utilisateur (UI), désormais stocké en base de données et modifiable via l'API d'administration.
- **Gestion des sources** : Ajout de la visibilité sur la date de dernière importation pour chaque source de données.
- **Contrôle d'accès** : Restriction de la création de logiciels et ajout de raccourcis dédiés pour les administrateurs.
- **Importation Zenodo** : Amélioration du processus d'importation spécifique pour les données Zenodo.

### Évolutions techniques
- **Optimisation des performances** : Amélioration des performances lors des imports massifs de données [#516](https://github.com/codegouvfr/sill-deploy/issues/516).
- **Fiabilisation des données (Corrections)** :
    - Correction des erreurs d'importation des données HAL (gestion des identifiants ROR/RNSR et des URLs) [#549](https://github.com/codegouvfr/sill-deploy/issues/549).
    - Correction de la récupération des organisations via Wikidata.
    - Correction de l'importation des utilisateurs et de la gestion des identifiants GitHub [#550](https://github.com/codegouvfr/sill-deploy/issues/550).
    - Résolution de problèmes liés à l'importation des descriptions et au stockage des données externes en base de données.
    - Correction de l'utilisation des identifiants de records (passage à `conceptrecid`).
- **Infrastructure et CI/CD** : Ajout de nouveaux workflows de déploiement et de configurations de personnalisation.

### Autres changements
- Réorganisation de l'ordre des migrations de base de données.
