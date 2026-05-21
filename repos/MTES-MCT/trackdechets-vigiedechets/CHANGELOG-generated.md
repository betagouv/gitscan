## Changelog : trackdechets-vigiedechets (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité (limitation des tentatives de réinitialisation de mot de passe), l'ajout de nouvelles fonctionnalités pour l'export des registres (par SIRET ou SIREN) et l'amélioration de l'infrastructure avec la possibilité d'utiliser ClickHouse en local. Des corrections et des mises à jour de dépendances ont également été effectuées.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les registres par SIRET ou SIREN. [#469](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/469)
- Ajout d'un message d'aide dynamique pour le type de registre. [#463](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/463)
- Limitation du nombre de tentatives de réinitialisation de mot de passe pour renforcer la sécurité. [#472](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/472)
- Possibilité d'utiliser ClickHouse en local pour le data warehouse. [#464](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/464)

### Évolutions techniques
- Mise à jour de l'image MinIO dans les workflows CI/CD pour bénéficier des dernières corrections et améliorations. [#473](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/473)
- Amélioration du processus de téléchargement du client MinIO.
- Refactoring du code de test pour les comptes utilisateurs.
- Utilisation de `generateRegistryV2ExportAsAdmin` pour la génération des exports.
- Formatage du code avec `ruff`.
- Correction de problèmes liés aux versions des dépendances. [#490](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/490)

### Autres changements
- Correction de l'espace dans une chaîne de caractères pour `generateRegistryV2ExportAsAdmin`.
- Correction du format du SIRET dans une mutation.
- Mise à jour des packages de dépendances.
- Correction de tests.
