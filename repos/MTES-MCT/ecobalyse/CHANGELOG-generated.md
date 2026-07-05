## Changelog : ecobalyse (30 derniers jours, au 02 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives aux données, notamment des mises à jour des données LCI pour divers produits alimentaires et matériaux (lait, sorgho, lin, haricots, amarante, agrumes, tomates, café, etc.). Des ajustements ont été apportés aux données relatives aux véhicules (batteries, pneus, câbles) et aux emballages. Des corrections et des améliorations ont également été apportées à l'interface utilisateur et à l'architecture du projet.

### Évolutions fonctionnelles
- Ajout de liens de documentation configurables. [#2577](https://github.com/MTES-MCT/ecobalyse/issues/2577)
- Mise à jour des ratios de transport routier/maritime. [#2575](https://github.com/MTES-MCT/ecobalyse/issues/2575)
- Ajout d'un champ d'origine par défaut pour les processus génériques. [#2414](https://github.com/MTES-MCT/ecobalyse/issues/2414)
- Amélioration de l'interface utilisateur pour la gestion des emballages dans le calculateur générique. [#2438](https://github.com/MTES-MCT/ecobalyse/issues/2438)
- Ajout de la possibilité de filtrer les processus invisibles dans le calculateur générique. [#2537](https://github.com/MTES-MCT/ecobalyse/issues/2537)
- Ajout de plusieurs exemples d'aliments dans l'interface. [#2563](https://github.com/MTES-MCT/ecobalyse/issues/2563)
- Ajout d'une région "Maghreb". [#2568](https://github.com/MTES-MCT/ecobalyse/issues/2568)
- Remplacement de l'unité "elecMJ" par "elecKwh". [#2561](https://github.com/MTES-MCT/ecobalyse/issues/2561)
- Ajout de la prise en charge de la phase d'utilisation pour les objets et véhicules. [#1710](https://github.com/MTES-MCT/ecobalyse/issues/1710)
- Ajout de pays aux explorateurs d'objets/véhicules. [#1724](https://github.com/MTES-MCT/ecobalyse/issues/1724)

### Évolutions techniques
- Mise à jour des dépendances Litestar, Sentry et des outils de développement. [#2584](https://github.com/MTES-MCT/ecobalyse/issues/2584), [#2585](https://github.com/MTES-MCT/ecobalyse/issues/2585), [#2583](https://github.com/MTES-MCT/ecobalyse/issues/2583), [#2582](https://github.com/MTES-MCT/ecobalyse/issues/2582)
- Refactorisation du pipeline de données pour la gestion des fichiers de transport. [#2535](https://github.com/MTES-MCT/ecobalyse/issues/2535)
- Utilisation de JSON pour stocker les composants. [#2393](https://github.com/MTES-MCT/ecobalyse/issues/2393)
- Mise à jour des dépendances Node.js. [#2532](https://github.com/MTES-MCT/ecobalyse/issues/2532), [#2486](https://github.com/MTES-MCT/ecobalyse/issues/2486), [#2499](https://github.com/MTES-MCT/ecobalyse/issues/2499), [#2500](https://github.com/MTES-MCT/ecobalyse/issues/2500)
- Ajout d'un tag `productmassdependent` pour les processus. [#2579](https://github.com/MTES-MCT/ecobalyse/issues/2579)
- Mise à jour de la base de données et des modèles via une migration. [#2536](https://github.com/MTES-MCT/ecobalyse/issues/2536)
- Amélioration de la fiabilité des tests E2E. [#2422](https://github.com/MTES-MCT/ecobalyse/issues/2422)

### Autres changements
- Mises à jour des données LCI pour plusieurs produits : lait, sorgho, seigle, graines de lin, haricots, amarante, tournesol, café, tomate, orange, etc.
- Ajout de données pour les batteries de véhicules électriques. [#2459](https://github.com/MTES-MCT/ecobalyse/issues/2459), [#2453](https://github.com/MTES-MCT/ecobalyse/issues/2453), [#2406](https://github.com/MTES-MCT/ecobalyse/issues/2406)
- Ajout de données pour les emballages en bois et papier. [#2404](https://github.com/MTES-MCT/ecobalyse/issues/2404)
- Correction de la syntaxe du modèle d'issue. [#2544](https://github.com/MTES-MCT/ecobalyse/issues/2544)
- Suppression de processus obsolètes pour les véhicules. [#2472](https://github.com/MTES-MCT/ecobalyse/issues/2472)
- Amélioration de la formulation pour les aliments. [#2523](https://github.com/MTES-MCT/ecobalyse/issues/2523)
