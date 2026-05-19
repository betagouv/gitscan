## Changelog : csplab (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, l'équipe a continué à améliorer l'ingestion et le traitement des offres d'emploi, notamment avec l'ajout de la vectorisation pour la recherche de métiers et la gestion des webhooks pour l'archivage des offres. Des améliorations significatives ont également été apportées à l'interface utilisateur, avec l'ajout de pages statiques (mentions légales, confidentialité, accessibilité) et l'amélioration de l'expérience utilisateur pour l'analyse de CV. Enfin, des efforts ont été déployés pour améliorer la robustesse et la documentation du code.

### Évolutions fonctionnelles
- Ajout de la vectorisation pour la recherche de métiers lors de l'ingestion des offres ([#551](https://github.com/betagouv/csplab/issues/551)).
- Affichage des offres d'emploi dans le tiroir (drawer) de présentation des candidats ([#550](https://github.com/betagouv/csplab/issues/550)).
- Ajout de pages statiques pour les mentions légales ([#225](https://github.com/betagouv/csplab/issues/225)), la politique de confidentialité ([#226](https://github.com/betagouv/csplab/issues/226)) et l'accessibilité ([#224](https://github.com/betagouv/csplab/issues/224)).
- Ajout de la possibilité de fermer le tiroir (drawer) modal de CV en utilisant la navigation du navigateur ([#444](https://github.com/betagouv/csplab/issues/444)).
- Affichage de l'organisation ou du ministère dans les cartes et le tiroir des opportunités ([#443](https://github.com/betagouv/csplab/issues/443)).
- Amélioration de l'affichage des filtres actifs sur la page de recherche ([#380](https://github.com/betagouv/csplab/issues/380)).
- Ajout de la possibilité d'archiver les offres via des webhooks ([#512](https://github.com/betagouv/csplab/issues/512)).
- Ajout d'un endpoint API pour lister les offres ([#440](https://github.com/betagouv/csplab/issues/440)).
- Gestion de la catégorie A+ lors du filtrage des offres ([#482](https://github.com/betagouv/csplab/issues/482)).

### Évolutions techniques
- Refactorisation de l'API et des tests pour une meilleure organisation et maintenabilité.
- Amélioration de la robustesse de la cartographie des ministères lors de l'ingestion ([#548](https://github.com/betagouv/csplab/issues/548)).
- Renommage de colonnes pour le ConcoursCleaner ([#511](https://github.com/betagouv/csplab/issues/511)).
- Mise à jour de la documentation OpenAPI ([#546](https://github.com/betagouv/csplab/issues/546)).
- Refactorisation de l'OfferFactory ([#514](https://github.com/betagouv/csplab/issues/514)).
- Ajout d'un usecase pour récupérer le détail d'une opportunité avec les métiers ([#487](https://github.com/betagouv/csplab/issues/487)).
- Isolation et journalisation des documents bruts en cas d'erreur lors de l'ingestion ([#509](https://github.com/betagouv/csplab/issues/509)).
- Mise en place d'un nouveau processus d'ingestion ([#493](https://github.com/betagouv/csplab/issues/493)).
- Amélioration de la gestion des connexions aux bases de données dans les tests.
- Suppression de la librairie pgvector.
- Passage à des loggers pour une meilleure gestion des logs ([#413](https://github.com/betagouv/csplab/issues/413)).
- Amélioration des tests et de la couverture de code.
- Mise à jour des dépendances (pypdf, python-dateutil).

### Autres changements
- Documentation de l'utilisation des webhooks Talentsoft ([#503](https://github.com/betagouv/csplab/issues/503)).
- Mise à jour des instructions d'installation pour les hooks Git ([#472](https://github.com/betagouv/csplab/issues/472)).
- Ajout de tests E2E avec Playwright pour l'analyse de CV ([#490](https://github.com/betagouv/csplab/issues/490)).
- Ajout d'une tâche pour nettoyer les métiers ([#414](https://github.com/betagouv/csplab/issues/414)).
- Amélioration de la configuration et de l'environnement de développement.
- Mise à jour du CHANGELOG.md ([#418](https://github.com/betagouv/csplab/issues/418), [#375](https://github.com/betagouv/csplab/issues/375)).
