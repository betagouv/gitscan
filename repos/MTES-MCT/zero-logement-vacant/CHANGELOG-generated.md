## Changelog : zero-logement-vacant (30 derniers jours)

### Résumé
Les dernières mises à jour de zero-logement-vacant se concentrent sur l'amélioration de l'interface utilisateur, l'ajout de nouvelles fonctionnalités pour la gestion des documents et des logements, ainsi que des optimisations techniques pour la performance et la sécurité de l'application. Des améliorations ont été apportées à la gestion des données énergétiques des logements et à la gestion des campagnes.

### Évolutions fonctionnelles
- Ajout d'un onglet pour la gestion des documents liés aux logements, permettant l'upload et la consultation de documents. [#1571](https://github.com/MTES-MCT/zero-logement-vacant/pull/1571)
- Possibilité de filtrer les logements par localisation relative. [#1629](https://github.com/MTES-MCT/zero-logement-vacant/pull/1629)
- Amélioration de l'affichage des informations énergétiques des logements (DPE, GES, RNB) dans la vue détaillée. [#1571](https://github.com/MTES-MCT/zero-logement-vacant/pull/1571)
- Suppression des liens vides dans le pied de page. [#1642](https://github.com/MTES-MCT/zero-logement-vacant/pull/1642)
- Refonte de l'interface pour la création et la modification des campagnes. [#1652](https://github.com/MTES-MCT/zero-logement-vacant/pull/1652)
- Possibilité de regrouper des logements dans le cadre des campagnes. [#1652](https://github.com/MTES-MCT/zero-logement-vacant/pull/1652)
- Suppression de la possibilité de modifier le nom du propriétaire d'un logement. [#1635](https://github.com/MTES-MCT/zero-logement-vacant/pull/1635)

### Évolutions techniques
- Amélioration de la sécurité de l'application avec l'ajout d'en-têtes de sécurité explicites et la correction de vulnérabilités. [#1658](https://github.com/MTES-MCT/zero-logement-vacant/pull/1658)
- Refactorisation de l'architecture frontend avec l'utilisation de composants MUI pour la mise en page. [#1646](https://github.com/MTES-MCT/zero-logement-vacant/pull/1646)
- Optimisation de la configuration NX pour améliorer l'efficacité du cache et les performances de build. [#1606](https://github.com/MTES-MCT/zero-logement-vacant/pull/1606)
- Migration de la bibliothèque Highland vers Web Streams. [#1622](https://github.com/MTES-MCT/zero-logement-vacant/pull/1622)
- Mise à jour des dépendances (webpack, axios, express). [#1607](https://github.com/MTES-MCT/zero-logement-vacant/pull/1607)
- Amélioration du workflow de développement avec l'ajout de règles et d'outils d'IA pour la vérification du code et l'automatisation des tâches. [#1659](https://github.com/MTES-MCT/zero-logement-vacant/pull/1659)
- Utilisation d'esbuild pour la construction du serveur afin d'améliorer la vitesse de build. [#1606](https://github.com/MTES-MCT/zero-logement-vacant/pull/1606)
- Correction de tests et amélioration de la couverture de test.

### Autres changements
- Mise à jour des données de référence pour les codes INSEE et les sources externes.
- Correction d'un problème lié à l'importation des données DPE.
- Mise à jour de la documentation.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Suppression de configurations inutiles.
- Synchronisation des fichiers de configuration avec l'environnement de production.
- Ajout de scripts pour l'exportation de données.
- Mise à jour des modèles de données.
- Correction de la gestion des dates DPE.
