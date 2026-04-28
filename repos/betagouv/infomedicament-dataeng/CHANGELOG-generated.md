## Changelog : infomedicament-dataeng (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la recherche sémantique des notices, l'optimisation du traitement des données pédiatriques et la modernisation de l'accès aux bases de données. Une première implémentation de l'import de datapackages a également été réalisée.

### Évolutions fonctionnelles
- **Recherche sémantique :** Implémentation d'une première version de la recherche sémantique sur les notices, utilisant des embeddings vectoriels générés via l'API Albert. Les notices sont segmentées en "chunks" pour permettre une meilleure recherche.
- **Import de données :** Ajout d'une preuve de concept pour l'import de données via le format datapackage. [#issue à créer]
- **Classification pédiatrique :** Récupération des données RCP (Résumé des Caractéristiques du Produit) depuis S3 pour la classification pédiatrique.

### Évolutions techniques
- **Base de données :** Remplacement des bibliothèques `psycopg2` et `pymysql` par SQLAlchemy pour une gestion plus flexible et moderne des connexions aux bases de données. [#issue à créer]
- **Optimisation pédiatrique :** Optimisation du traitement des données pédiatriques pour éviter les erreurs de mémoire (OOM - Out Of Memory) en traitant les données par lots.
- **Refactoring :** Réorganisation du code source en sous-packages, un par cas d'utilisation de l'interface en ligne de commande (CLI).
- **Robustesse :** Ajout de `tenacity` pour gérer les erreurs temporaires lors de la génération des embeddings.

### Autres changements
- **Correction :** Correction d'un avertissement de type dans la fonction `sql_to_csv`.
- **Amélioration :** Correction d'un problème où le titre de niveau 1 était incorrectement ignoré lors de la génération des embeddings.
