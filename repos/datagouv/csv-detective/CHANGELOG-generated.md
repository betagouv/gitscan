## Changelog : csv-detective (30 derniers jours, au 24 juin 2026)

### Résumé
Les récentes mises à jour de csv-detective améliorent la capacité du logiciel à analyser différents types de fichiers, notamment les fichiers Parquet, et à détecter plus précisément les types de données dans les colonnes. Des améliorations ont également été apportées à la gestion des valeurs manquantes et à la correction de certains formats de données. Enfin, des corrections mineures ont été effectuées pour améliorer la qualité du code et le processus de CI/CD.

### Évolutions fonctionnelles
- Ajout de la prise en charge de l'analyse des fichiers Parquet [#253](https://github.com/datagouv/csv-detective/pull/253).
- Possibilité de spécifier des valeurs NaN supplémentaires pour une meilleure détection des données manquantes [#255](https://github.com/datagouv/csv-detective/pull/255).
- Ajout de la liste des valeurs uniques pour les colonnes catégorielles (simples et multiples) [#250](https://github.com/datagouv/csv-detective/pull/250).
- Renommage du format `booleen` en `bool` pour une meilleure cohérence [#252](https://github.com/datagouv/csv-detective/pull/252).

### Évolutions techniques
- Correction d'un problème de détection des valeurs uniques dans les colonnes trop complexes [#257](https://github.com/datagouv/csv-detective/pull/257).
- Correction des erreurs de linting et amélioration du processus de vérification du lint dans le CI [#254](https://github.com/datagouv/csv-detective/pull/254).
- Utilisation d'un token UV pour la publication, améliorant la sécurité et l'automatisation du processus de publication [#256](https://github.com/datagouv/csv-detective/pull/256).

### Autres changements
- Aucune documentation ou configuration n'a été modifiée dans cette version.
