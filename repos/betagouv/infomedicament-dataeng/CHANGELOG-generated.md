## Changelog : infomedicament-dataeng (30 derniers jours, au 02 mai 2026)

### Résumé
Ce mois-ci, le projet a connu une refonte significative de son infrastructure technique, passant à SQLAlchemy pour la gestion des bases de données et réorganisant la structure du code. De nouvelles fonctionnalités ont été ajoutées pour l'import de données OpenSearch, l'import de données ASMR/SMR depuis data.gouv.fr et la gestion des mises à jour mensuelles des données HTML. L'amélioration de la qualité du code et de la documentation a également été une priorité.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité pour importer les données ASMR/SMR depuis data.gouv.fr [#43ec6bf](https://github.com/betagouv/infomedicament-dataeng/commit/43ec6bf).
- Implémentation d'un workflow pour importer les mises à jour mensuelles des données HTML de manière incrémentale [#efab280](https://github.com/betagouv/infomedicament-dataeng/commit/efab280).
- Ajout d'une commande ETL pour indexer les spécialités dans OpenSearch [#92ef447](https://github.com/betagouv/infomedicament-dataeng/commit/92ef447).
- Préparation de l'infrastructure pour supporter plusieurs index OpenSearch [#b5d7bf2](https://github.com/betagouv/infomedicament-dataeng/commit/b5d7bf2).
- Nettoyage des ancres dans les sections "notice" et "rcp" [#b4b28a1](https://github.com/betagouv/infomedicament-dataeng/commit/b4b28a1).
- Documentation de la procédure d'import des fichiers CSV de présentations dans PostgreSQL [#1299063](https://github.com/betagouv/infomedicament-dataeng/commit/1299063).

### Évolutions techniques
- Remplacement de `psycopg2` et `pymysql` par SQLAlchemy pour une gestion plus flexible et moderne des bases de données [#a2beb83](https://github.com/betagouv/infomedicament-dataeng/commit/a2beb83).
- Refactorisation de la structure du code pour organiser les utilitaires en sous-packages dédiés à chaque cas d'utilisation de l'interface en ligne de commande (CLI) [#895841b](https://github.com/betagouv/infomedicament-dataeng/commit/895841b).
- Ajout de hooks `pre-commit` pour assurer la qualité du code et le formattage automatique [#73dccc6](https://github.com/betagouv/infomedicament-dataeng/commit/73dccc6).
- Intégration de linter et de tests dans le workflow CI/CD [#4a43cee](https://github.com/betagouv/infomedicament-dataeng/commit/4a43cee).
- Correction d'un avertissement de type dans la fonction `sql_to_csv` [#e5b01c3](https://github.com/betagouv/infomedicament-dataeng/commit/e5b01c3).

### Autres changements
- Renommage du projet en `infomedicament-dataeng` [#9ce073a](https://github.com/betagouv/infomedicament-dataeng/commit/9ce073a).
- Refonte de la structure du fichier `README` pour une meilleure présentation du projet [#689c4a4](https://github.com/betagouv/infomedicament-dataeng/commit/689c4a4).
- Mise à jour de la description du projet dans le fichier `README` [#526cf4a](https://github.com/betagouv/infomedicament-dataeng/commit/526cf4a).
- Application de linter et de formatage du code [#8a2cd66](https://github.com/betagouv/infomedicament-dataeng/commit/8a2cd66).
