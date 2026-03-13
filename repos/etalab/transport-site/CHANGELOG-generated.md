## Changelog : transport-site (30 derniers jours)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la recherche de jeux de données et de ressources, notamment grâce à l'utilisation de données en mémoire pour une meilleure performance. Des améliorations significatives ont également été apportées au traitement et à la validation des données NeTEx, avec l'ajout de rapports téléchargeables et une meilleure gestion des erreurs. Enfin, des corrections et des améliorations diverses ont été apportées à l'interface utilisateur et à l'infrastructure.

### Évolutions fonctionnelles
- Amélioration de la recherche de jeux de données et de ressources, avec la possibilité de filtrer par sous-type et l'utilisation de données en mémoire pour une meilleure performance. [#5380] [#5340] [#5333]
- Ajout d'une barre de recherche sur les pages de jeux de données et de ressources. [#5380]
- Possibilité de passer le dashboard Metabase en plein écran. [#5399]
- Ajout de la Suisse à la liste des divisions administratives. [#5367]
- Les jeux de données IRVE dédoublonnés sont maintenant disponibles avec des informations supplémentaires. [#5360]
- Téléchargement des rapports de validation NeTEx au format Parquet. [#5375]
- Téléchargement des rapports NeTEx via une modale. [#5419]
- Affichage des métadonnées NeTEx. [#5339]
- Notifications pour les ressources NeTEx expirées. [#5336]
- Correction du tri sur les jeux de données les plus récents dans la recherche. [#5373]

### Évolutions techniques
- Mise à jour de Postgres de la version 14 à 18 et de TimescaleDB à la version 2.23 dans l'environnement CI. [#5027]
- Refactoring et corrections diverses dans le code NeTEx pour améliorer la robustesse et la maintenabilité. [#5344] [#5338]
- Amélioration de la configuration des datasets prioritaires pour le dédoublonnage IRVE, en utilisant un fichier de configuration dédié. [#5409]
- Ajout d'un job pour créer des bases de données Company. [#5423]
- Amélioration de la gestion des erreurs XSD dans le traitement NeTEx, avec regroupement des messages d'erreur. [#5369]
- Stabilisation des tests de navigation. [#5392]
- Montée de version de stylelint de 15 à 17. [#5403]

### Autres changements
- Mise à jour du logo et de la référence textuelle vers "Ministère des Transports". [#5386]
- Page "Nouveautés" mise à jour pour février 2026. [#5381]
- Ajout de documentation pour le test de disponibilité. [#5398]
- Ajout de dashboards Metabase pour les statistiques de la plateforme Public Transit. [#5394] [#5390]
- Correction d'un overflow des titres de ressources. [#5397]
- Amélioration du menu principal. [#5405]
- Correction d'une URL de ressource mal encodée. [#5363]
- Suppression d'un jeu de données Parkings Relais obsolète. [#5417]
- Correction de la localisation manquante. [#5416]
- Dédoublonnage des IRVE : Qualicharge est maintenant prioritaire. [#5414]
- FollowDatasetLive : redirection vers la gestion du JDD concerné. [#5418]
- Validation GTFS-RT : ajout d'un avertissement quand les IDs ne correspondent pas. [#5400]
- Date de dernière historisation : compte dès la première historisation. [#5402]
- Consolidation IRVE : élimination des derniers doublons. [#5365]
