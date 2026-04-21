## Changelog : csplab (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'ingestion et du traitement des données, notamment des offres d'emploi et des CV. Des améliorations significatives ont été apportées à la recherche de candidatures, à l'accessibilité et à l'expérience utilisateur globale. Des refactorings importants ont également eu lieu pour préparer le terrain à de futures évolutions et optimisations.

### Évolutions fonctionnelles
- **Candidatures :**
    - Ajout de filtres avancés pour affiner la recherche de CV correspondant aux opportunités [#355](https://github.com/betagouv/csplab/issues/355).
    - Amélioration de l'ouverture du tiroir de résultats après application de filtres [#374](https://github.com/betagouv/csplab/issues/374).
    - Intégration de Matomo pour le suivi analytique du parcours candidat [#358](https://github.com/betagouv/csplab/issues/358).
    - Ajout d'une fonctionnalité de chargement progressif des résultats pour une meilleure expérience utilisateur [#352](https://github.com/betagouv/csplab/issues/352).
    - Ajout d'une région live pour annoncer les résultats aux lecteurs d'écran, améliorant l'accessibilité [#353](https://github.com/betagouv/csplab/issues/353).
- **Ingestion :**
    - Mise en place d'une ingestion asynchrone des offres d'emploi détaillées [#342](https://github.com/betagouv/csplab/issues/342).
    - Implémentation de la récupération d'informations détaillées depuis Talentsoft [#344](https://github.com/betagouv/csplab/issues/344).
    - Ajout de la possibilité de rechercher des documents bruts par identifiants externes [#345](https://github.com/betagouv/csplab/issues/345).
    - Mapping des catégories aux offres d'emploi [#362](https://github.com/betagouv/csplab/issues/362).
    - Suppression de la limite de tokens pour l'expérimentation des CV [#341](https://github.com/betagouv/csplab/issues/341).
- **OCR :** Implémentation de l'OCR souverain [#332](https://github.com/betagouv/csplab/issues/332).

### Évolutions techniques
- **Architecture :**
    - Suppression du modèle `VectorizedDocumentModel` et du dépôt `pgvector_repository` [#385](https://github.com/betagouv/csplab/issues/385).
    - Suppression de l'intégration Elasticsearch (ES) [#370](https://github.com/betagouv/csplab/issues/370).
    - Refactorisation de la vue des résultats CV en use case et presenter [#361](https://github.com/betagouv/csplab/issues/361).
- **Infrastructure :**
    - Utilisation d'un client HTTP asynchrone pour l'ingestion [#389](https://github.com/betagouv/csplab/issues/389).
    - Mise en place d'une file d'attente et d'un broker pour les tâches asynchrones [#376](https://github.com/betagouv/csplab/issues/376).
    - Ajout de la possibilité de remplacer le port par défaut [#391](https://github.com/betagouv/csplab/issues/391).
    - Désactivation des tâches périodiques en environnement de développement [#390](https://github.com/betagouv/csplab/issues/390).
- **Tests :** Ajout de tests d'accessibilité automatisés avec pytest-playwright et axe-playwright-python [#157](https://github.com/betagouv/csplab/issues/157).
- **Divers :**
    - Mise à jour des dépendances OCR et Tycho [#383](https://github.com/betagouv/csplab/issues/383), [#382](https://github.com/betagouv/csplab/issues/382), [#363](https://github.com/betagouv/csplab/issues/363).
    - Mise en file d'attente des tâches périodiques de vectorisation et de nettoyage [#381](https://github.com/betagouv/csplab/issues/381).
    - Correction d'un bug dans la tâche de chargement des offres [#393](https://github.com/betagouv/csplab/issues/393).

### Autres changements
- Mise à jour du CHANGELOG.md pour les versions 0.1.6 et 0.1.5 [#338](https://github.com/betagouv/csplab/issues/338), [#290](https://github.com/betagouv/csplab/issues/290).
- Mise à jour de la liste des scopes suggérés lors de la création de commits [#337](https://github.com/betagouv/csplab/issues/337).
- Correction de la position et du bouton de fermeture des alertes toast [#354](https://github.com/betagouv/csplab/issues/354).
- Correction d'un problème de gestion des statics en développement [#360](https://github.com/betagouv/csplab/issues/360).
- Ajout de documentation sur la stratégie de tests [#317](https://github.com/betagouv/csplab/issues/317).
