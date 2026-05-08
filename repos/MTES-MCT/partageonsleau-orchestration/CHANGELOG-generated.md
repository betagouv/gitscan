## Changelog : partageonsleau-orchestration (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, l'orchestrateur a connu des améliorations significatives en termes de connectivité avec la plateforme Partageons l'Eau (PLE), d'ajout de connecteurs pour différents services (Willie, Olo, Aquasys) et de gestion des tâches avec l'intégration de BullMQ. Des efforts ont également été faits pour améliorer la robustesse du projet avec l'ajout d'un pipeline CI/CD et la gestion des certificats Redis.

### Évolutions fonctionnelles
- Ajout de la connexion avec la plateforme Partageons l'Eau (PLE) [#4f0833c](https://github.com/MTES-MCT/partageonsleau-orchestration/pulls/4f0833c).
- Implémentation de connecteurs pour les services Willie, Olo et Aquasys, permettant l'ingestion de données depuis ces sources [#47f9e84](https://github.com/MTES-MCT/partageonsleau-orchestration/pulls/47f9e84).
- Gestion des conflits lors de la déclaration de données [#c8b8e6d](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/c8b8e6d).
- Prise en charge de plusieurs fichiers lors de l'ingestion de données [#839cde6](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/839cde6).
- Amélioration du calcul des volumes à partir des index pour Willie [#c7808ee](https://github.com/MTES-MCT/partageonsleau-orchestration/pulls/c7808ee).
- Ajout d'un identifiant de point (pointId) pour la communication avec le backend [#b127da1](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/b127da1).

### Évolutions techniques
- Intégration de BullMQ pour la gestion des tâches et des queues [#b035b16](https://github.com/MTES-MCT/partageonsleau-orchestration/pulls/b035b16).
- Dockerisation de l'application pour faciliter le déploiement et la reproductibilité [#843be4d](https://github.com/MTES-MCT/partageonsleau-orchestration/pulls/843be4d).
- Mise en place d'un pipeline CI/CD avec `deploy.yml` pour l'automatisation des déploiements [#b958131](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/b958131).
- Configuration de certificats Redis pour une connexion sécurisée [#89588b3](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/89588b3).
- Utilisation de `ioredis` pour une meilleure gestion de la connexion Redis.
- Mise à jour de la configuration des variables et des secrets.

### Autres changements
- Ajout d'une documentation pour le projet [#c26d011](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/c26d011).
- Mise à jour du fichier README pour refléter les dernières évolutions [#bb1c66e](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/bb1c66e).
- Corrections de linting et de style de code [#2b9a2e6](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/2b9a2e6), [#49c06af](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/49c06af).
- Correction d'une politique "no conflict" [#0ec8ed5](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/0ec8ed5).
- Modification du port par défaut.
- Ajout d'un administrateur BullMQ pour la supervision des queues [#b5ba1d1](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/b5ba1d1).
