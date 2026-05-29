## Changelog : csplab (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'ingestion des données, notamment via l'ajout de support pour les webhooks Talensoft et l'amélioration de la gestion des sources de données. L'interface utilisateur a également bénéficié d'améliorations, avec l'ajout de pages statiques (mentions légales, confidentialité, accessibilité) et l'implémentation de tests E2E pour le parcours d'analyse de CV.

### Évolutions fonctionnelles
- Ajout de la prise en charge des webhooks Talensoft pour l'ingestion des offres d'emploi [#592](https://github.com/betagouv/csplab/issues/592).
- Implémentation d'un endpoint pour lister les métiers [#569](https://github.com/betagouv/csplab/issues/569).
- Ajout de pages statiques pour les mentions légales, la politique de confidentialité et l'accessibilité [#225](https://github.com/betagouv/csplab/issues/225), [#226](https://github.com/betagouv/csplab/issues/226), [#224](https://github.com/betagouv/csplab/issues/224).
- Possibilité d'archiver des offres via des webhooks [#512](https://github.com/betagouv/csplab/issues/512).
- Le filtre de catégorie inclut désormais la catégorie A+ [#482](https://github.com/betagouv/csplab/issues/482).
- Ajout de la possibilité de récupérer le détail d'une opportunité avec les métiers associés [#487](https://github.com/betagouv/csplab/issues/487).
- Ajout d'un endpoint pour lister les offres [#440](https://github.com/betagouv/csplab/issues/440).

### Évolutions techniques
- Refonte de l'architecture frontend avec l'initialisation de Storybook [#596](https://github.com/betagouv/csplab/issues/596).
- Amélioration de la gestion des variables d'environnement pour Talensoft [#600](https://github.com/betagouv/csplab/issues/600).
- Création d'énums pour les webhooks Talensoft [#607](https://github.com/betagouv/csplab/issues/607).
- Refactorisation du code pour préparer l'endpoint de liste des métiers [#603](https://github.com/betagouv/csplab/issues/603).
- Mise en place de tests E2E avec Playwright pour le parcours d'analyse de CV [#490](https://github.com/betagouv/csplab/issues/490).
- Amélioration de la gestion des connexions des threads worker dans les tests [#478](https://github.com/betagouv/csplab/issues/478).
- Standardisation des noms de méthodes pour les opérations de récupération (get_xxxx) [#568](https://github.com/betagouv/csplab/issues/568).
- Refactorisation des tests et des fixtures dans le module Tycho [#467](https://github.com/betagouv/csplab/issues/467).
- Ajout de la gestion de `relativedelta` pour l'archivage des offres [#477](https://github.com/betagouv/csplab/issues/477).
- Utilisation de `SettingsConfigDict` pour remplacer la configuration Pydantic obsolète [#489](https://github.com/betagouv/csplab/issues/489).
- Ajout d'un mécanisme de logging [#578](https://github.com/betagouv/csplab/issues/578).
- Amélioration de la robustesse du mapping des ministères [#548](https://github.com/betagouv/csplab/issues/548).

### Autres changements
- Ajout d'une tâche pour linter le schéma dans le workflow de linting [#608](https://github.com/betagouv/csplab/issues/608).
- Ajout d'un workflow GitHub Actions pour l'attribution automatique [#606](https://github.com/betagouv/csplab/issues/606).
- Documentation de l'architecture frontend et des conventions [#595](https://github.com/betagouv/csplab/issues/595).
- Comparaison des référentiels DILA et Talensoft pour les organismes [#601](https://github.com/betagouv/csplab/issues/601).
- Ajout d'une entité Source et d'une API pour lister les sources [#574](https://github.com/betagouv/csplab/issues/574).
- Mise à jour de la documentation d'installation pour les hooks Git [#472](https://github.com/betagouv/csplab/issues/472).
- Amélioration de la documentation de l'endpoint API [#480](https://github.com/betagouv/csplab/issues/480).
- Mise à jour des dépendances (notebook, ocr, tycho) [#497](https://github.com/betagouv/csplab/issues/497), [#496](https://github.com/betagouv/csplab/issues/496), [#495](https://github.com/betagouv/csplab/issues/495), [#571](https://github.com/betagouv/csplab/issues/571), [#570](https://github.com/betagouv/csplab/issues/570).
- Ajout de test de couverture de code [#498](https://github.com/betagouv/csplab/issues/498).
- Mise à jour du CHANGELOG.md pour les versions 0.1.9 et 0.1.8 [#485](https://github.com/betagouv/csplab/issues/485), [#418](https://github.com/betagouv/csplab/issues/418).
