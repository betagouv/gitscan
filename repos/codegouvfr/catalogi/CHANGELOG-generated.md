## Changelog : catalogi (30 derniers jours, au 27 août 2026)

### Résumé
Cette période a été marquée par un renforcement des outils d'administration, notamment via un nouvel éditeur de configuration de l'interface, et une optimisation des processus d'importation de données. Plusieurs correctifs ont également été apportés pour fiabiliser la récupération d'informations provenant de sources externes telles que GitHub, Wikidata ou HAL.

### Évolutions fonctionnelles
- Ajout d'un éditeur de configuration de l'interface utilisateur dédié aux administrateurs.
- Amélioration des processus d'importation massive de données, particulièrement pour Zenodo.
- Ajout de la visibilité sur la date de dernière importation pour les sources.
- Encadrement de la création de logiciels et ajout de raccourcis d'accès pour les administrateurs.

### Évolutions techniques
- Optimisation des performances lors des importations massives [#516](https://github.com/codegouvfr/catalogi/issues/516).
- Migration de la configuration de l'interface utilisateur vers PostgreSQL pour permettre une gestion dynamique via API.
- Fiabilisation de l'importation et de la synchronisation des données :
    - Corrections sur les données HAL (gestion des identifiants ROR/RNSR et des URLs) [#549](https://github.com/codegouvfr/catalogi/issues/549).
    - Amélioration de la récupération des organisations via Wikidata.
    - Correction de l'importation des utilisateurs et de la gestion des identifiants GitHub [#550](https://github.com/codegouvfr/catalogi/issues/550).
    - Correction de la sauvegarde des descriptions et des données externes en base de données.
    - Utilisation de `conceptrecid` au lieu de l'ID de l'enregistrement pour une meilleure identification.

### Autres changements
- Réorganisation des migrations de la base de données.
