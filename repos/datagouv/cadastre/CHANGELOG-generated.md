## Changelog : cadastre (30 derniers jours, au 2 mai 2026)

### Résumé
Cette version apporte principalement une mise à jour des données de découpage administratif (COG) pour l'année 2026, assurant la cohérence des informations cadastrales avec les dernières données de la DGFIP.  Des corrections mineures de linting ont également été apportées.

### Évolutions fonctionnelles
- Mise à jour des données de découpage administratif (COG) pour 2026, intégrant les changements de la DGFIP. [#145](https://github.com/datagouv/cadastre/pull/145)

### Évolutions techniques
- Mise à jour de la dépendance `@etalab/decoupage-administratif` pour supporter les nouveaux formats de données de la DGFIP.
- Modification de l'expression régulière utilisée pour identifier les départements afin de s'adapter aux changements de la DGFIP.

### Autres changements
- Correction de problèmes de linting pour améliorer la qualité du code. [#145](https://github.com/datagouv/cadastre/pull/145)
