## Changelog : quefairedemesobjets (30 derniers jours, au 04/08/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'expérience utilisateur sur mobile, la fiabilisation des processus de traitement des données (notamment pour les datasets de la BAN et le clustering) et l'optimisation de l'environnement de développement pour garantir une meilleure qualité de code.

### Évolutions fonctionnelles
- **Amélioration de l'interface** : L'affichage de l'infotri est désormais responsive, offrant une meilleure expérience sur les petits écrans [#3179](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3179).
- **Ajustements des données et filtres** : 
    - Suppression du filtrage des établissements basé sur un code étranger [#3216](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3216).
    - Amélioration de la gestion des identifiants nuls pour la CMA [#3253](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3253).

### Évolutions techniques
- **Optimisation des pipelines de données** :
    - Intégration de la récupération des paramètres du DAG de clustering via API [#3246](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3246).
    - Ajout d'un paramètre de correction pour les datasets de la BAN [#3199](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3199).
    - Optimisation de la copie des tables en limitant la récupération des colonnes au schéma public uniquement [#3215](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3215).
- **Infrastructure et outils de développement** :
    - Amélioration de la qualité du code SQL avec l'ajout de `sqlfluff` sur la plateforme de données [#3190](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3190).
    - Correction de la gestion des dépendances suite au passage aux workspaces `uv` [#3239](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3239).
    - Fiabilisation de la recréation de la base de données de prévisualisation [#3254](https://github.com/incubateur-ademe/quefairedemesobjets/pull/3254).
