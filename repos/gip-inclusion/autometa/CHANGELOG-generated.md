## Changelog : autometa (30 derniers jours, au 29 octobre 2026)

### Résumé
Ce mois-ci, autometa a franchi une étape importante dans sa capacité d'analyse en intégrant de nouvelles sources de données (Airtable, Mon Récap) et en rendant la recherche beaucoup plus intuitive grâce à une compréhension sémantique des requêtes. Le système est devenu plus robuste et fiable, notamment grâce à une meilleure gestion des erreurs de connexion et une automatisation accrue des environnements de test.

### Évolutions fonctionnelles
- **Recherche et filtrage améliorés** : introduction de la recherche par sens (embeddings), nouveaux filtres par auteur et interface de recherche regroupée pour une navigation plus fluide.
- **Nouvelles sources de données** : ajout du support pour Airtable en lecture seule [#249] et intégration de la base applicative Mon Récap [#250].
- **Gestion des tableaux de bord** : support des tableaux de bord multi-sources, gestion des variantes et de l'obfuscation des données, et vérification automatique de la qualité visuelle avant le partage de liens [#230].
- **Zendesk** : nouvelles capacités de lecture et d'édition des macros avec suivi des modifications.
- **Interface utilisateur** : affichage des résultats SQL [#235] et épinglage du guide de données dans la navigation [#234].

### Évolutions techniques
- **Résilience et fiabilité** : renforcement de la gestion des timeouts Redis et amélioration de la stabilité du moteur d'exécution (runner) pour mieux supporter les interruptions de service.
- **Infrastructure et CI/CD** : optimisation de la taille de l'image de déploiement Scalingo [#266], amélioration des tâches planifiées (Crons) avec récapitulatifs Slack [#257, #236] et renforcement de la sécurité (CSP/S3) [#256].
- **Expérience de développement** : automatisation complète du cycle de vie des environnements de test (review apps) avec un système de préparation (seeding) et de purge automatique pour garantir des données de démonstration toujours propres.
- **Performance** : accélération des tests unitaires grâce à l'exécution en parallèle avec `pytest-xdist`.
- **Architecture** : refonte de la lecture des données [#267] et amélioration du contrat de la façade logicielle [#259].

### Autres changements
- **Documentation** : mise à jour des guides concernant les tableaux de bord multi-sources, l'obfuscation et l'utilisation des variantes.
- **Nettoyage** : suppression de la connexion automatique à Sentry [#264] et retrait du scraping RPE [#237].
