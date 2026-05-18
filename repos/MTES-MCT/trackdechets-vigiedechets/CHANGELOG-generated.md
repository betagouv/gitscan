## Changelog : trackdechets-vigiedechets (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité (limitation des tentatives de réinitialisation de mot de passe), l'ajout de nouvelles fonctionnalités pour l'export de registres (par SIREN ou SIRET) et des corrections pour assurer la stabilité de l'application. Des améliorations ont également été apportées à la gestion de l'environnement de test avec MinIO.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les registres par SIREN ou SIRET. [#469](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/469)
- Limitation du nombre de tentatives de réinitialisation de mot de passe pour renforcer la sécurité. [#472](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/472)
- Ajout d'un message d'aide dynamique pour le type de registre. [#463](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/463)
- Correction du format du SIRET lors d'une mutation.
- Correction d'un espace dans une chaîne de caractères lors de la génération d'un export de registre.

### Évolutions techniques
- Mise à jour de l'image MinIO utilisée dans les workflows de test. [#473](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/473)
- Amélioration du processus de téléchargement du client MinIO.
- Passage à l'utilisation de `generateRegistryV2ExportAsAdmin` pour la génération d'exports de registre.
- Correction de tests suite à des modifications de code.
- Correction de dépendances et mise à jour des packages.

### Autres changements
- Correction suite à la montée de version des dépendances. [#490](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/490)
- Mise à jour des fichiers de verrouillage des dépendances.
- Reformattage des tests `accounts/test_view`.
