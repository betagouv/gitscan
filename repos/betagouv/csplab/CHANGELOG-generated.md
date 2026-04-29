## Changelog : csplab (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'ingestion et du traitement des offres d'emploi, ainsi que sur l'expérience utilisateur de la présentation des candidatures. Des améliorations techniques ont également été apportées pour optimiser l'infrastructure, les tests et la documentation.

### Évolutions fonctionnelles
- Les utilisateurs peuvent désormais fermer la fenêtre modale de présentation des candidatures en utilisant le bouton de retour du navigateur. [#444](https://github.com/betagouv/csplab/issues/444)
- L'organisation ou le ministère est maintenant affiché sur les cartes et dans les fenêtres modales des opportunités. [#443](https://github.com/betagouv/csplab/issues/443)
- Les filtres actifs sont correctement reflétés dans l'interface utilisateur lors du chargement de la page dans Tycho. [#380](https://github.com/betagouv/csplab/issues/380)
- Ajout de l'analyse Matomo pour suivre le parcours des candidats dans Tycho. [#358](https://github.com/betagouv/csplab/issues/358)
- Possibilité de filtrer les CVs par catégories dans Tycho. [#357](https://github.com/betagouv/csplab/issues/357)
- Amélioration de la gestion des documents en empêchant les documents ayant échoué de rester dans un état en attente et d'être retraités. [#452](https://github.com/betagouv/csplab/issues/452)
- Ajout de la documentation sur les dépendances système requises pour l'OCR local. [#453](https://github.com/betagouv/csplab/issues/453)

### Évolutions techniques
- Refactorisation des méthodes `find_by_xx` en `get_by_xx` pour une meilleure cohérence. [#458](https://github.com/betagouv/csplab/issues/458)
- Les conteneurs de test Tycho sont maintenant indépendants pour une meilleure isolation et fiabilité. [#457](https://github.com/betagouv/csplab/issues/457)
- Initialisation de la gestion de la couverture de code. [#449](https://github.com/betagouv/csplab/issues/449)
- Refactorisation de la journalisation pour utiliser l'interpolation de chaînes paresseuses. [#412](https://github.com/betagouv/csplab/issues/412)
- Suppression de la bibliothèque `pgvector` et des modèles associés. [#385](https://github.com/betagouv/csplab/issues/385)
- Mise en place d'une file d'attente et d'un broker pour gérer les tâches asynchrones (vectorisation, nettoyage). [#376](https://github.com/betagouv/csplab/issues/376)
- Utilisation d'un client HTTP asynchrone dans Tycho pour améliorer les performances. [#389](https://github.com/betagouv/csplab/issues/389)
- Ajout de tests d'accessibilité automatisés avec pytest-playwright et axe-playwright-python. [#157](https://github.com/betagouv/csplab/issues/157)
- Mise à jour des dépendances `pypdf` dans les modules OCR et Notebook pour corriger des failles de sécurité. [#401](https://github.com/betagouv/csplab/issues/401), [#402](https://github.com/betagouv/csplab/issues/402)
- Suppression de l'ancien index Elasticsearch. [#370](https://github.com/betagouv/csplab/issues/370)
- Ajout d'une tâche pour nettoyer les métiers dans Tycho. [#414](https://github.com/betagouv/csplab/issues/414)

### Autres changements
- Suppression de configurations, DTOs et bibliothèques inutilisées dans l'infrastructure d'ingestion. [#459](https://github.com/betagouv/csplab/issues/459)
- Réorganisation des tests pour une meilleure structure. [#451](https://github.com/betagouv/csplab/issues/451)
- Désactivation des validateurs de mots de passe en mode développement. [#448](https://github.com/betagouv/csplab/issues/448)
- Ajout d'une commande `make run-mvp` pour lancer tous les services MVP en une seule fois. [#420](https://github.com/betagouv/csplab/issues/420)
- Suppression de la fonctionnalité de recherche de corps inutilisée dans la présentation des candidatures. [#437](https://github.com/betagouv/csplab/issues/437)
- Correction du chemin de l'interpréteur Python dans VS Code. [#439](https://github.com/betagouv/csplab/issues/439)
- Ajout d'une couche optionnelle dans les modèles de commit. [#417](https://github.com/betagouv/csplab/issues/417)
- Mise à jour du fichier CHANGELOG.md pour la version 0.1.7. [#375](https://github.com/betagouv/csplab/issues/375) et 0.1.6 [#338](https://github.com/betagouv/csplab/issues/338)
- Correction du bootstrap pour qu'il fonctionne sur une configuration propre. [#399](https://github.com/betagouv/csplab/issues/399)
- Mise à jour des dépendances Tycho et OCR. [#388](https://github.com/betagouv/csplab/issues/388), [#363](https://github.com/betagouv/csplab/issues/363)
- Ajout de la possibilité de mapper les catégories aux offres. [#362](https://github.com/betagouv/csplab/issues/362)
- Implémentation de la récupération des offres détaillées via le client Talentsoft. [#344](https://github.com/betagouv/csplab/issues/344)
- Ajout de la recherche par ID externes dans le repository de documents bruts. [#345](https://github.com/betagouv/csplab/issues/345)
- Refactorisation de la vue des résultats de CV en use case et presenter. [#361](https://github.com/betagouv/csplab/issues/361)
- Correction d'un bug empêchant l'ouverture de la fenêtre modale après un filtrage. [#374](https://github.com/betagouv/csplab/issues/374)
- Correction d'un bug dans la gestion statique en développement. [#360](https://github.com/betagouv/csplab/issues/360)
- Correction d'un bug dans l'ingestion des documents. [#393](https://github.com/betagouv/csplab/issues/393)
- Suppression de la possibilité de gérer l'ingestion des offres dans `load_documents`. [#350](https://github.com/betagouv/csplab/issues/350)
