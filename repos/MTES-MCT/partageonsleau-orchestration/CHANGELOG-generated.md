## Changelog : partageonsleau-orchestration (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, l'orchestrateur Partageons l'Eau a connu des avancées significatives en termes d'intégration de sources de données et de préparation pour la connexion à la plateforme PLE. L'ajout de connecteurs pour plusieurs sources (Willie, Olo, Aquasys) et l'implémentation d'une file d'attente de tâches (BullMQ) permettent une ingestion plus robuste et scalable des données. Le projet a également été dockerisé pour faciliter le déploiement et la reproductibilité.

### Évolutions fonctionnelles
- Ajout de connecteurs pour les sources de données Willie, Olo et Aquasys, permettant l'ingestion de données depuis ces sources vers Partageons l'Eau. [#4](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/4)
- Préparation de l'intégration avec la plateforme Partageons l'Eau (PLE) en utilisant un compte de service et un token de déclarant. [#6](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/6)
- Implémentation d'un connecteur de base pour la source de données template-file.
- Mise en place d'un mécanisme pour mettre à jour la date de dernière exécution (`last_run_at`) à la fin de chaque tâche.

### Évolutions techniques
- Dockerisation de l'application pour faciliter le déploiement et la reproductibilité. [#1](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/1)
- Intégration de la librairie BullMQ pour la gestion des tâches en file d'attente, améliorant la robustesse et la scalabilité de l'orchestrateur. [#5](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/5)
- Correction de problèmes de linting avec xo. [#2](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/2) et [#3](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/3)
- Amélioration de la structure du code et correction de bugs mineurs liés à TypeScript.

### Autres changements
- Initialisation du projet avec un pipeline connecteur par point (compte de service -> contexte -> connecteur -> ingestion) et une première implémentation Willie en mode incrémental.
- Ajout du `pointId` pour l'envoi à la plateforme backend.
