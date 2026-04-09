## Changelog : csplab (30 derniers jours, au 09 avril 2026)

### Résumé
Ce mois-ci, csplab a connu des améliorations significatives dans l'ingestion de données, l'OCR (reconnaissance optique de caractères) et l'expérience utilisateur, notamment pour la fonctionnalité de recherche de candidatures (tycho). L'accessibilité a également été renforcée avec l'ajout de tests automatisés et des améliorations pour les utilisateurs ayant des besoins spécifiques.

### Évolutions fonctionnelles
- **Ingestion de données :**
    - Ajout de la capacité de charger des offres d'emploi détaillées. [#342](https://github.com/betagouv/csplab/issues/342)
    - Amélioration de la résilience du processus de nettoyage des documents lors de l'ingestion. [#329](https://github.com/betagouv/csplab/issues/329)
    - Mise en place d'un mapping des catégories vers les offres. [#362](https://github.com/betagouv/csplab/issues/362)
- **Recherche de candidatures (tycho) :**
    - Ajout de filtres avancés pour affiner la recherche de CV. [#357](https://github.com/betagouv/csplab/issues/357)
    - Intégration de Qdrant comme base de données vectorielle pour améliorer la pertinence des correspondances CV/opportunités. [#316](https://github.com/betagouv/csplab/issues/316)
    - Ajout d'analytics Matomo pour suivre le parcours des candidats. [#358](https://github.com/betagouv/csplab/issues/358)
    - Amélioration de l'expérience utilisateur avec des indicateurs de chargement, des alertes et des régions "live" pour les lecteurs d'écran. [#352](https://github.com/betagouv/csplab/issues/352), [#353](https://github.com/betagouv/csplab/issues/353), [#354](https://github.com/betagouv/csplab/issues/354), [#310](https://github.com/betagouv/csplab/issues/310)
    - Ajout de liens de navigation rapide pour l'accessibilité. [#311](https://github.com/betagouv/csplab/issues/311)
    - Implémentation de la pagination et de la gestion des paramètres de filtre dans l'URL. [#274](https://github.com/betagouv/csplab/issues/274)
- **OCR :**
    - Initialisation du service OCR avec des routes privées et authentifiées. [#319](https://github.com/betagouv/csplab/issues/319)
    - Implémentation de l'OCR souverain. [#332](https://github.com/betagouv/csplab/issues/332)
    - Ajout de l'extraction de texte. [#327](https://github.com/betagouv/csplab/issues/327)
    - Envoi des erreurs OCR à Sentry pour le suivi. [#324](https://github.com/betagouv/csplab/issues/324)

### Évolutions techniques
- **Tests :** Ajout de tests d'accessibilité automatisés avec pytest-playwright et axe-playwright-python. [#157](https://github.com/betagouv/csplab/issues/157)
- **Refactoring :** Refactorisation de la vue des résultats de CV pour une meilleure organisation du code. [#361](https://github.com/betagouv/csplab/issues/361)
- **Dépendances :** Mise à jour des dépendances du projet (tycho-ocr et toutes). [#363](https://github.com/betagouv/csplab/issues/363), [#326](https://github.com/betagouv/csplab/issues/326)
- **Tooling :** Amélioration de la gestion des statics en développement. [#360](https://github.com/betagouv/csplab/issues/360)
- **CI/CD :** Correction du CI pour Qdrant. [#356](https://github.com/betagouv/csplab/issues/356)
- **Suppression :** Suppression du service Elasticsearch (ES). [#370](https://github.com/betagouv/csplab/issues/370)

### Autres changements
- Mise à jour de la documentation (template des issues GitHub). [#305](https://github.com/betagouv/csplab/issues/305)
- Mise à jour du CHANGELOG.md pour les versions 0.1.6 et 0.1.5. [#338](https://github.com/betagouv/csplab/issues/338), [#290](https://github.com/betagouv/csplab/issues/290)
- Ajout de tooltips pour les champs de filtre. [#276](https://github.com/betagouv/csplab/issues/276)
- Amélioration des meta tags. [#308](https://github.com/betagouv/csplab/issues/308)
- Ajout d'une assertion sur le scoring. [#281](https://github.com/betagouv/csplab/issues/281)
- Correction de la gestion des dates et heures lors de l'upsert des RawDocument et Offer. [#287](https://github.com/betagouv/csplab/issues/287)
- Ajout de la possibilité d'utiliser `httpx` pour `sentry_sdk`. [#325](https://github.com/betagouv/csplab/issues/325)
- Suppression de la contrainte du nombre maximal de tokens pour l'expérimentation de CV. [#341](https://github.com/betagouv/csplab/issues/341)
- Ajout de popper-utils pour scalingo. [#330](https://github.com/betagouv/csplab/issues/330)
- Ajout d'auto-reload et de l'intégration django-browser-reload en développement. [#277](https://github.com/betagouv/csplab/issues/277)
- Correction de l'ouverture du drawer après filtrage. [#374](https://github.com/betagouv/csplab/issues/374)
