## Changelog : betabot (30 derniers jours, au 30 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'enrichissement des données indexées par le bot, notamment avec l'ajout des incubateurs et des pages de site, ainsi que sur la résolution de plusieurs problèmes liés à l'affichage des messages et au fonctionnement des messages directs. Des optimisations techniques ont également été apportées pour améliorer la robustesse et la performance du bot.

### Évolutions fonctionnelles
- Ajout de l'indexation des incubateurs, permettant au bot de répondre aux questions les concernant.
- Ajout de l'indexation des pages de site, élargissant ainsi le champ des connaissances du bot.
- Amélioration de l'affichage des messages longs dans les *embeds* pour éviter les erreurs.
- Ajout d'une commande `curl` pour récupérer le flux vidéo de ruche_numerique. [#issue à ajouter si applicable]
- Corrections de bugs concernant les messages directs (DM), améliorant leur fiabilité.

### Évolutions techniques
- Mise en place d'une base de données SQLite pour les requêtes d'agrégation, optimisant ainsi les performances.
- Amélioration des schémas de base de données pour une meilleure organisation et efficacité.
- Mise à jour de la version de Node.js vers la version 24.
- Refonte de la gestion des threads et des feedbacks.
- Diverses corrections de build et de configuration Docker.

### Autres changements
- Mise à jour de la documentation concernant les spécifications et les données indexées.
- Ajout d'instructions pour faciliter l'utilisation du bot.
- Nettoyage et refactoring du code pour une meilleure maintenabilité.
