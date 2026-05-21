## Changelog : csplab (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'ingestion et de l'archivage des offres d'emploi, l'ajout de nouvelles fonctionnalités pour la présentation des candidatures et l'amélioration de l'infrastructure et des outils de développement. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout de la possibilité d'afficher l'organisation ou le ministère sur les cartes et dans les détails des offres d'emploi. [#443](https://github.com/betagouv/csplab/issues/443)
- Amélioration de l'affichage des offres d'emploi dans le tiroir (drawer) de candidature. [#550](https://github.com/betagouv/csplab/issues/550)
- Ajout de pages statiques pour les mentions légales, la politique de confidentialité et l'accessibilité. [#225](https://github.com/betagouv/csplab/issues/225), [#226](https://github.com/betagouv/csplab/issues/226), [#224](https://github.com/betagouv/csplab/issues/224)
- Implémentation de la vectorisation pour les métiers, permettant une recherche plus performante. [#551](https://github.com/betagouv/csplab/issues/551)
- Ajout d'un endpoint API pour lister les offres d'emploi. [#440](https://github.com/betagouv/csplab/issues/440)
- Possibilité d'archiver des offres d'emploi via des webhooks. [#512](https://github.com/betagouv/csplab/issues/512)
- Amélioration du filtre de catégories pour inclure A+. [#482](https://github.com/betagouv/csplab/issues/482)

### Évolutions techniques
- Standardisation des noms de méthodes pour la récupération de données (utilisation de `get_xxxx`). [#568](https://github.com/betagouv/csplab/issues/568)
- Refactorisation de l'API et de la documentation. [#504](https://github.com/betagouv/csplab/issues/504), [#480](https://github.com/betagouv/csplab/issues/480)
- Amélioration de la gestion des erreurs lors de l'ingestion de documents, en isolant et en loguant les documents problématiques. [#509](https://github.com/betagouv/csplab/issues/509)
- Mise en place de tests E2E avec Playwright pour la présentation des CV. [#490](https://github.com/betagouv/csplab/issues/490)
- Suppression de la dépendance pgvector. [#386](https://github.com/betagouv/csplab/issues/386)
- Refactorisation de l'architecture pour séparer les applications "tycho" et "web". [#515](https://github.com/betagouv/csplab/issues/515)
- Amélioration de la gestion des connexions dans les tests. [#478](https://github.com/betagouv/csplab/issues/478)
- Ajout de tests de couverture. [#498](https://github.com/betagouv/csplab/issues/498)
- Mise à jour des dépendances (pypdf, python-dateutil). [#401](https://github.com/betagouv/csplab/issues/401), [#402](https://github.com/betagouv/csplab/issues/402), [#425](https://github.com/betagouv/csplab/issues/425)

### Autres changements
- Mise à jour de la documentation d'installation, notamment pour les hooks Git. [#472](https://github.com/betagouv/csplab/issues/472)
- Amélioration de la configuration de la taille de la clé de chiffrement. [#474](https://github.com/betagouv/csplab/issues/474)
- Mise à jour du CHANGELOG.md pour les versions 0.1.8 et 0.1.9. [#485](https://github.com/betagouv/csplab/issues/485), [#606](https://github.com/betagouv/csplab/issues/606)
- Ajout de la gestion des caractères '+' non encodés dans les signatures. [#506](https://github.com/betagouv/csplab/issues/506)
- Amélioration de la robustesse du mapping des ministères. [#548](https://github.com/betagouv/csplab/issues/548)
- Renommage de colonnes pour ConcoursCleaner. [#511](https://github.com/betagouv/csplab/issues/511)
- Correction de bugs divers et améliorations de la qualité du code.
