## Changelog : acceslibre-schema (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, le schéma a été mis à jour pour supporter la gestion de plusieurs schémas distincts, permettant une modélisation plus fine des informations d'accessibilité.  Cette évolution facilite la description des caractéristiques d'accessibilité pour différents types de bâtiments (bâtiments standards, étages, hébergements, bureaux de vote, écoles).

### Évolutions fonctionnelles
- Introduction d'une nouvelle structure basée sur des "datapackages" pour gérer plusieurs schémas : `schema_base`, `schema_floor`, `schema_hosting`, `schema_polling_station` et `schema_school`. [#33](https://github.com/MTES-MCT/acceslibre-schema/pull/33)
- Conversion du schéma au format datapackage pour supporter cette nouvelle structure. [#33](https://github.com/MTES-MCT/acceslibre-schema/pull/33)

### Évolutions techniques
-  Implémentation de la gestion de multiples schémas via l'utilisation de datapackages.
-  Refonte de la structure du schéma pour permettre la modularité et la réutilisation des définitions.

### Autres changements
-  Aucun autre changement significatif à signaler.
