## Changelog : relais (30 derniers jours, au 2026-05-12)

### Résumé
Ce mois-ci, le projet relais a connu une refonte majeure de son infrastructure et de son architecture, passant à Rails 8.1 et intégrant GoodJob pour la gestion des tâches asynchrones.  De nouvelles fonctionnalités ont été ajoutées pour supporter l'intégration avec CNOUS et la gestion de demandes proactives, améliorant ainsi la capacité du service à répondre aux besoins des administrations.

### Évolutions fonctionnelles
- **Intégration CNOUS :** Ajout de l'intégration avec CNOUS, incluant l'authentification OAuth2, le téléchargement de données et le parsing des fichiers CSV avec des protections PII (données personnelles identifiables) [#1](https://github.com/datagouv/relais/pull/1).
- **Demandes proactives :** Implémentation d'un modèle `ProactiviteRequest` et d'une machine d'état pour gérer les demandes proactives [#3](https://github.com/datagouv/relais/pull/3).
- **Stockage de fichiers :** Amélioration du stockage des fichiers avec l'ajout de colonnes `file_bytes` et `file_purged_at` pour une gestion plus flexible des données [#4](https://github.com/datagouv/relais/pull/4).

### Évolutions techniques
- **Mise à jour de Rails :**  Le projet a été mis à jour vers Rails 8.1, offrant les dernières améliorations de performance et de sécurité.
- **Intégration GoodJob :**  GoodJob a été intégré pour la gestion des tâches asynchrones, améliorant la réactivité et la scalabilité du service.
- **Configuration CI/CD :**  Configuration de RSpec, Rubocop et d'un endpoint `/healthz` pour permettre des tests automatisés lors des déploiements.
- **Refactoring de l'architecture :** Refonte de l'architecture du projet pour l'aligner avec apistration.

### Autres changements
- **Documentation :** Mise à jour de la documentation `CLAUDE.md` pour refléter l'état actuel du projet et les nouvelles fonctionnalités [#4](https://github.com/datagouv/relais/pull/4).
- **Nettoyage de code :**  Améliorations générales du code et de la configuration.
