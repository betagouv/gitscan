## Changelog : acceslibre-schema (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, le schéma a été mis à jour pour supporter plusieurs fichiers de schéma distincts, permettant une modélisation plus granulaire des informations d'accessibilité.  Cette évolution facilite la gestion et l'utilisation du schéma pour différents types de bâtiments et d'équipements.

### Évolutions fonctionnelles
- Introduction de la prise en charge de multiples fichiers de schéma : `schema_base`, `schema_floor`, `schema_hosting`, `schema_polling_station` et `schema_school`.  Cela permet de définir des schémas spécifiques pour chaque type de bâtiment ou d'élément.
- Conversion vers le format datapackage pour faciliter la gestion de ces multiples schémas.

### Évolutions techniques
- Implémentation de la conversion tableschema vers datapackage [#33](https://github.com/MTES-MCT/acceslibre-schema/pull/33).
