## Changelog : csplab (30 derniers jours, au 02 juin 2026)

### Résumé
Ce mois-ci, les évolutions de csplab se concentrent sur l'amélioration de l'ingestion des offres d'emploi, notamment via l'ajout de support pour les webhooks Talensoft et l'archivage des offres. L'authentification par email/mot de passe est désormais fonctionnelle. Des améliorations significatives ont également été apportées à l'interface utilisateur, avec l'ajout de tests E2E et de pages statiques importantes comme la politique de confidentialité et les mentions légales.

### Évolutions fonctionnelles
- **Authentification:** Mise en place de l'authentification par email et mot de passe pour les utilisateurs [#639](https://github.com/betagouv/csplab/issues/639).
- **Ingestion des offres:** Ajout de la prise en charge des webhooks Talensoft pour l'importation des offres [#500](https://github.com/betagouv/csplab/issues/500).
- **Archivage des offres:** Implémentation de la fonctionnalité d'archivage des offres [#455](https://github.com/betagouv/csplab/issues/455).
- **Recherche d'opportunités:** Ajout des métiers dans le cas d'utilisation de mise en relation CV/opportunités [#637](https://github.com/betagouv/csplab/issues/637).
- **Interface utilisateur:** Ajout des pages statiques "Mentions légales", "Politique de confidentialité" et "Accessibilité" [#224](https://github.com/betagouv/csplab/issues/224), [#225](https://github.com/betagouv/csplab/issues/225), [#226](https://github.com/betagouv/csplab/issues/226).
- **Gestion des erreurs Frontend:** Interception et gestion des erreurs au niveau du frontend [#629](https://github.com/betagouv/csplab/issues/629).
- **API:** Exposition d'un endpoint pour lister les offres [#440](https://github.com/betagouv/csplab/issues/440) et un endpoint pour importer les offres [#547](https://github.com/betagouv/csplab/issues/547).
- **ATS Domain:** Ajout de l'organisme dans le contexte identité [#624](https://github.com/betagouv/csplab/issues/624).

### Évolutions techniques
- **Infrastructure:** Amélioration de la gestion des sources d'offres avec l'ajout d'une entité `Source` et d'une API associée [#574](https://github.com/betagouv/csplab/issues/574).
- **Base de données:** Migration vers un modèle utilisateur personnalisé [#614](https://github.com/betagouv/csplab/issues/614), [#616](https://github.com/betagouv/csplab/issues/616), [#632](https://github.com/betagouv/csplab/issues/632).
- **Tests:** Mise en place d'une suite de tests E2E avec Playwright pour l'interface utilisateur [#490](https://github.com/betagouv/csplab/issues/490).
- **CI/CD:** Ajout d'une tâche pour l'analyse statique du code avec `djlint` [#584](https://github.com/betagouv/csplab/issues/584) et une workflow pour publier Storybook [#647](https://github.com/betagouv/csplab/issues/647).
- **Refactoring:** Refactorisation du code pour préparer l'exposition de l'endpoint de liste des métiers [#603](https://github.com/betagouv/csplab/issues/603).
- **Logging:** Mise en place d'un mécanisme de logging plus robuste [#578](https://github.com/betagouv/csplab/issues/578).
- **Dépendances:** Mise à jour de certaines dépendances (notebook, ocr, tycho) [#497](https://github.com/betagouv/csplab/issues/497), [#496](https://github.com/betagouv/csplab/issues/496), [#495](https://github.com/betagouv/csplab/issues/495).

### Autres changements
- **Documentation:** Traduction du template de Pull Request en français [#619](https://github.com/betagouv/csplab/issues/619).
- **Configuration:** Mise à jour des instructions d'installation pour les Git hooks [#472](https://github.com/betagouv/csplab/issues/472).
- **Notebook:** Exploration de Rome 4 pour la vectorisation des métiers [#507](https://github.com/betagouv/csplab/issues/507).
- **Tooling:** Amélioration de la configuration ESLint et VSCode [#612](https://github.com/betagouv/csplab/issues/612).
- **Nettoyage de code:** Suppression de tests View remplacés par des tests E2E [#462](https://github.com/betagouv/csplab/issues/462).
