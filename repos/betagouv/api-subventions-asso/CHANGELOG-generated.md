## Changelog : api-subventions-asso (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'import de données de subventions, notamment via l'intégration de sources comme Sirene et RNA Waldec. Des corrections ont également été apportées pour améliorer la stabilité et la fiabilité de l'API, ainsi que la gestion des sessions utilisateurs.

### Évolutions fonctionnelles
- Intégration de l'import des établissements Sirene via une tâche cron automatisée. [#3987](https://github.com/betagouv/api-subventions-asso/issues/3987)
- Import des fichiers RNA Waldec au format Parquet. [#3984](https://github.com/betagouv/api-subventions-asso/issues/3984)
- Amélioration de la détection des fichiers Chorus sur S3. [#3931](https://github.com/betagouv/api-subventions-asso/issues/3931)
- Ajout d'un tag après l'import des données. [#3932](https://github.com/betagouv/api-subventions-asso/issues/3932)
- Suppression du JWT lors de la déconnexion pour une meilleure sécurité. [#1288](https://github.com/betagouv/api-subventions-asso/issues/1288)

### Évolutions techniques
- Intégration complète de Sirene-etablissements. [#3986](https://github.com/betagouv/api-subventions-asso/issues/3986)
- Mise à jour du script de publication pour inclure tous les packages, y compris le package racine.
- Ajout de tests d'intégration pour l'import des établissements Sirene. [#4010](https://github.com/betagouv/api-subventions-asso/issues/4010)
- Mise à jour de l'URL de la source de données Sirene Stock pour utiliser un lien stable. [#3982](https://github.com/betagouv/api-subventions-asso/issues/3982)
- Correction d'un problème lié à la mise à jour de la pipeline dans la migration Chorus.
- Correction d'un bug dans la fonction `getDocuments` de l'adaptateur api-asso.
- Correction d'un problème de test RIDET ou Tahitiet avant de vérifier si une entité est une association.

### Autres changements
- Suppression d'une exclusion d'âge obsolète pour les publications pnpm.
- Regénération du changelog.
- Plusieurs versions intermédiaires ont été publiées (0.84.8, 0.84.9, 0.84.10, 0.84.11, 0.84.12, 0.85.0, 0.85.1) avec des corrections et des améliorations mineures.
