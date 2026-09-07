## Changelog : catalogi (30 derniers jours, au 27 août 2026)

### Résumé
Cette période a été marquée par l'amélioration des outils d'administration, notamment via un nouvel éditeur de configuration de l'interface, et par une optimisation des processus d'importation de données massives. Plusieurs corrections ont également été apportées pour fiabiliser la synchronisation avec des sources externes telles que GitHub, Wikidata et HAL.

### Évolutions fonctionnelles
- Ajout d'un éditeur de configuration de l'interface utilisateur (UI) dédié aux administrateurs.
- Mise en place de restrictions sur la création de logiciels et ajout de raccourcis pour faciliter la navigation administrative.
- Ajout de la visibilité sur la date de dernière importation pour chaque source de données.

### Évolutions techniques
- **Optimisation des performances** : Amélioration des processus d'importation massive, notamment pour la source Zenodo [#516](https://github.com/codegouvfr/catalogi/issues/516).
- **Gestion de la configuration** : Migration de la configuration de l'interface utilisateur vers PostgreSQL pour permettre une gestion dynamique via l'API d'administration.
- **Fiabilisation des données et imports** :
    - Correction des flux d'importation de données HAL (gestion des identifiants ROR, des URLs de sites et des descriptions) [#549](https://github.com/codegouvfr/catalogi/issues/549).
    - Amélioration de la récupération des organisations via Wikidata.
    - Correction et fiabilisation de l'importation des utilisateurs et des identifiants depuis GitHub [#550](https://github.com/codegouvfr/catalogi/issues/550).
    - Correction de l'utilisation des identifiants de records (utilisation de `conceptrecid`).

### Autres changements
- Réorganisation de l'ordre des migrations de la base de données.
