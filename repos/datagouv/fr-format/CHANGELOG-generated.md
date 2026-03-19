## Changelog : fr-format (30 derniers jours, au 17 mars 2026)

### Résumé
Cette nouvelle version de `fr-format` apporte des améliorations significatives à la bibliothèque, notamment l'ajout d'un nouveau format de validation (IdRNB), la traduction de la documentation en français et une modernisation du code pour supporter Python 3.10 et supérieur. Des corrections de documentation et une refactorisation interne améliorent également la cohérence et la maintenabilité du projet.

### Évolutions fonctionnelles
- Ajout du nouveau format de validation `IdRNB` ([#54](https://github.com/datagouv/fr-format/pull/54)).
- Renommage de `NumeroDepartement` en `CodeDepartement` pour une meilleure clarté et cohérence ([#56](https://github.com/datagouv/fr-format/pull/56)).
- La documentation est maintenant entièrement en français ([#55](https://github.com/datagouv/fr-format/pull/55)).

### Évolutions techniques
- Modernisation du code pour supporter Python 3.10 et supérieur, avec correction de problèmes dans la documentation ([#53](https://github.com/datagouv/fr-format/pull/53)).
- Refactorisation pour uniformiser la structure du projet avec d'autres dépôts ([#51](https://github.com/datagouv/fr-format/pull/51)).
- Rationalisation des imports pour améliorer la lisibilité du code ([#57](https://github.com/datagouv/fr-format/pull/57)).
- Suppression de la méthode spécifique `new_geo` et unification de la gestion des formats géographiques INSEE dans `VersionedSetFormat`.  **Attention :** le paramètre `cog` des validateurs a été remplacé par `version` ([#41](https://github.com/datagouv/fr-format/pull/41)).

### Autres changements
- Correction des chemins d'accès aux fichiers dans la documentation ([#52](https://github.com/datagouv/fr-format/pull/52)).
- Ajout d'un fichier de contribution au projet ([#38](https://github.com/datagouv/fr-format/pull/38)).
- Amélioration du fichier README avec plus de détails ([#40](https://github.com/datagouv/fr-format/pull/40)).
- Ajout de la possibilité de récupérer toutes les valeurs valides pour un format ([#42](https://github.com/datagouv/fr-format/pull/42)).
- Mise à jour des formats `CodeRegion` et `Region` avec de nouvelles versions ([#46](https://github.com/datagouv/fr-format/pull/46)).
- Mise à jour de la source des codes postaux pour une meilleure fiabilité ([#47](https://github.com/datagouv/fr-format/pull/47)).
- Ajout de l'affichage de la source de chaque format français ([#43](https://github.com/datagouv/fr-format/pull/43)).
- Corrections mineures de code et de formatage ([#44](https://github.com/datagouv/fr-format/pull/44), [#37](https://github.com/datagouv/fr-format/pull/37)).
