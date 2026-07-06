## Changelog : transports-sanitaires (30 derniers jours, au 3 juillet 2026)

### Résumé
Ce mois-ci, le simulateur d'éligibilité aux transports sanitaires a connu des évolutions importantes, notamment une refonte de l'architecture et de l'intégration des règles métier, ainsi que des améliorations pour faciliter le déploiement et l'utilisation de l'application, y compris via une extension. L'application a également été renommée en "simulateur-eligibilite".

### Évolutions fonctionnelles
- Ajout d'une application d'identification et de réception du contexte pour le simulateur. [#25c5073](https://github.com/betagouv/transports-sanitaires/commit/25c5073)
- Implémentation de nouvelles règles métier pour le simulateur. [#1345b23](https://github.com/betagouv/transports-sanitaires/commit/1345b23)
- Ajout d'un raccourci clavier pour ouvrir la popup du simulateur. [#bddca55](https://github.com/betagouv/transports-sanitaires/commit/bddca55)
- Amélioration de l'accessibilité de la popup avec focus sur l'input lors de l'ouverture. [#61aeb0b](https://github.com/betagouv/transports-sanitaires/commit/61aeb0b)
- Ajout d'une structure parent pour la popup. [#61aeb0b](https://github.com/betagouv/transports-sanitaires/commit/61aeb0b)
- Création d'une extension pour faciliter la recherche du simulateur dans un glossaire. [#0228d61](https://github.com/betagouv/transports-sanitaires/commit/0228d61)
- Publication d'une première version (v1) du simulateur. [#0643c84](https://github.com/betagouv/transports-sanitaires/commit/0643c84) et [#7a4c0f4](https://github.com/betagouv/transports-sanitaires/commit/7a4c0f4)

### Évolutions techniques
- Refactorisation : fusion des règles Publicodes en un seul fichier pour une meilleure organisation. [#7a4c45a](https://github.com/betagouv/transports-sanitaires/commit/7a4c45a)
- Correction d'erreurs TypeScript dans le build. [#baaa902](https://github.com/betagouv/transports-sanitaires/commit/baaa902)
- Adaptation de l'application aux nouvelles règles concernant l'authentification (suppression de l'authentification). [#ce28abd](https://github.com/betagouv/transports-sanitaires/commit/ce28abd) et [#25c5073](https://github.com/betagouv/transports-sanitaires/commit/25c5073)
- Mise en place d'un déploiement via GitHub Pages et correction de problèmes de navigation en mode StrictMode. [#b2818a7](https://github.com/betagouv/transports-sanitaires/commit/b2818a7)
- Renommage de l'application en "simulateur-eligibilite". [#e7ff2ca](https://github.com/betagouv/transports-sanitaires/commit/e7ff2ca)
- Mise à jour des dépendances pour le déploiement avec Scalingo. [#6f031f5](https://github.com/betagouv/transports-sanitaires/commit/6f031f5) et [#0107ecb](https://github.com/betagouv/transports-sanitaires/commit/0107ecb)

### Autres changements
- Documentation : Mise à jour de la documentation AGENTS.md avec la structure du dépôt, les commandes et les conventions. [#fd0dd74](https://github.com/betagouv/transports-sanitaires/commit/fd0dd74)
- Documentation : Ajout de diagrammes d'architecture C4 pour l'identification et l'analyse. [#69b2fd5](https://github.com/betagouv/transports-sanitaires/commit/69b2fd5)
- Documentation : Conversion des diagrammes d'architecture en Mermaid. [#613d36e](https://github.com/betagouv/transports-sanitaires/commit/613d36e)
- Migration vers un nouveau système Notion. [#a2e1678](https://github.com/betagouv/transports-sanitaires/commit/a2e1678)
- Configuration de mise pour Node et Python. [#0f3469d](https://github.com/betagouv/transports-sanitaires/commit/0f3469d)
- Suppression de la version des fichiers `.tsbuildinfo` du suivi Git. [#8b3e1bb](https://github.com/betagouv/transports-sanitaires/commit/8b3e1bb)
- Ajout de tâches pour lancer et installer les applications. [#71b2b22](https://github.com/betagouv/transports-sanitaires/commit/71b2b22)
- Initialisation du dépôt. [#17297f3](https://github.com/betagouv/transports-sanitaires/commit/17297f3)
