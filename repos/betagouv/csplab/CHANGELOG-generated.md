## Changelog : csplab (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'ingestion et du traitement des données, notamment des offres d'emploi, ainsi que sur l'optimisation de l'expérience utilisateur de la présentation des candidatures. Des améliorations techniques significatives ont été apportées à l'architecture, avec une migration vers une gestion asynchrone des tâches et la suppression de composants obsolètes. L'accessibilité a également été améliorée grâce à l'ajout de tests automatisés.

### Évolutions fonctionnelles
- Amélioration de la présentation des candidatures :
  - Possibilité de fermer la fenêtre modale de présentation de candidature en utilisant le bouton "Retour" du navigateur. [#444](https://github.com/betagouv/csplab/issues/444)
  - Affichage de l'organisation ou du ministère associé à une opportunité dans les cartes et les fenêtres modales. [#443](https://github.com/betagouv/csplab/issues/443)
  - Mise à jour du style et du contenu des CV dans la présentation MVP. [#441](https://github.com/betagouv/csplab/issues/441)
  - Reflet des filtres actifs dans l'interface utilisateur lors du chargement de la page des candidats (Tycho). [#380](https://github.com/betagouv/csplab/issues/380)
- Ingestion des données :
  - Prévention du blocage des documents ayant échoué dans un état "en attente" lors de l'ingestion. [#452](https://github.com/betagouv/csplab/issues/452)
  - Ajout de la suppression des vecteurs dans le dépôt vectoriel. [#421](https://github.com/betagouv/csplab/issues/421)
  - Chargement des données des métiers (Tycho). [#397](https://github.com/betagouv/csplab/issues/397)
  - Nettoyage des métiers (Tycho). [#398](https://github.com/betagouv/csplab/issues/398)
  - Mapping des catégories aux offres (ingestion). [#362](https://github.com/betagouv/csplab/issues/362)
  - Chargement des offres détaillées (ingestion). [#342](https://github.com/betagouv/csplab/issues/342)
- Intégration Talentsoft : Mise en place du client TalentsoftBackClient. [#425](https://github.com/betagouv/csplab/issues/425)
- Analyse : Ajout de Matomo pour le suivi de l'expérience utilisateur des candidats (Tycho). [#358](https://github.com/betagouv/csplab/issues/358)

### Évolutions techniques
- Architecture :
  - Migration vers une architecture asynchrone avec l'ajout d'un broker et d'une queue pour la gestion des tâches. [#376](https://github.com/betagouv/csplab/issues/376)
  - Suppression de la bibliothèque pgvector et du modèle VectorizedDocumentModel. [#385](https://github.com/betagouv/csplab/issues/385)
  - Suppression de l'intégration Elasticsearch (ES). [#370](https://github.com/betagouv/csplab/issues/370)
  - Refactoring de la gestion des tests, notamment pour l'embedding service (passage en asynchrone). [#442](https://github.com/betagouv/csplab/issues/442)
- Améliorations diverses :
  - Mise à jour des dépendances (pypdf, tycho, ocr, notebook). [#401](https://github.com/betagouv/csplab/issues/401), [#402](https://github.com/betagouv/csplab/issues/402), [#388](https://github.com/betagouv/csplab/issues/388), [#363](https://github.com/betagouv/csplab/issues/363)
  - Refactoring de la méthode de recherche (renommage find_by_xx en get_by_xx). [#458](https://github.com/betagouv/csplab/issues/458)
  - Refactoring du code de journalisation pour utiliser l'interpolation de chaînes paresseuses. [#412](https://github.com/betagouv/csplab/issues/412)
  - Refactoring du code de la vue des résultats du CV. [#361](https://github.com/betagouv/csplab/issues/361)

### Autres changements
- Outils :
  - Initialisation du versioning de la couverture de code. [#449](https://github.com/betagouv/csplab/issues/449)
  - Ajout d'un script `make run-mvp` pour lancer tous les services MVP en une seule commande. [#420](https://github.com/betagouv/csplab/issues/420)
  - Ajout de tests automatisés d'accessibilité avec pytest-playwright et axe-playwright-python. [#157](https://github.com/betagouv/csplab/issues/157)
  - Correction du chemin de l'interpréteur Python dans VS Code. [#439](https://github.com/betagouv/csplab/issues/439)
  - Correction du fonctionnement du bootstrap sur une installation fraîche. [#399](https://github.com/betagouv/csplab/issues/399)
  - Désactivation des validateurs de mot de passe en mode développement. [#448](https://github.com/betagouv/csplab/issues/448)
  - Ajout d'une couche optionnelle dans les modèles de commit. [#417](https://github.com/betagouv/csplab/issues/417)
- Documentation : Documentation des dépendances système requises pour l'OCR local. [#453](https://github.com/betagouv/csplab/issues/453)
- Publication : Mise à jour du CHANGELOG.md pour les versions 0.1.6 et 0.1.7. [#375](https://github.com/betagouv/csplab/issues/375), [#338](https://github.com/betagouv/csplab/issues/338)
- Suppression de code inutilisé : Suppression de configurations, DTOs et bibliothèques inutilisées dans l'infrastructure d'ingestion. [#459](https://github.com/betagouv/csplab/issues/459)
- Suppression de fonctionnalité : Suppression de la fonctionnalité de recherche de corps (corps de métier) non utilisée. [#437](https://github.com/betagouv/csplab/issues/437)
