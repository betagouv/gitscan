## Changelog : catalogi (30 derniers jours, au 10 septembre 2026)

### Résumé
Cette période a été marquée par un renforcement des capacités d'administration et une optimisation significative des processus d'importation de données. Les outils de gestion de l'interface utilisateur ont été modernisés pour les administrateurs, tandis que la fiabilité des données provenant de sources externes (HAL, Wikidata, GitHub) a été grandement améliorée.

### Évolutions fonctionnelles
- **Gestion de l'interface (UI) :** Introduction d'un éditeur de configuration de l'interface utilisateur pour les administrateurs. Cette configuration est désormais stockée en base de données et modifiable via l'API d'administration.
- **Contrôle d'accès :** Mise en place de restrictions sur la création de logiciels et ajout de raccourcis dédiés pour les administrateurs.

### Évolutions techniques
- **Optimisation des imports :**
    - Amélioration des performances lors des imports massifs, notamment pour la source Zenodo [#516](https://github.com/codegouvfr/catalogi/issues/516).
    - Ajout d'un indicateur `lastimport` sur les sources pour un meilleur suivi.
- **Fiabilisation des données :**
    - Correction de plusieurs erreurs d'importation de données provenant de sources externes : corrections sur les identifiants et URLs pour HAL, la récupération des organisations via Wikidata, et la gestion des identifiants et descriptions utilisateurs depuis GitHub [#549](https://github.com/codegouvfr/catalogi/issues/549) [#550](https://github.com/codegouvfr/catalogi/issues/550).
- **Architecture et base de données :**
    - Migration de la configuration de l'interface utilisateur vers PostgreSQL.
    - Refactorisation des migrations de base de données et ajustement de l'utilisation des identifiants (conceptrecid).
- **Qualité logicielle :**
    - Amélioration de la suite de tests, notamment par le découplage des données de test de la configuration UI et une meilleure gestion des fixtures.

### Autres changements
- Ajustements de la configuration de build et de la nomenclature du projet.
