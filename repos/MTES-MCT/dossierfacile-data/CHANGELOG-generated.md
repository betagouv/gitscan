## Changelog : dossierfacile-data (30 derniers jours, au 2026-05-13)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la modélisation des documents et des garanties, avec une refonte du modèle des documents et des corrections liées à l'unicité des identifiants de garant. Des travaux ont également été réalisés pour ajouter un nouveau modèle de fonctionnalité utilisateur.

### Évolutions fonctionnelles
- Correction d'un problème lié à l'unicité de l'identifiant de garant dans le modèle `guarantor_document` [#68](https://github.com/MTES-MCT/dossierfacile-data/issues/68), [#69](https://github.com/MTES-MCT/dossierfacile-data/issues/69), [#70](https://github.com/MTES-MCT/dossierfacile-data/issues/70).
- Ajout d'un nouveau modèle DBT pour la fonctionnalité utilisateur [#64](https://github.com/MTES-MCT/dossierfacile-data/issues/64).
- Refonte du modèle des documents pour améliorer sa structure et sa pertinence [#67](https://github.com/MTES-MCT/dossierfacile-data/issues/67).

### Évolutions techniques
- Refactorisation de la construction du modèle des documents à partir des logs des locataires [#66](https://github.com/MTES-MCT/dossierfacile-data/issues/66).
- Suppression des modèles d'analyse flous, simplifiant ainsi le code et améliorant la maintenance [#65](https://github.com/MTES-MCT/dossierfacile-data/issues/65).
