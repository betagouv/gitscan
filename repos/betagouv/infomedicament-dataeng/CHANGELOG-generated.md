## Changelog : infomedicament-dataeng (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la recherche sémantique des notices, l'optimisation du traitement des données pédiatriques et la modernisation de l'accès aux bases de données. Des expérimentations sont également en cours pour importer des données via des datapackages.

### Évolutions fonctionnelles
- **Recherche sémantique :** Implémentation d'une première version de la recherche sémantique sur les notices, utilisant des embeddings vectoriels générés via l'API Albert. Cela permettra une recherche plus pertinente et basée sur le sens des termes.
- **Classification pédiatrique :** Amélioration de la performance du module de classification pédiatrique en traitant les données par lots pour éviter les erreurs de mémoire insuffisante (OOM).
- **Import de données :** Début d'une implémentation pour importer des données au format datapackage [#issue à ajouter si applicable].

### Évolutions techniques
- **Base de données :** Remplacement des bibliothèques `psycopg2` et `pymysql` par SQLAlchemy pour une gestion plus flexible et moderne des connexions aux bases de données.
- **Refactoring du code :** Réorganisation du code source en sous-packages, un par cas d'utilisation de l'interface en ligne de commande (CLI), pour une meilleure modularité et maintenabilité.
- **Optimisation des embeddings :** Utilisation de la bibliothèque `tenacity` pour gérer les erreurs lors de la génération des embeddings et correction d'un problème de saut de titre de niveau 1.
- **Accès S3 :** Modification de la politique du bucket S3 pour une meilleure gestion des accès.
- **Récupération des données RCP :** Implémentation de la récupération des données RCP (Résumé des Caractéristiques du Produit) depuis S3.

### Autres changements
- Correction d'un avertissement de type dans la fonction `sql_to_csv`.
