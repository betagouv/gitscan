## Changelog : trackdechets-vigiedechets (30 derniers jours, au 15 juillet 2026)

### Résumé
Cette mise à jour apporte des corrections concernant les dates d'export des données, notamment pour les déclarations du 31 décembre 2025. Des améliorations de maintenabilité ont également été apportées en centralisant les variables de template et en appliquant un formatage de code cohérent.

### Évolutions fonctionnelles
- Correction de la date d'affichage des exports pour tenir compte de l'absence de déclarations au 31/12/2025.  [#519](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/519)
- Mise à jour des dates dans le template PDF pour les exports de données. [#517](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/517) et [#41a335b](https://github.com/MTES-MCT/trackdechets-vigiedechets/commit/41a335b)

### Évolutions techniques
- Refactoring : Centralisation des variables de template via un context processor pour une meilleure organisation et réutilisation. [#518](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/518) et [#9faa4de](https://github.com/MTES-MCT/trackdechets-vigiedechets/commit/9faa4de)
- Application du formatage de code avec `ruff` pour améliorer la lisibilité et la cohérence du code. [#23ab147](https://github.com/MTES-MCT/trackdechets-vigiedechets/commit/23ab147)

### Autres changements
- Mise à jour de la configuration Matomo. [#521](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/521) et [#5d2973b](https://github.com/MTES-MCT/trackdechets-vigiedechets/commit/5d2973b)
- Actualisation de la date. [#dfdc06a](https://github.com/MTES-MCT/trackdechets-vigiedechets/commit/dfdc06a)
