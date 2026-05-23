## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, le projet a connu des améliorations significatives en matière de gestion des collections de documents, de sécurité et d'indexation. De nouvelles fonctionnalités permettent de créer des collections à partir de différents types de documents, d'indexer des documents distants et maîtrisés, et de gérer plus finement les accès via des tokens JWT. Des corrections de sécurité et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'une route `/api/collections/` pour créer une nouvelle collection à partir de différents types de documents (maîtrisés, distants, etc.). [#83a9f80](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/83a9f80)
- Possibilité de nommer la collection lors de sa création. [#4cc551d](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/4cc551d)
- Implémentation de la gestion des documents maîtrisés (questions/réponses) et possibilité de les ajouter à une collection. [#ff400c9](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/ff400c9)
- Ajout d'une route `/api/documents` pour l'indexation de documents. [#a59d534](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/a59d534)
- Possibilité de modifier les documents déjà indexés. [#e14abbc](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/e14abbc)
- Ajout d'une route `/evaluation` pour l'évaluation des documents via un VLM (Vision Language Model) et Docling. [#53b8f3a](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/53b8f3a)
- Amélioration du prompt pour interdire les questions relatives aux Rx. [#b83f216](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/b83f216)
- Ajout d'un script pour générer des tokens JWT. [#e7e9dfe](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/e7e9dfe)

### Évolutions techniques
- Sécurisation de toutes les routes avec authentification JWT. [#972d73b](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/972d73b)
- Refactorisation du service d'indexation. [#d482b79](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/d482b79)
- Suppression de l'indexeur Albert. [#6358a5a](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/6358a5a)
- Utilisation de tâches en arrière-plan pour l'indexation et l'évaluation afin d'améliorer la performance. [#d0a1b78](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/d0a1b78), [#b98730a](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/b98730a)
- Déploiement en production automatisé via une GitHub Action. [#eb7c387](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/eb7c387)
- Amélioration de la configuration Docker pour éviter d'embarquer tous les fichiers du projet dans l'image. [#be6498e](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/be6498e)
- Correction d'alertes de sécurité Dependabot de haute sévérité. [#f8ce26d](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/f8ce26d)

### Autres changements
- Ajout de logs lors de l'indexation. [#37e3b35](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/37e3b35)
- Suppression de fichiers JSON obsolètes. [#b46b016](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/b46b016)
- Correction de la CI pour MQC. [#32034cf](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/32034cf)
- Ajout de documentation. [#0a63179](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/0a63179)
- Configuration du logger. [#8d8db2e](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/8d8db2e)
- Ajout d'un fichier de configuration minimal pour Renovate. [#4e0b91d](https://github.com/betagouv/anssi-recommandations-cyber-data/pulls/4e0b91d)
