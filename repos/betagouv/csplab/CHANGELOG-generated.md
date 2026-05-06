## Changelog : csplab (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'ingestion et du traitement des offres, l'optimisation des tests et de l'infrastructure, ainsi que l'ajout de nouvelles fonctionnalités pour l'expérience candidat, notamment autour de la visualisation des CV et de l'accessibilité. Des améliorations de la documentation et de la configuration ont également été apportées.

### Évolutions fonctionnelles
- Possibilité d'archiver des offres via l'interface d'ingestion. [#455](https://github.com/betagouv/csplab/issues/455)
- Amélioration de l'expérience utilisateur pour les candidats :
    - Possibilité de fermer le tiroir modal de CV via la navigation du navigateur. [#444](https://github.com/betagouv/csplab/issues/444)
    - Affichage de l'organisation ou du ministère dans les cartes d'opportunités et les tiroirs. [#443](https://github.com/betagouv/csplab/issues/443)
    - Mise à jour des styles et du contenu du CV MVP. [#441](https://github.com/betagouv/csplab/issues/441)
    - Refonte de la vue des résultats de CV en utilisant une approche use case/presenter. [#361](https://github.com/betagouv/csplab/issues/361)
- Ajout d'analytics Matomo pour suivre le parcours candidat. [#358](https://github.com/betagouv/csplab/issues/358)
- Amélioration de l'affichage des filtres actifs dans l'interface Tycho. [#380](https://github.com/betagouv/csplab/issues/380)
- Les documents ayant échoué lors de l'ingestion ne restent plus dans un état en attente et ne sont plus retraités en boucle. [#452](https://github.com/betagouv/csplab/issues/452)

### Évolutions techniques
- Refonte de l'architecture d'ingestion :
    - Suppression de code et de configurations inutilisés. [#459](https://github.com/betagouv/csplab/issues/459)
    - Mise en place d'une file d'attente asynchrone pour la vectorisation et le nettoyage des données. [#381](https://github.com/betagouv/csplab/issues/381)
    - Intégration d'un client TalentsoftBackClient. [#425](https://github.com/betagouv/csplab/issues/425)
- Amélioration des tests :
    - Homogénéisation des tests et refactoring des factories et fixtures (Tycho). [#467](https://github.com/betagouv/csplab/issues/467)
    - Tests des conteneurs indépendants (Tycho). [#457](https://github.com/betagouv/csplab/issues/457)
    - Ajout de tests d'accessibilité automatisés avec pytest-playwright et axe-playwright-python. [#157](https://github.com/betagouv/csplab/issues/157)
    - Initialisation de la gestion de la couverture de code. [#449](https://github.com/betagouv/csplab/issues/449)
- Suppression de pgvector et du modèle VectorizedDocumentModel. [#385](https://github.com/betagouv/csplab/issues/385)
- Utilisation d'un client HTTP asynchrone pour l'ingestion. [#389](https://github.com/betagouv/csplab/issues/389)
- Mise à jour des dépendances : pypdf, dependencies Tycho et Notebook. [#401](https://github.com/betagouv/csplab/issues/401), [#388](https://github.com/betagouv/csplab/issues/388), [#363](https://github.com/betagouv/csplab/issues/363)

### Autres changements
- Amélioration de la documentation :
    - Mise à jour des instructions d'installation des hooks Git. [#472](https://github.com/betagouv/csplab/issues/472)
    - Documentation des dépendances système requises pour l'OCR local. [#453](https://github.com/betagouv/csplab/issues/453)
    - Ajout de documentation pour l'API. [#396](https://github.com/betagouv/csplab/issues/396)
- Amélioration de la configuration :
    - Définition d'une taille de clé appropriée. [#474](https://github.com/betagouv/csplab/issues/474)
    - Désactivation des validateurs de mot de passe en mode développement. [#448](https://github.com/betagouv/csplab/issues/448)
- Refactoring du code :
    - Renommage des méthodes `find_by_xx` en `get_by_xx`. [#458](https://github.com/betagouv/csplab/issues/458)
    - Refactoring du logging pour utiliser l'interpolation de chaînes paresseuses. [#412](https://github.com/betagouv/csplab/issues/412)
- Amélioration de l'interface d'administration pour visualiser le workflow d'ingestion. [#469](https://github.com/betagouv/csplab/issues/469)
- Ajout de tâches pour nettoyer les métiers (Tycho). [#414](https://github.com/betagouv/csplab/issues/414)
- Correction d'un bug empêchant le bootstrap de fonctionner sur une installation propre. [#399](https://github.com/betagouv/csplab/issues/399)
- Correction d'un bug dans VSCode concernant le chemin de l'interpréteur Python. [#439](https://github.com/betagouv/csplab/issues/439)
- Suppression d'Elasticsearch (ES). [#370](https://github.com/betagouv/csplab/issues/370)
- Ajout d'une surcharge de port pour les services. [#391](https://github.com/betagouv/csplab/issues/391)
- Ajout d'une couche optionnelle dans les modèles de commit. [#417](https://github.com/betagouv/csplab/issues/417)
