## Changelog : partageonsleau-orchestration (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, le projet a connu des avancées significatives dans la connexion avec les différentes Plateformes de Données Environnementales (PLE) et l'amélioration de l'infrastructure. L'ajout de connecteurs pour plusieurs PLE (Willie, Olo, Aquasys) permet d'étendre la capacité du système à ingérer des données.  L'orchestration a été dockerisée et une file d'attente BullMQ a été implémentée pour améliorer la gestion des tâches.

### Évolutions fonctionnelles
- Ajout de la connexion avec la PLE : permet l'échange de données avec les plateformes externes. [#5](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/5)
- Implémentation de connecteurs pour les PLE Willie, Olo et Aquasys : permet l'ingestion de données depuis ces sources. [#4](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/4)
- Ajout du `pointId` lors de l'envoi des données au backend : améliore l'identification et le suivi des données. [#6](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/6)
- Mise en place d'une file d'attente BullMQ : améliore la gestion et la fiabilité des tâches asynchrones. [#5](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/5)
- Mise à jour de `last_run_at` à la fin de l'exécution de la tâche : assure un suivi précis des exécutions.

### Évolutions techniques
- Dockerisation de l'application : facilite le déploiement et la reproductibilité de l'environnement. [#1](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/1)
- Ajout d'un fichier `deploy.yml` : automatise le processus de déploiement.
- Configuration des certificats Redis : améliore la sécurité de la connexion à Redis.
- Correction de variables et de secrets : renforce la sécurité et la configuration du projet.
- Refactorisation du code et correction de linting : améliore la qualité et la maintenabilité du code. [#2](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/2), [#3](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/3)
- Modification du port par défaut.

### Autres changements
- Initialisation du projet en TypeScript avec un pipeline connecteur par point.
- Ajout d'une première implémentation Willie en mode incrémental.
- Amélioration de la ressemblance du `template-file` avec Aquasys.
