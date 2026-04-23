## Changelog : csplab (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'ingestion et le traitement des données, notamment des CV et des offres d'emploi, avec un accent particulier sur l'optimisation des performances et la suppression de dépendances obsolètes. Des améliorations significatives ont également été apportées à l'expérience utilisateur, notamment en matière d'accessibilité et d'analyse des données.

### Évolutions fonctionnelles
- Amélioration du filtrage des CV pour une meilleure correspondance avec les opportunités [#355](https://github.com/betagouv/csplab/issues/355).
- Ajout d'analyses Matomo pour suivre le parcours des candidats [#358](https://github.com/betagouv/csplab/issues/358).
- Implémentation de l'OCR souverain [#332](https://github.com/betagouv/csplab/issues/332).
- Possibilité de charger les données métiers (métiers) pour l'ingestion [#414](https://github.com/betagouv/csplab/issues/414) et [#398](https://github.com/betagouv/csplab/issues/398).
- Amélioration de l'ouverture du tiroir après filtrage des candidats [#374](https://github.com/betagouv/csplab/issues/374).
- Ajout de la possibilité d'envoyer le traitement des CVs uploadés à un broker de tâches [#377](https://github.com/betagouv/csplab/issues/377).
- Ajout de filtres avancés pour affiner la recherche de CVs [#357](https://github.com/betagouv/csplab/issues/357).

### Évolutions techniques
- Suppression de la bibliothèque pgvector et du modèle `VectorizedDocumentModel` [#386](https://github.com/betagouv/csplab/issues/386) et [#385](https://github.com/betagouv/csplab/issues/385).
- Suppression de l'index Elasticsearch [#370](https://github.com/betagouv/csplab/issues/370).
- Mise en place d'une file d'attente asynchrone pour la vectorisation et le nettoyage des documents [#381](https://github.com/betagouv/csplab/issues/381) et [#376](https://github.com/betagouv/csplab/issues/376).
- Refactorisation de la vue des résultats du CV en "use case" et "presenter" [#361](https://github.com/betagouv/csplab/issues/361).
- Utilisation d'un client HTTP asynchrone pour l'ingestion [#389](https://github.com/betagouv/csplab/issues/389).
- Mise à jour de pypdf pour des raisons de sécurité [#401](https://github.com/betagouv/csplab/issues/401) et [#402](https://github.com/betagouv/csplab/issues/402).
- Correction pour permettre le bon fonctionnement du bootstrap sur une installation propre [#399](https://github.com/betagouv/csplab/issues/399).
- Suppression de la gestion de l'ingestion des offres au sein de `load_documents` [#350](https://github.com/betagouv/csplab/issues/350).

### Autres changements
- Ajout de tests d'accessibilité automatisés avec pytest-playwright et axe-playwright-python [#157](https://github.com/betagouv/csplab/issues/157).
- Améliorations de l'interface utilisateur : ajout de régions live pour les lecteurs d'écran, amélioration du positionnement des alertes toast et ajout d'une opacité de chargement [#353](https://github.com/betagouv/csplab/issues/353), [#354](https://github.com/betagouv/csplab/issues/354) et [#352](https://github.com/betagouv/csplab/issues/352).
- Ajout d'une option pour surcharger le port [#391](https://github.com/betagouv/csplab/issues/391).
- Ajout d'une couche optionnelle dans les modèles de commit [#417](https://github.com/betagouv/csplab/issues/417).
- Mise à jour de la documentation du CHANGELOG pour les versions 0.1.6 et 0.1.7.
- Correction d'un bug lié aux contraintes de tokens maximum pour l'expérimentation des CVs [#341](https://github.com/betagouv/csplab/issues/341).
- Mise à jour de la liste des scopes suggérés lors du commit [#337](https://github.com/betagouv/csplab/issues/337).
- Corrections de bugs et améliorations diverses.
