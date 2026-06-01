## Changelog : csplab (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'ingestion de données, notamment avec l'ajout de la gestion des webhooks Talensoft et l'archivage des offres. Des améliorations significatives ont également été apportées à l'interface utilisateur, avec l'ajout de tests E2E pour le parcours candidat et l'ajout de pages statiques importantes comme la politique de confidentialité et les mentions légales. Enfin, des optimisations et des corrections de bugs ont été réalisées dans l'ensemble du projet.

### Évolutions fonctionnelles
- **Ingestion :** Ajout de la prise en charge des webhooks Talensoft pour la réception des offres d'emploi. [#592](https://github.com/betagouv/csplab/issues/592)
- **Ingestion :** Possibilité d'archiver des offres d'emploi. [#455](https://github.com/betagouv/csplab/issues/455)
- **Interface candidat :** Ajout de pages statiques pour les mentions légales, la politique de confidentialité et l'accessibilité. [#225](https://github.com/betagouv/csplab/issues/225), [#226](https://github.com/betagouv/csplab/issues/226), [#224](https://github.com/betagouv/csplab/issues/224)
- **Recherche :** Intégration de la catégorie A+ dans le filtre de recherche. [#482](https://github.com/betagouv/csplab/issues/482)
- **API :** Exposition d'un endpoint pour lister les métiers. [#569](https://github.com/betagouv/csplab/issues/569)
- **API :** Ajout d'un endpoint pour lister les offres. [#440](https://github.com/betagouv/csplab/issues/440)
- **Authentification :** Authentification des requêtes Vue Django. [#613](https://github.com/betagouv/csplab/issues/613)

### Évolutions techniques
- **Tests :** Mise en place d'une suite de tests E2E avec Playwright pour le parcours candidat. [#490](https://github.com/betagouv/csplab/issues/490)
- **CI/CD :** Ajout d'un workflow GitHub Actions pour l'auto-assignation des PR. [#606](https://github.com/betagouv/csplab/issues/606)
- **Architecture :** Refonte de l'architecture frontend avec Storybook pour l'ATS. [#596](https://github.com/betagouv/csplab/issues/596)
- **Ingestion :** Création d'une nouvelle application d'ingestion pour une meilleure organisation. [#493](https://github.com/betagouv/csplab/issues/493)
- **Ingestion :** Utilisation d'enums pour les webhooks Talensoft. [#607](https://github.com/betagouv/csplab/issues/607)
- **Ingestion :** Création d'un client Talensoft partagé. [#599](https://github.com/betagouv/csplab/issues/599)
- **Ingestion :** Amélioration de la gestion des erreurs lors du chargement des documents. [#509](https://github.com/betagouv/csplab/issues/509)
- **Ingestion :**  Standardisation des noms de méthodes (get_xxxx). [#568](https://github.com/betagouv/csplab/issues/568)
- **OCR :** Mise à jour des dépendances. [#496](https://github.com/betagouv/csplab/issues/496)
- **Notebook :** Mise à jour des dépendances. [#497](https://github.com/betagouv/csplab/issues/497)
- **Typage :** Remplacement de `Config` Pydantic déprécié par `SettingsConfigDict`. [#489](https://github.com/betagouv/csplab/issues/489)

### Autres changements
- **Documentation :** Traduction du template de PR en français. [#619](https://github.com/betagouv/csplab/issues/619)
- **Documentation :** Documentation de l'architecture et des conventions du frontend. [#595](https://github.com/betagouv/csplab/issues/595)
- **Documentation :** Mise à jour des instructions d'installation pour les Git hooks. [#472](https://github.com/betagouv/csplab/issues/472)
- **Configuration :** Amélioration de la gestion des variables d'environnement pour Talensoft. [#600](https://github.com/betagouv/csplab/issues/600)
- **Linting :** Ajout d'une tâche pour linter le schéma. [#608](https://github.com/betagouv/csplab/issues/608)
- **Linting :** Ajout de djlint dans la CI. [#584](https://github.com/betagouv/csplab/issues/584)
- **Tests :** Ajout de test d'accessibilité pour le parcours candidat. [#464](https://github.com/betagouv/csplab/issues/464)
- **Refactoring :** Divers refactorings pour améliorer la qualité du code et la maintenabilité.
- **Correction de bugs :** Correction de plusieurs bugs mineurs dans l'ensemble du projet.
