## Changelog : csplab (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'ingestion et du traitement des offres d'emploi, ainsi que sur l'expérience candidat. Des tests automatisés de bout en bout ont été ajoutés pour garantir la qualité, et des optimisations ont été apportées à l'infrastructure et aux performances. L'archivage des offres est désormais possible.

### Évolutions fonctionnelles
- Possibilité d'archiver des offres via la commande `load_offers` [#455](https://github.com/betagouv/csplab/issues/455).
- Amélioration du filtre de catégories de candidatures pour inclure la catégorie A+ [#482](https://github.com/betagouv/csplab/issues/482).
- Affichage de l'organisation ou du ministère sur les cartes et les tiroirs d'opportunités [#443](https://github.com/betagouv/csplab/issues/443).
- Amélioration de l'expérience utilisateur pour la présentation des CV, notamment la navigation au clavier et la fermeture des tiroirs modaux [#460](https://github.com/betagouv/csplab/issues/460), [#461](https://github.com/betagouv/csplab/issues/461), [#463](https://github.com/betagouv/csplab/issues/463), [#444](https://github.com/betagouv/csplab/issues/444), [#441](https://github.com/betagouv/csplab/issues/441).
- Correction d'un bug empêchant les documents ayant échoué d'être retraités [#452](https://github.com/betagouv/csplab/issues/452).

### Évolutions techniques
- Ajout d'une suite de tests E2E avec Playwright pour améliorer la couverture des tests et la stabilité de l'application [#490](https://github.com/betagouv/csplab/issues/490).
- Refactorisation de l'infrastructure d'ingestion pour utiliser `python-dateutil` pour une meilleure gestion des dates [#477](https://github.com/betagouv/csplab/issues/477).
- Mise en place d'une documentation API plus complète [#480](https://github.com/betagouv/csplab/issues/480).
- Utilisation de clients HTTP asynchrones pour améliorer les performances de l'ingestion [#389](https://github.com/betagouv/csplab/issues/389).
- Suppression de l'utilisation de `pgvector` et refactorisation du code associé [#385](https://github.com/betagouv/csplab/issues/385).
- Mise en place d'une file d'attente de tâches (broker) pour gérer les tâches asynchrones telles que le traitement des CV et la vectorisation [#376](https://github.com/betagouv/csplab/issues/376).
- Amélioration de la configuration et de la gestion des dépendances.
- Homogénéisation des tests et refactorisation des factories et fixtures dans Tycho [#467](https://github.com/betagouv/csplab/issues/467).
- Remplacement de Pydantic Config déprécié par SettingsConfigDict [#489](https://github.com/betagouv/csplab/issues/489).

### Autres changements
- Mise à jour de la documentation d'installation pour inclure les hooks Git [#472](https://github.com/betagouv/csplab/issues/472).
- Amélioration de la journalisation (logging) pour faciliter le débogage [#412](https://github.com/betagouv/csplab/issues/412).
- Mise à jour de la documentation des commandes de chargement [#481](https://github.com/betagouv/csplab/issues/481).
- Correction de problèmes de configuration et de chemins d'accès pour l'environnement de développement [#399](https://github.com/betagouv/csplab/issues/399), [#439](https://github.com/betagouv/csplab/issues/439).
- Mise à jour des dépendances du projet.
- Amélioration de la configuration des tâches périodiques en mode développement [#483](https://github.com/betagouv/csplab/issues/483).
- Ajout de la possibilité de surcharger les ports en configuration [#391](https://github.com/betagouv/csplab/issues/391).
- Ajout d'un template de commit optionnel [#417](https://github.com/betagouv/csplab/issues/417).
