## Changelog : partageonsleau-orchestration (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, l'orchestrateur Partageons l'Eau a connu des avancées significatives en termes de connectivité aux sources de données. L'ajout de connecteurs pour Olo et Aquasys, ainsi que des améliorations sur le connecteur Willie, permettent d'ingérer des données depuis davantage de sources. Le projet a également été dockerisé pour faciliter le déploiement et la reproductibilité.

### Évolutions fonctionnelles
- Ajout de connecteurs pour les sources de données Olo et Aquasys [#4](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/4).
- Implémentation d'une connexion de base au backend pour le connecteur template-file [#6](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/6).
- Préparation du flux PLE avec un compte de service et un token déclarant.
- Mise à jour de la date de dernière exécution (`last_run_at`) à la fin du traitement.

### Évolutions techniques
- Dockerisation de l'application pour simplifier le déploiement et assurer la cohérence de l'environnement [#1](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/1).
- Corrections et améliorations du linter xo [#2](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/2) et [#3](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/3).
- Refonte du template-file pour ressembler à Aquasys [#6](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/6).

### Autres changements
- Initialisation du projet avec un pipeline connecteur par point (service account -> contexte -> connecteur -> ingestion) et une première implémentation Willie en mode incrémental.
- Ajout de l'ID de point (`pointId`) à envoyer au backend [#6](https://github.com/MTES-MCT/partageonsleau-orchestration/pull/6).
- Tests du flux avec la connexion au backend.
