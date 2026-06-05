## Changelog : betabot (30 derniers jours, au 04 juin 2026)

### Résumé
Ce mois-ci, les améliorations apportées à betabot se concentrent sur l'enrichissement des sources de données, l'amélioration de la qualité des réponses et la correction de plusieurs problèmes liés à l'intégration avec Matrix et à l'exécution du bot en conteneur Docker. Des efforts ont également été faits pour faciliter l'installation et la configuration du bot.

### Évolutions fonctionnelles
- Ajout de l'indexation des pages de site web pour améliorer la recherche d'informations.
- Intégration de nouvelles sources de documentation : DSFR, FranceConnect et Proconnect.
- Ajout d'une base de données SQLite pour des requêtes d'agrégation plus performantes.
- Ajout d'une fonctionnalité pour récupérer le flux vidéo de ruche_numerique via une commande curl.
- Ajout d'une base de données pour l'incubateur [#1234](https://github.com/betagouv/betabot/issues/1234).
- Amélioration de la gestion des messages directs (DM) dans Matrix, avec correction de plusieurs bugs associés.
- Correction d'un problème d'affichage des embeds pour les textes longs.

### Évolutions techniques
- Mise à jour de la version de Node.js vers la version 24.
- Amélioration des schémas de base de données pour une meilleure cohérence des données.
- Correction de plusieurs problèmes liés à l'exécution du bot en conteneur Docker.
- Optimisation de l'utilisation des threads pour éviter les problèmes en conversations individuelles.
- Ajout de champs `created_at` aux données pour faciliter le suivi de la création des entrées.
- Correction de bugs liés à l'envoi d'URLs dans le contexte de "wttj".
- Amélioration de la gestion des URLs dans la documentation.

### Autres changements
- Ajout d'instructions pour l'installation et la configuration du bot.
- Mise à jour de la documentation et des spécifications des données.
- Nettoyage du code et suppression de code inutilisé.
- Ajout de tests d'évaluation pour le routage des outils.
