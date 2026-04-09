## Changelog : dragster (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, dragster a connu des améliorations significatives dans la gestion des compétences (skills) et de l'évaluation des agents, notamment avec l'ajout d'une nouvelle compétence de mémorisation pour le suivi de l'ingestion de documents. Des corrections ont également été apportées à la configuration des tests et de l'intégration continue pour une meilleure stabilité et fiabilité.

### Évolutions fonctionnelles
- Ajout d'une compétence de mémorisation pour suivre l'ingestion de documents ([ed5f6c8](https://github.com/etalab-ia/dragster/commit/ed5f6c8a36898939584041560e219d3ec59c5681)).
- Possibilité d'activer/désactiver les hooks et de configurer le contexte pour la compétence de mémorisation ([28a73c5](https://github.com/etalab-ia/dragster/commit/28a73c511ba5520060f31d7032f560b112e3833b)).
- Réorganisation des compétences avec des métadonnées de fournisseur pour une meilleure organisation ([549e04b](https://github.com/etalab-ia/dragster/commit/549e04bea5f52170ec1f91c19ab7db43856f86d6)).
- Ajout de tests d'évaluation pour la compétence de mémorisation ([cf31e20](https://github.com/etalab-ia/dragster/commit/cf31e205477216f940f6195f9999542417f72620)).

### Évolutions techniques
- Refactorisation du nommage des compétences pour éviter les conflits, en utilisant le préfixe `rag-` ([f2764a8](https://github.com/etalab-ia/dragster/commit/f2764a85445b41747b191515814f88695987976f)).
- Amélioration de la validation des liens symboliques des compétences dans l'environnement CI ([38dc879](https://github.com/etalab-ia/dragster/commit/38dc879f9f55337ba82241b7004cf9c5d2418b82)).
- Mise à jour de la configuration de l'intégration continue pour utiliser `letta_code` pour les évaluations ([4247209](https://github.com/etalab-ia/dragster/commit/42472097f17119456842499078719166f346051f)).
- Simplification des liens symboliques des compétences pour une meilleure gestion ([5a42c74](https://github.com/etalab-ia/dragster/commit/5a42c7466f71485f3997836852961416324978d9)).
- Utilisation de liens symboliques individuels pour chaque compétence au lieu d'un lien vers l'ensemble du répertoire ([f454f37](https://github.com/etalab-ia/dragster/commit/f454f3797884caa9224dd0bab7a415b848c40b42)).

### Autres changements
- Ajout d'un logo ASCII art au fichier README ([408e0d6](https://github.com/etalab-ia/dragster/commit/408e0d64910f666808953636a77a555060496f23)).
- Ajout de badges de statut, de licence et de version au fichier README ([9b90e12](https://github.com/etalab-ia/dragster/commit/9b90e12393644b850466480a14460a2973f97d79)).
- Mise en place d'un workflow `release-please` pour la gestion automatisée des versions ([0924bfd](https://github.com/etalab-ia/dragster/commit/0924bfd6618377118a4d19263f69f84834c6876f)).
- Correction de la configuration du hook `worktrunk` ([8d6a953](https://github.com/etalab-ia/dragster/commit/8d6a953ee3e5fedd40ee39ecefbf1914da7fd466)).
- Alignement des titres des compétences avec les noms des frontmatter ([e20d3a3](https://github.com/etalab-ia/dragster/commit/e20d3a31998926489394634747f493376166541c)).
- Suppression de l'évaluateur `response_quality` qui nécessitait une clé OpenAI ([014de29](https://github.com/etalab-ia/dragster/commit/014de299860358497834938406944425439b476a)).
