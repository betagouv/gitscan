## Changelog : acceslibre-schema (30 derniers jours, au 15 avril 2026)

### Résumé
Cette mise à jour majeure introduit la prise en charge de schémas multiples pour une meilleure organisation et flexibilité des données d'accessibilité. Le schéma est désormais divisé en plusieurs fichiers (base, étage, hébergement, bureau de vote, école) pour faciliter la gestion et l'utilisation des informations spécifiques à chaque type de bâtiment.

### Évolutions fonctionnelles
- Introduction de schémas distincts pour différents types de bâtiments :
  - `schema_base` : Schéma de base commun à tous les types de bâtiments.
  - `schema_floor` : Schéma pour les informations relatives aux étages.
  - `schema_hosting` : Schéma pour les informations relatives aux hébergements.
  - `schema_polling_station` : Schéma pour les informations relatives aux bureaux de vote.
  - `schema_school` : Schéma pour les informations relatives aux écoles.
- Conversion vers un format datapackage pour supporter ces multiples schémas.

### Évolutions techniques
- Implémentation de la conversion tableschema vers datapackage [#33](https://github.com/MTES-MCT/acceslibre-schema/pull/33).
- Refonte de la structure des schémas pour permettre la modularité et la réutilisation.

### Autres changements
- Aucun autre changement significatif à signaler.
