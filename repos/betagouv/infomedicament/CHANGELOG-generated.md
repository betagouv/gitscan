## Changelog : infomedicament (30 derniers jours, au 15/09/2026)

### Résumé
Cette période a été marquée par l'amélioration de la consultation des informations médicales, notamment grâce à l'ajout de vidéos, l'affichage direct des notices et une gestion plus fine des stocks par spécialité. L'interface utilisateur a également été affinée pour offrir une navigation plus fluide et une présentation plus claire des données.

### Évolutions fonctionnelles
- **Amélioration de la consultation** : Affichage direct des notices et des RCP via un rendu HTML [#290](https://github.com/betagouv/infomedicament/pull/290) et intégration de vidéos sur les pages de spécifications.
- **Gestion des stocks** : Mise en place de la gestion et de l'affichage des informations de stock par spécialité.
- **Optimisation de l'interface (UI)** : 
    - Corrections sur le menu mobile [#305](https://github.com/betagouv/infomedicament/pull/305), les sous-menus et les indications d'en-tête [#298](https://github.com/betagouv/infomedicament/pull/298).
    - Amélioration visuelle des blocs de stock (ajout de bordures) et de l'affichage des lignes CIP pour plus de clarté.
- **Qualité des données** : Nettoyage des données relatives à la pédiatrie.

### Évolutions techniques
- **Recherche et navigation** : Refonte de l'autocomplétion avec la création d'un point de terminaison (endpoint) et d'une logique dédiés [#279](https://github.com/betagouv/infomedicament/pull/279).
- **Infrastructure et Observabilité** : 
    - Amélioration du proxy [#301](https://github.com/betagouv/infomedicament/pull/301) et ajout d'un système de logs [#292](https://github.com/betagouv/infomedicament/pull/292).
    - Ajout de scripts de restauration [#299](https://github.com/betagouv/infomedicament/pull/299).
- **Fiabilisation** : 
    - Correction de la gestion des valeurs de stock nulles.
    - Renforcement de la suite de tests (intégration du CIS et vérification de la cohérence des données de stock).

### Autres changements
- **Maintenance** : Nettoyage de la base de données avec la suppression de tables de contenu inutilisées [#297](https://github.com/betagouv/infomedicament/pull/297).
