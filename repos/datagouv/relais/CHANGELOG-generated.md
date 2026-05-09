## Changelog : relais (30 derniers jours, au 7 mai 2026)

### Résumé
Le projet relais a connu une refonte significative de son infrastructure et de sa configuration.  Une nouvelle base de code, alignée sur le projet `apistration`, a été initialisée avec Rails 8.1.  Des outils de test et de linting ont été intégrés pour améliorer la qualité du code et faciliter les déploiements. La documentation a également été mise à jour pour refléter ces changements.

### Évolutions techniques
- Initialisation d'un squelette Rails 8.1 aligné avec `apistration` [ff8278b](https://github.com/datagouv/relais/commit/ff8278b)
- Configuration de GoodJob pour la gestion des tâches asynchrones et documentation du processus de démarrage [895ea57](https://github.com/datagouv/relais/commit/895ea57)
- Intégration de RSpec, Rubocop et d'un endpoint `/healthz` pour les tests et la vérification de l'état de l'application lors des déploiements [01e4282](https://github.com/datagouv/relais/commit/01e4282)
- Réalignement de la documentation `CLAUDE.md` avec l'état actuel du projet et de l'API [9425745](https://github.com/datagouv/relais/commit/9425745)
- Réalignement du squelette du projet en fonction de la portée de l'API [9c306e0](https://github.com/datagouv/relais/commit/9c306e0)
- Initialisation du fichier `claude.md` [5844c4e](https://github.com/datagouv/relais/commit/5844c4e)
