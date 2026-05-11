## Changelog : csplab (30 derniers jours, au 8 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ingestion et le traitement des offres, l'amélioration de la qualité du code et de l'infrastructure, ainsi que sur l'ajout de tests automatisés pour garantir la stabilité de l'application. Des améliorations sont également apportées à l'interface utilisateur, notamment pour la présentation des candidatures et des organisations.

### Évolutions fonctionnelles
- Ajout d'une page statique listant les conditions d'utilisation. [#227](https://github.com/betagouv/csplab/issues/227)
- Possibilité de filtrer les candidatures par catégorie A+. [#482](https://github.com/betagouv/csplab/issues/482)
- Affichage de l'organisation ou du ministère associé à une offre dans les cartes et les tiroirs de candidatures. [#443](https://github.com/betagouv/csplab/issues/443)
- Amélioration de la présentation des CV (styles et contenu). [#441](https://github.com/betagouv/csplab/issues/441)
- Possibilité de fermer les tiroirs modaux de la présentation des candidatures via la navigation du navigateur. [#444](https://github.com/betagouv/csplab/issues/444)
- Ajout de la possibilité d'archiver des offres lors du chargement. [#492](https://github.com/betagouv/csplab/issues/492)
- Intégration de la catégorie APLUS dans le nettoyage des offres. [#486](https://github.com/betagouv/csplab/issues/486)

### Évolutions techniques
- Mise en place d'une suite de tests E2E avec Playwright pour la présentation des candidatures. [#490](https://github.com/betagouv/csplab/issues/490)
- Refonte de l'architecture d'ingestion pour utiliser des tâches asynchrones avec un broker et une queue (Huey). [#376](https://github.com/betagouv/csplab/issues/376)
- Suppression de l'utilisation de pgvector et du modèle VectorizedDocumentModel. [#385](https://github.com/betagouv/csplab/issues/385)
- Remplacement de la configuration Pydantic dépréciée par SettingsConfigDict dans le module OCR. [#489](https://github.com/betagouv/csplab/issues/489)
- Amélioration de la gestion des connexions aux bases de données dans les tests d'ingestion. [#478](https://github.com/betagouv/csplab/issues/478)
- Mise à jour des dépendances pour améliorer la sécurité et la performance (pypdf, dependencies OCR, notebook, tycho). [#382](https://github.com/betagouv/csplab/issues/382), [#383](https://github.com/betagouv/csplab/issues/383), [#401](https://github.com/betagouv/csplab/issues/401), [#402](https://github.com/betagouv/csplab/issues/402), [#495](https://github.com/betagouv/csplab/issues/495), [#496](https://github.com/betagouv/csplab/issues/496), [#497](https://github.com/betagouv/csplab/issues/497)
- Refactorisation du code pour renommer les méthodes `find_by_xx` en `get_by_xx`. [#458](https://github.com/betagouv/csplab/issues/458)
- Amélioration de la documentation pour l'installation des hooks Git et des dépendances système pour l'OCR. [#472](https://github.com/betagouv/csplab/issues/472), [#453](https://github.com/betagouv/csplab/issues/453)
- Ajout de tests pour vérifier que les filtres actifs sont correctement reflétés dans l'interface utilisateur au chargement de la page. [#380](https://github.com/betagouv/csplab/issues/380)
- Suppression de code inutilisé et simplification de la configuration. [#459](https://github.com/betagouv/csplab/issues/459), [#479](https://github.com/betagouv/csplab/issues/479)

### Autres changements
- Mise à jour de la documentation CHANGELOG.md pour les versions 0.1.7 et 0.1.8. [#418](https://github.com/betagouv/csplab/issues/418), [#375](https://github.com/betagouv/csplab/issues/375)
- Amélioration de la documentation de l'API. [#480](https://github.com/betagouv/csplab/issues/480)
- Amélioration des commandes de chargement dans la documentation. [#481](https://github.com/betagouv/csplab/issues/481)
- Refactorisation des logs pour utiliser l'interpolation de chaînes paresseuses. [#412](https://github.com/betagouv/csplab/issues/412)
- Ajout de port override pour les services. [#391](https://github.com/betagouv/csplab/issues/391)
- Ajout d'une tâche pour nettoyer les métiers. [#397](https://github.com/betagouv/csplab/issues/397)
- Amélioration de l'affichage dans l'interface d'administration pour l'ingestion. [#469](https://github.com/betagouv/csplab/issues/469)
- Correction du chemin de l'interpréteur Python dans VSCode. [#439](https://github.com/betagouv/csplab/issues/439)
- Désactivation des validateurs de mot de passe en mode développement. [#448](https://github.com/betagouv/csplab/issues/448)
- Ajout d'une couche optionnelle dans les modèles de commit. [#417](https://github.com/betagouv/csplab/issues/417)
- Amélioration de l'organisation des tests. [#451](https://github.com/betagouv/csplab/issues/451)
- Augmentation de la taille de la clé de configuration. [#474](https://github.com/betagouv/csplab/issues/474)
- Ajout de la possibilité de supprimer des documents du repository vectoriel. [#421](https://github.com/betagouv/csplab/issues/421)
- Ajout d'un client TalentsoftBackClient. [#425](https://github.com/betagouv/csplab/issues/425)
- Initialisation de la version de coverage. [#449](https://github.com/betagouv/csplab/issues/449)
- Prévention du maintien des documents ayant échoué dans un état en attente. [#452](https://github.com/betagouv/csplab/issues/452)
- Amélioration de la parallélisation des tests E2E et restauration du calcul de la couverture. [#494](https://github.com/betagouv/csplab/issues/494)
