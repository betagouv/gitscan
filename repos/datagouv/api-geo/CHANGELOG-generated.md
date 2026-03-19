## Changelog : api-geo (30 derniers jours, au 10 mars 2026)

### Résumé
Cette mise à jour apporte une amélioration de la normalisation des chaînes de caractères, notamment pour les noms de lieux contenant des apostrophes ou des caractères spéciaux. Cette correction améliore la qualité des recherches et des correspondances géographiques au sein de l'API.

### Évolutions fonctionnelles
- Correction d'un bug dans la fonction de normalisation des chaînes de caractères qui empêchait la reconnaissance correcte de certains noms de lieux (ex: "d'Alençon") [#202](https://github.com/datagouv/api-geo/pull/202).

### Évolutions techniques
- Amélioration de la fonction `normalizeString` pour une meilleure gestion des caractères spéciaux et des apostrophes.

### Autres changements
- Aucun changement significatif à signaler.
