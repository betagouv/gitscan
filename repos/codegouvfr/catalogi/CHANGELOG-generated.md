## Changelog : catalogi (30 derniers jours, au 27 août 2026)

### Résumé
Cette période a été marquée par un renforcement des outils d'administration, notamment pour la gestion de l'interface, et une amélioration significative de la fiabilité et de la performance des processus d'importation de données provenant de sources externes (HAL, Zenodo, GitHub).

### Évolutions fonctionnelles
- **Administration de l'interface** : Ajout d'un éditeur de configuration de l'interface utilisateur pour les administrateurs.
- **Gestion des logiciels** : Mise en place de contrôles sur la création de logiciels et ajout de raccourcis de navigation pour l'administration.
- **Suivi des données** : Ajout de la date de dernier import sur les sources pour une meilleure traçabilité.
- **Importation Zenodo** : Amélioration du processus d'importation massive des données issues de Zenodo.

### Évolutions techniques
- **Optimisation des performances** : Amélioration des processus d'importation massive de données [#516](https://github.com/codegouvfr/catalogi/issues/516).
- **Architecture de configuration** : La configuration de l'interface utilisateur est désormais stockée en base de données (PostgreSQL) et pilotable via l'API d'administration.
- **Fiabilisation des imports de données externes** :
    - Correction des flux de données **HAL** (gestion des identifiants ROR/RNSR, des URLs de sites et des descriptions).
    - Correction de la récupération des organisations via **Wikidata**.
    - Correction de l'importation des utilisateurs et de la gestion des identifiants depuis **GitHub**.
- **Correction de données** : Passage à l'utilisation de `conceptrecid` au lieu de l'ID de record pour assurer la cohérence des données.

### Autres changements
- Réorganisation de l'ordre des migrations de la base de données.
