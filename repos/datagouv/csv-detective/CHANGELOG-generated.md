## Changelog : csv-detective (30 derniers jours, au 12 mai 2026)

### Résumé
Les récentes mises à jour de csv-detective se concentrent sur la correction de bugs et l'amélioration de la robustesse du processus de validation des données. Une correction importante assure que la validation échoue si une erreur survient lors du chargement des données par blocs, garantissant ainsi une meilleure intégrité des résultats. Des améliorations de linting et l'ajout de tests associés contribuent également à la qualité du code.

### Évolutions fonctionnelles
- Correction d'un bug : la validation échoue désormais si une erreur se produit lors du chargement des données par blocs, empêchant ainsi l'utilisation de résultats incomplets ou erronés. [#251](https://github.com/datagouv/csv-detective/issues/251)

### Évolutions techniques
- Amélioration de la qualité du code via des corrections de linting.
- Ajout de tests unitaires pour renforcer la couverture et la fiabilité du code.

### Autres changements
- Mise à jour de la dépendance `urllib3`. [#251](https://github.com/datagouv/csv-detective/issues/251)
