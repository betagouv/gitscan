## Changelog : monitor-field (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'infrastructure de construction et de test de l'application, ainsi que sur l'implémentation initiale de la fonctionnalité d'affichage des zones réglementaires de pêche. Des améliorations ont également été apportées à la recherche et au stockage des données.

### Évolutions fonctionnelles
- Implémentation initiale de l'affichage des zones réglementaires de pêche [#1](https://github.com/MTES-MCT/monitor-field/pull/1).
- Ajout de la possibilité de rechercher par zone [#20](https://github.com/MTES-MCT/monitor-field/pull/20).
- Affichage d'une liste des zones réglementaires de pêche [#23](https://github.com/MTES-MCT/monitor-field/pull/23).
- Ajout de boutons dans la barre inférieure pour faciliter l'accès aux fonctionnalités de recherche [#24](https://github.com/MTES-MCT/monitor-field/pull/24).
- Possibilité de sauvegarder les données au format GeoJSON dans la base de données [#19](https://github.com/MTES-MCT/monitor-field/pull/19).

### Évolutions techniques
- Mise en place d'un workflow de construction pour le développement avec EAS [#22](https://github.com/MTES-MCT/monitor-field/pull/22), [#25](https://github.com/MTES-MCT/monitor-field/pull/25).
- Configuration de workflows CI/CD pour la construction et le déploiement de l'application [#26](https://github.com/MTES-MCT/monitor-field/pull/26).
- Mise à jour de la configuration de SonarQube et ajout de Codecov pour l'analyse de la qualité du code [#19](https://github.com/MTES-MCT/monitor-field/pull/19).
- Migration de ESLint vers Oxlint pour un linting plus performant [#19](https://github.com/MTES-MCT/monitor-field/pull/19).
- Mise à jour des versions de Node et des dépendances du projet [#19](https://github.com/MTES-MCT/monitor-field/pull/19).
- Correction de la configuration de Jest pour les tests unitaires [#19](https://github.com/MTES-MCT/monitor-field/pull/19).
- Mise à jour du slug de l'application Expo [#20](https://github.com/MTES-MCT/monitor-field/pull/20).

### Autres changements
- Mise à jour de la documentation et du fichier README [#12](https://github.com/MTES-MCT/monitor-field/pull/20).
- Renommage de `reglementations` en `regulations` pour une meilleure cohérence [#1](https://github.com/MTES-MCT/monitor-field/pull/1).
- Modifications diverses suite aux revues de code [#7](https://github.com/MTES-MCT/monitor-field/pull/7).
- Ajout du dossier `coverage` au fichier `.gitignore`.
- Correction de l'importation de modules.
