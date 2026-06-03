## Changelog : betabot (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de la base de données et de l'indexation pour une recherche plus performante, ainsi que sur la correction de bugs liés à l'affichage des messages et à la gestion des messages directs. Des améliorations de l'infrastructure et de la configuration ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un support pour l'incubateur dans la base de données.
- Ajout d'une commande `curl` pour récupérer le flux vidéo de ruche_numerique. [#issue à ajouter si applicable]
- Amélioration de l'indexation des pages de site pour une recherche plus complète.
- Correction de l'affichage des messages longs dans les *embeds*. [#issue à ajouter si applicable]

### Évolutions techniques
- Ajout de la colonne `created_at` à la base de données.
- Implémentation d'une base de données SQLite pour les requêtes d'agrégation.
- Mise à jour de la version de Node.js à la version 24.
- Amélioration des schémas de la base de données.
- Corrections de bugs liés à la construction de l'image Docker.

### Autres changements
- Mise à jour de la documentation et des spécifications des données.
- Ajout d'instructions pour l'utilisation du bot.
- Diverses corrections de bugs et améliorations de la stabilité.
- Travaux préparatoires (WIP) pour de futures fonctionnalités.
