## Changelog : csplab (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'ingestion et du traitement des offres d'emploi, notamment en intégrant un nouveau service OCR pour l'extraction de texte, et en préparant l'utilisation de vecteurs pour la recherche sémantique. Des améliorations significatives ont également été apportées à l'interface utilisateur, en particulier pour la recherche de candidats et l'accessibilité.

### Évolutions fonctionnelles
- Ajout de filtres avancés pour la recherche de candidats et l'appariement CV/opportunités [#355](https://github.com/betagouv/csplab/issues/355).
- Intégration de Matomo pour le suivi analytique du parcours candidat [#358](https://github.com/betagouv/csplab/issues/358).
- Amélioration de l'expérience utilisateur avec l'ajout de régions "live" pour les lecteurs d'écran [#353](https://github.com/betagouv/csplab/issues/353) et des indicateurs de chargement [#352](https://github.com/betagouv/csplab/issues/352).
- Implémentation d'un service OCR pour l'extraction de texte à partir de documents [#332](https://github.com/betagouv/csplab/issues/332) et [#327](https://github.com/betagouv/csplab/issues/327).
- Possibilité de mapper les catégories aux offres [#362](https://github.com/betagouv/csplab/issues/362).
- Ajout de la possibilité de charger des offres détaillées [#342](https://github.com/betagouv/csplab/issues/342).
- Suppression des contraintes sur le nombre de tokens pour l'expérimentation des CV [#341](https://github.com/betagouv/csplab/issues/341).

### Évolutions techniques
- Mise en place d'une architecture asynchrone avec un broker et une queue pour la vectorisation et le nettoyage des documents [#381](https://github.com/betagouv/csplab/issues/381) et [#376](https://github.com/betagouv/csplab/issues/376).
- Remplacement de pgvector par Qdrant pour la gestion des vecteurs [#385](https://github.com/betagouv/csplab/issues/385) et [#316](https://github.com/betagouv/csplab/issues/316).
- Refactorisation de la vue des résultats CV en "use case" et "presenter" [#361](https://github.com/betagouv/csplab/issues/361).
- Suppression de l'utilisation d'Elasticsearch [#370](https://github.com/betagouv/csplab/issues/370).
- Amélioration de la résilience du traitement par lots des documents [#329](https://github.com/betagouv/csplab/issues/329).
- Ajout de tests d'accessibilité automatisés avec pytest-playwright et axe-playwright-python [#157](https://github.com/betagouv/csplab/issues/157).
- Mise à jour des dépendances (OCR, Tycho, httpx) [#383](https://github.com/betagouv/csplab/issues/383), [#382](https://github.com/betagouv/csplab/issues/382), [#363](https://github.com/betagouv/csplab/issues/363), [#326](https://github.com/betagouv/csplab/issues/326), [#325](https://github.com/betagouv/csplab/issues/325).
- Ajout de routes privées avec authentification pour le service OCR [#322](https://github.com/betagouv/csplab/issues/322).
- Intégration de Sentry pour la gestion des erreurs dans le service OCR [#324](https://github.com/betagouv/csplab/issues/324).

### Autres changements
- Mise à jour de la documentation CHANGELOG.md pour les versions 0.1.6 et 0.1.5 [#338](https://github.com/betagouv/csplab/issues/338) et [#290](https://github.com/betagouv/csplab/issues/290).
- Amélioration de la gestion des commits avec une liste de scopes suggérés [#337](https://github.com/betagouv/csplab/issues/337).
- Correction de bugs mineurs liés à l'affichage et au fonctionnement de l'interface utilisateur [#374](https://github.com/betagouv/csplab/issues/374), [#360](https://github.com/betagouv/csplab/issues/360), [#354](https://github.com/betagouv/csplab/issues/354).
- Correction d'un problème de dates lors de l'insertion/mise à jour de documents [#287](https://github.com/betagouv/csplab/issues/287).
- Ajout d'un override de port pour le projet [#391](https://github.com/betagouv/csplab/issues/391).
- Désactivation des tâches périodiques en environnement de développement [#390](https://github.com/betagouv/csplab/issues/390).
- Utilisation d'un client HTTP asynchrone pour l'ingestion [#389](https://github.com/betagouv/csplab/issues/389).
- Correction d'un bug dans la tâche d'ingestion [#393](https://github.com/betagouv/csplab/issues/393).
