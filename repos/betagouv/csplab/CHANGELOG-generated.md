## Changelog : csplab (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'ingestion et du traitement des données, notamment des offres d'emploi, ainsi que sur l'expérience utilisateur de la recherche de candidatures. Des améliorations significatives ont été apportées à l'accessibilité et à la performance, avec l'ajout de tests automatisés d'accessibilité et l'optimisation de certains processus. La suppression de composants obsolètes et la modernisation des dépendances contribuent également à la stabilité et à la maintenabilité du projet.

### Évolutions fonctionnelles
- Ajout de l'intégration avec Talentsoft pour l'ingestion de données d'offres d'emploi [#425](https://github.com/betagouv/csplab/issues/425).
- Implémentation de filtres avancés pour la recherche de candidatures et la mise en relation avec les opportunités [#355](https://github.com/betagouv/csplab/issues/355) et [#357](https://github.com/betagouv/csplab/issues/357).
- Amélioration de l'affichage des résultats de recherche de CV avec une refactorisation vers une approche "use case + presenter" [#361](https://github.com/betagouv/csplab/issues/361).
- Ajout d'analytics Matomo pour suivre le parcours des candidats [#358](https://github.com/betagouv/csplab/issues/358).
- Ajout d'une fonctionnalité permettant de charger les données des métiers [#397](https://github.com/betagouv/csplab/issues/397).
- Possibilité de supprimer les documents du repository vectoriel [#421](https://github.com/betagouv/csplab/issues/421).
- Amélioration de l'ouverture du tiroir de filtres après application des filtres [#374](https://github.com/betagouv/csplab/issues/374).
- Ajout de tests automatisés d'accessibilité avec pytest-playwright et axe-playwright-python [#157](https://github.com/betagouv/csplab/issues/157).

### Évolutions techniques
- Refactorisation de la journalisation (logging) pour utiliser l'interpolation de chaînes paresseuses, améliorant ainsi les performances [#412](https://github.com/betagouv/csplab/issues/412).
- Suppression de la bibliothèque pgvector et des modèles associés, simplifiant ainsi l'architecture [#386](https://github.com/betagouv/csplab/issues/386) et [#385](https://github.com/betagouv/csplab/issues/385).
- Mise à jour des dépendances pypdf dans les modules ocr et notebook pour corriger des failles de sécurité [#401](https://github.com/betagouv/csplab/issues/401) et [#402](https://github.com/betagouv/csplab/issues/402).
- Utilisation d'un client HTTP asynchrone dans l'ingestion pour améliorer la performance [#389](https://github.com/betagouv/csplab/issues/389).
- Suppression de l'intégration Elasticsearch (ES) [#370](https://github.com/betagouv/csplab/issues/370).
- Mise en place d'une file d'attente pour les tâches de vectorisation et de nettoyage [#381](https://github.com/betagouv/csplab/issues/381).
- Ajout d'un broker et d'une queue pour les tâches asynchrones [#376](https://github.com/betagouv/csplab/issues/376).

### Autres changements
- Correction du chemin de l'interpréteur Python dans VS Code [#439](https://github.com/betagouv/csplab/issues/439).
- Ajout d'une commande `make run-mvp` pour lancer tous les services MVP en une seule fois [#420](https://github.com/betagouv/csplab/issues/420).
- Suppression d'une fonctionnalité de recherche de corps de texte inutilisée [#437](https://github.com/betagouv/csplab/issues/437).
- Ajout d'une couche optionnelle dans les modèles de commit [#417](https://github.com/betagouv/csplab/issues/417).
- Correction de problèmes de configuration pour le bootstrap [#399](https://github.com/betagouv/csplab/issues/399).
- Ajout d'une option pour overrider le port des services [#391](https://github.com/betagouv/csplab/issues/391).
- Correction de la gestion des statics en développement [#360](https://github.com/betagouv/csplab/issues/360).
- Nettoyage des métiers dans l'ingestion [#398](https://github.com/betagouv/csplab/issues/398) et [#414](https://github.com/betagouv/csplab/issues/414).
- Mise à jour de la documentation CHANGELOG.md pour les versions 0.1.6 et 0.1.7 [#338](https://github.com/betagouv/csplab/issues/338) et [#375](https://github.com/betagouv/csplab/issues/375).
- Amélioration de la position et du bouton de fermeture des alertes toast [#354](https://github.com/betagouv/csplab/issues/354).
- Ajout d'une région live pour annoncer les résultats aux lecteurs d'écran [#353](https://github.com/betagouv/csplab/issues/353).
- Ajout d'une opacité de chargement sur la zone des résultats pendant les échanges htmx [#352](https://github.com/betagouv/csplab/issues/352).
- Mise à jour des dépendances dans les modules tycho-ocr et tycho [#363](https://github.com/betagouv/csplab/issues/363) et [#388](https://github.com/betagouv/csplab/issues/388).
