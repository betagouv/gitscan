## Changelog : acceslibre-schema (30 derniers jours, au 15 avril 2026)

### Résumé
Cette mise à jour majeure introduit la possibilité de gérer plusieurs schémas distincts pour différents types de bâtiments (base, étage, hébergement, bureaux de vote, écoles) via l'utilisation d'un format datapackage. Cela permet une modélisation plus précise et flexible des informations d'accessibilité.

### Évolutions fonctionnelles
- Introduction de schémas spécifiques pour différents types de bâtiments :
  - `schema_base`
  - `schema_floor`
  - `schema_hosting`
  - `schema_polling_station`
  - `schema_school`
- Conversion du schéma vers le format datapackage pour supporter ces multiples schémas.

### Évolutions techniques
- Implémentation de la conversion tableschema vers datapackage [#33](https://github.com/MTES-MCT/acceslibre-schema/pull/33).
- Restructuration interne pour supporter la gestion de plusieurs schémas.

### Autres changements
- Aucun autre changement significatif à signaler.
