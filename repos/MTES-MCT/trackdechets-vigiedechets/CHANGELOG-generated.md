## Changelog : trackdechets-vigiedechets (30 derniers jours, au 01 juin 2026)

### Résumé
Cette version apporte des améliorations à la fonctionnalité de contact (ajout de pièces jointes multiples), permet l'utilisation locale de ClickHouse pour le data warehouse, et inclut des corrections suite à des mises à jour de dépendances. Des optimisations et corrections mineures ont également été apportées à la génération de registres.

### Évolutions fonctionnelles
- **Formulaire de contact :** Possibilité de joindre plusieurs fichiers au formulaire de contact de la FAQ/assistance. [#476](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/476)
- **Data Warehouse :** Possibilité d'utiliser ClickHouse en local pour le data warehouse. [#464](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/464)

### Évolutions techniques
- **Dépendances :** Mise à jour de plusieurs dépendances du projet.
- **Génération de registres :** Passage à l'utilisation de `generateRegistryV2ExportAsAdmin` pour la génération des registres, avec corrections associées.
- **Tests :** Corrections et mises à jour des tests.

### Autres changements
- Correction de bugs suite à la montée de version des dépendances. [#490](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/490)
- Amélioration de la gestion des espaces dans les chaînes de caractères lors de la génération de registres.
- Corrections mineures et ajustements divers.
