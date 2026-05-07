## Changelog : acceslibre-schema (30 derniers jours, au 15 avril 2026)

### Résumé
Cette mise à jour majeure introduit la possibilité de gérer plusieurs schémas distincts pour différents types de bâtiments (base, étage, hébergement, bureau de vote, école) au sein d'un même *datapackage*. Cela permet une modélisation plus précise et flexible des informations d'accessibilité.

### Évolutions fonctionnelles
- Introduction de schémas spécifiques pour différents types de bâtiments :
  - `schema_base`
  - `schema_floor`
  - `schema_hosting`
  - `schema_polling_station`
  - `schema_school`
- Utilisation du format *datapackage* pour regrouper ces schémas multiples.

### Évolutions techniques
- Conversion du schéma vers un format *datapackage* pour supporter la gestion de schémas multiples [#33](https://github.com/MTES-MCT/acceslibre-schema/pull/33).
- Implémentation de la conversion tableschema vers datapackage.

### Autres changements
- Aucune autre modification significative n'a été apportée durant cette période.
